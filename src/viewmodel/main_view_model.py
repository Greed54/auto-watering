from datetime import datetime

from PySide6.QtCore import QObject, QTimer, Signal, Slot

from model.data_models import ApplicationState


class MainViewModel(QObject):
    time_updated = Signal(str)
    state_updated = Signal(ApplicationState)
    channel_selected = Signal(int)
    manual_mode_requested = Signal()
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
            self.channel_selected.emit(channel_id)

    @Slot()
    def toggle_auto_watering(self):
        # todo: add validation
        self.state.is_auto_watering_enabled = not self.state.is_auto_watering_enabled
        self.state_updated.emit(self.state)

    @Slot()
    def on_manual_mode_clicked(self):
        if self.state.is_auto_watering_enabled:
            self.warning_requested.emit("Auto watering is enabled.\nDisable it before.")
        else:
            self.manual_mode_requested.emit()
