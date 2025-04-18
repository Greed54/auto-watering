import threading
import time as t
from datetime import datetime, time, timedelta
from typing import Dict, Callable, Optional

from model.data_models import ApplicationState
from model.irrigation import IrrigationController


class AutoWateringScheduler:
    MIN_PUMP_OFF_DELAY = 1  # seconds to wait after pump off

    def __init__(
            self,
            state: ApplicationState,
            controller: IrrigationController,
            on_state_change: Callable[[ApplicationState], None] = None
    ):
        self._app_state = state
        self._scheduler_state = state.scheduler_state
        self._controller = controller
        self._notify_cb = on_state_change

        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self._thread = None

        # recover any in-progress cycle
        self._recover_state()

    def start(self):
        """Start the scheduler loop in a background thread."""
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run_loop, daemon=True)
        self._thread.start()

    def stop(self):
        """Stop the scheduler immediately and close all outputs."""
        self._stop_event.set()
        if self._thread:
            self._thread.join()
        self._controller.close_all()
        self._notify()

    def pause(self):
        """Pause mid-cycle: stop pump and valves immediately."""
        if self._scheduler_state.in_progress and not self._pause_event.is_set():
            self._pause_event.set()
            self._controller.off_pump()
            self._controller.close_all()
            self._notify()

    def resume(self):
        """Resume from pause: reopen valves for the current group, then pump."""
        if self._scheduler_state.in_progress and self._pause_event.is_set():
            self._pause_event.clear()
            gid = self._scheduler_state.current_group_id
            if gid is not None:
                for ch in self._app_state.channels.values():
                    if ch.group_id == gid and ch.is_active:
                        self._controller.open_valve(ch.id)
            self._controller.on_pump()
            self._notify()

    @property
    def is_watering(self) -> bool:
        """Return True if a watering cycle is currently active."""
        return self._scheduler_state.in_progress

    def get_next_run_times(self) -> Dict[int, Optional[datetime]]:
        """
        Compute the next open time for each channel based on active groups only.
        Return None for channels never active and never run.
        """
        base = self._scheduler_state.next_cycle_time or datetime.now()
        if self._scheduler_state.in_progress and self._scheduler_state.last_cycle_start:
            base = self._scheduler_state.last_cycle_start

        # determine active group IDs
        active_gids = sorted({
            ch.group_id for ch in self._app_state.channels.values()
            if ch.is_active and ch.group_id in self._app_state.groups
        })

        # build per‑group offsets
        offsets: Dict[int, datetime] = {}
        cum = timedelta()
        for gid in active_gids:
            grp = self._app_state.groups[gid]
            offsets[gid] = base + cum
            dur = grp.watering_duration
            cum += timedelta(hours=dur.hour, minutes=dur.minute, seconds=dur.second)

        # assign per‑channel
        result: Dict[int, Optional[datetime]] = {}
        for ch in self._app_state.channels.values():
            if not ch.is_active and ch.next_watering_time is None:
                result[ch.id] = None
            else:
                result[ch.id] = offsets.get(ch.group_id, base)
        return result

    def _notify(self):
        if self._notify_cb:
            self._notify_cb(self._app_state)

    def _recover_state(self):
        """
        Restore scheduler_state on startup:
        - If a cycle was mid-progress, calculate remaining time.
        - Otherwise reset in_progress and schedule the next cycle.
        """
        ss = self._scheduler_state
        now = datetime.now()

        if ss.last_cycle_start:
            elapsed = (now - ss.last_cycle_start).total_seconds()
            total = sum(
                self._time_to_seconds(g.watering_duration)
                for g in self._app_state.groups.values()
            )

            if ss.in_progress and elapsed < total:
                cum = 0
                for gid, grp in sorted(self._app_state.groups.items()):
                    d = self._time_to_seconds(grp.watering_duration)
                    if elapsed < cum + d:
                        ss.current_group_id = gid
                        ss.group_remaining_sec = int(cum + d - elapsed)
                        break
                    cum += d

                ss.next_cycle_time = ss.last_cycle_start + timedelta(
                    hours=self._app_state.schedule.cycle_interval.hour,
                    minutes=self._app_state.schedule.cycle_interval.minute,
                    seconds=self._app_state.schedule.cycle_interval.second
                )
                return

        # no unfinished cycle
        ss.in_progress = False
        ss.current_group_id = None
        ss.group_remaining_sec = 0
        ss.next_cycle_time = now

    def _is_in_watering_window(self) -> bool:
        """Check if now is within the allowed watering window."""
        schedule_settings = self._app_state.schedule
        now = datetime.now().time()

        if schedule_settings.sunset_mode:
            return True
        if schedule_settings.start_time and schedule_settings.end_time:
            return schedule_settings.start_time <= now <= schedule_settings.end_time
        return False

    def _run_loop(self):
        """Main loop: wait for the next cycle, then execute it."""
        while not self._stop_event.is_set():
            schedule_settings = self._app_state.schedule
            ss = self._scheduler_state

            if not schedule_settings.is_auto_watering_enabled or not self._is_in_watering_window():
                t.sleep(1)
                continue

            # skip if no channel is active
            if not any(ch.is_active for ch in self._app_state.channels.values()):
                interval = self._app_state.schedule.cycle_interval
                ss.next_cycle_time = datetime.now() + timedelta(
                    hours=interval.hour,
                    minutes=interval.minute,
                    seconds=interval.second
                )
                self._notify()
                t.sleep(1)
                continue

            now = datetime.now()
            if ss.next_cycle_time and now < ss.next_cycle_time:
                t.sleep(min((ss.next_cycle_time - now).total_seconds(), 1))
                continue

            self._start_cycle()

    def _start_cycle(self):
        """
        Execute one full cycle:
        1) for each active group: open active valves, then pump at first group
        2) wait group duration, respecting pause/resume
        3) close valves of each group; after all groups: stop pump, delay, close all
        """
        ss = self._scheduler_state
        ss.in_progress = True
        ss.last_cycle_start = datetime.now()
        ss.current_group_id = None
        self._notify()

        # only groups with active channels
        group_ids = sorted({
            ch.group_id for ch in self._app_state.channels.values()
            if ch.is_active and ch.group_id in self._app_state.groups
        })

        for idx, gid in enumerate(group_ids):
            if self._stop_event.is_set() or not self._app_state.schedule.is_auto_watering_enabled:
                break

            ss.current_group_id = gid
            self._notify()

            # open active valves of this group
            for ch in self._app_state.channels.values():
                if ch.group_id == gid and ch.is_active:
                    self._controller.open_valve(ch.id)
            self._notify()

            # start pump once at the first group
            if idx == 0:
                self._controller.on_pump()
                self._notify()

            # countdown with pause support
            ss.group_remaining_sec = self._time_to_seconds(
                self._app_state.groups[gid].watering_duration
            )
            self._notify()
            while ss.group_remaining_sec > 0 and not self._stop_event.is_set():
                if self._pause_event.is_set():
                    t.sleep(0.1)
                    continue
                t.sleep(1)
                ss.group_remaining_sec -= 1
                self._notify()

            # close valves of this group
            for ch in self._app_state.channels.values():
                if ch.group_id == gid:
                    self._controller.close_valve(ch.id)
            self._notify()

        # stop pump first, wait, then close all valves
        self._controller.off_pump()
        self._notify()
        t.sleep(self.MIN_PUMP_OFF_DELAY)
        self._controller.close_all()
        self._notify()

        # reset state and schedule the next run
        ss.in_progress = False
        ss.current_group_id = None
        ss.group_remaining_sec = 0
        ss.next_cycle_time = ss.last_cycle_start + timedelta(
            hours=self._app_state.schedule.cycle_interval.hour,
            minutes=self._app_state.schedule.cycle_interval.minute,
            seconds=self._app_state.schedule.cycle_interval.second
        )
        self._notify()

    @staticmethod
    def _time_to_seconds(t_obj: time) -> int:
        return t_obj.hour * 3600 + t_obj.minute * 60 + t_obj.second
