import copy
from datetime import time
from typing import Optional, Dict

from PySide6.QtCore import QObject, Signal, Slot, QTime

from model.data_models import ApplicationState


class ScheduleSettingsViewModel(QObject):
    sunset_mode_changed = Signal(bool)
    start_time_changed = Signal(object)  # QTime | None
    end_time_changed = Signal(object)  # QTime | None
    interval_changed = Signal(object)  # QTime | None
    groups_loaded = Signal(object)
    warning_requested = Signal(str)
    save_enabled = Signal(bool)

    def __init__(self, state: ApplicationState, parent=None):
        super().__init__(parent)
        self._state = state
        self._local_schedule = None
        self._local_groups: Dict[int, time] = {}

    @Slot()
    def load(self):
        if self._state.schedule.is_auto_watering_enabled:
            self.warning_requested.emit(
                "You cannot change the schedule settings while the automatic mode is active. Disable it before doing so.")
            self.save_enabled.emit(False)
        else:
            self.save_enabled.emit(True)
        self._from_state_to_local()

    @Slot()
    def close(self):
        self._from_state_to_local()

    @Slot(bool)
    def set_sunset_mode(self, on: bool):
        self._local_schedule["sunsetMode"] = on
        self.sunset_mode_changed.emit(on)

    @Slot(QTime)
    def set_start_time(self, qt: QTime):
        if qt is None:
            self._local_schedule["start_time"] = None
        else:
            self._local_schedule["start_time"] = time(qt.hour(), qt.minute(), qt.second())

    @Slot(QTime)
    def set_end_time(self, qt: QTime):
        if qt is None:
            self._local_schedule["end_time"] = None
        else:
            self._local_schedule["end_time"] = time(qt.hour(), qt.minute(), qt.second())

    @Slot(QTime)
    def set_interval(self, qt: QTime):
        if qt is None:
            self._local_schedule["interval"] = time(0, 0)
        else:
            self._local_schedule["interval"] = time(qt.hour(), qt.minute(), qt.second())

    @Slot(int, QTime)
    def set_group_duration(self, gid: int, qt: QTime):
        if qt is None:
            self._local_groups[gid] = time(0, 0, 0)
        else:
            self._local_groups[gid] = time(qt.hour(), qt.minute(), qt.second())

    @Slot()
    def save(self):
        schedule = self._state.schedule
        schedule.sunset_mode = self._local_schedule["sunsetMode"]
        schedule.start_time = self._local_schedule["start_time"]
        schedule.end_time = self._local_schedule["end_time"]
        schedule.cycle_interval = self._local_schedule["interval"]

        for gid, duration in self._local_groups.items():
            if gid in self._state.groups:
                self._state.groups[gid].watering_duration = duration

    def _from_state_to_local(self):
        schedule = self._state.schedule
        self._local_schedule = {
            "sunsetMode": schedule.sunset_mode,
            "start_time": schedule.start_time,
            "end_time": schedule.end_time,
            "interval": schedule.cycle_interval,
        }
        self._local_groups = {
            gid: copy.copy(gr.watering_duration) for gid, gr in self._state.groups.items()
        }
        self.sunset_mode_changed.emit(self._local_schedule["sunsetMode"])
        start_time = self._to_q_time(self._local_schedule["start_time"])
        end_time = self._to_q_time(self._local_schedule["end_time"])
        interval = self._to_q_time(self._local_schedule["interval"])
        self.start_time_changed.emit(start_time)
        self.end_time_changed.emit(end_time)
        self.interval_changed.emit(interval)
        self.groups_loaded.emit(self._local_groups)

    @staticmethod
    def _to_q_time(t: Optional[time]):
        if t is None:
            return None
        return QTime(t.hour, t.minute, t.second)
