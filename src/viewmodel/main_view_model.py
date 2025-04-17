from datetime import datetime

from PySide6.QtCore import QObject, QTimer, Signal, Slot

from model.data_models import ApplicationState


class MainViewModel(QObject):
    time_updated = Signal(str)
    state_updated = Signal(object)
    channel_clicked = Signal(int)
    manual_mode_clicked = Signal()
    warning_shown = Signal(str)

    def __init__(self, state: ApplicationState, parent=None):
        super().__init__(parent)
        self.state = state

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    @Slot()
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M | %d.%m.%Y")
        self.time_updated.emit(current_time)

    @Slot(int)
    def on_channel_tale_click(self, channel_id: int):
        channel = self.state.channels[channel_id]
        if channel:
            self.state.selected_channel_id = channel_id
            self.state_updated.emit(self.state)
            self.channel_clicked.emit(channel_id)

    @Slot()
    def toggle_auto_watering(self):
        # todo: add validation
        self.state.is_auto_watering_enabled = not self.state.is_auto_watering_enabled
        self.state_updated.emit(self.state)

    @Slot()
    def on_manual_mode_clicked(self):
        if self.state.is_auto_watering_enabled:
            self.warning_shown.emit("Auto watering is enabled.\nDisable it before.")
        else:
            self.manual_mode_clicked.emit()
