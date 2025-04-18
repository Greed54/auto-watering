from PySide6.QtCore import QObject, Signal

from model.data_models import ApplicationState
from model.irrigation import IrrigationController
from model.scheduler import AutoWateringScheduler


class QtSchedulerAdapter(QObject):
    state_changed = Signal(ApplicationState)

    def __init__(self, state: ApplicationState, controller: IrrigationController):
        super().__init__()
        # wrap CoreScheduler, pass callback into _on_core_state
        self._core = AutoWateringScheduler(state, controller, on_state_change=self._on_core_state)

    def start(self):
        self._core.start()

    def stop(self):
        self._core.stop()

    def pause(self):
        self._core.pause()

    def resume(self):
        self._core.resume()

    def is_watering(self) -> bool:
        return self._core.is_watering

    def get_next_run_times(self):
        return self._core.get_next_run_times()

    def _on_core_state(self, state: ApplicationState):
        # forward to Qt world
        self.state_changed.emit(state)
