from datetime import datetime

from PySide6.QtCore import QObject, QTimer, Signal, Slot, SignalInstance

from model.data_models import ApplicationState


class MainViewModel(QObject):
    time_updated = Signal(str)
    state_updated = Signal(ApplicationState)
    warning_requested = Signal(str)

    def __init__(self, state: ApplicationState, parent=None):
        super().__init__(parent)
        self.state = state

        self._timer = QTimer(self)
        self._timer.timeout.connect(self.refresh_time)
        self._timer.start(1000)
        self.refresh_time()

    @Slot()
    def refresh_time(self):
        current_time = datetime.now().strftime("%H:%M | %d.%m.%Y")
        self.time_updated.emit(current_time)

    @Slot(int)
    def select_channel(self, channel_id: int):
        if channel_id in self.state.channels:
            self.state.selected_channel_id = channel_id
            self.state_updated.emit(self.state)

    @Slot()
    def toggle_auto_watering(self):
        # todo: add validation
        self.state.schedule.is_auto_watering_enabled = not self.state.schedule.is_auto_watering_enabled
        self.state_updated.emit(self.state)

    @Slot(SignalInstance)
    def toggle_manual_mode(self, manual_mode_requested: SignalInstance):
        if self.state.schedule.is_auto_watering_enabled:
            self.warning_requested.emit("Auto watering is enabled.\nDisable it before.")
        else:
            manual_mode_requested.emit()
