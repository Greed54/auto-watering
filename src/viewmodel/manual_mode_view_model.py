from datetime import datetime

from PySide6.QtCore import QObject, Signal, Slot, QTimer

from model.data_models import ApplicationState


class ManualModeViewModel(QObject):
    time_updated = Signal(str)
    state_updated = Signal(object)
    auto_mode_clicked = Signal()

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

    @Slot()
    def on_auto_mode_clicked(self):
        self.state.pump.is_enabled = False
        for channel in self.state.channels.values():
            channel.is_enabled = False
        self.auto_mode_clicked.emit()

    @Slot()
    def on_channel_tale_click(self, channel_id: int):
        channel = self.state.channels[channel_id]
        if channel:
            channel.is_enabled = not channel.is_enabled
            self.state_updated.emit(self.state)

    @Slot()
    def on_pump_tale_click(self):
        self.state.pump.is_enabled = not self.state.pump.is_enabled
        self.state_updated.emit(self.state)
