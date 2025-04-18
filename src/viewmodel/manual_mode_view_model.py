from datetime import datetime

from PySide6.QtCore import QObject, Signal, Slot, QTimer

from model.data_models import ApplicationState


class ManualModeViewModel(QObject):
    time_updated = Signal(str)
    state_updated = Signal(ApplicationState)
    auto_mode_requested = Signal()

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

    @Slot()
    def enable_auto__mode(self):
        self.state.pump.is_enabled = False
        for channel in self.state.channels.values():
            channel.is_enabled = False
        self.state_updated.emit(self.state)
        self.auto_mode_requested.emit()

    @Slot()
    def toggle_channel(self, channel_id: int):
        channel = self.state.channels[channel_id]
        if channel:
            channel.is_enabled = not channel.is_enabled
            self.state_updated.emit(self.state)

    @Slot()
    def toggle_pump(self):
        self.state.pump.is_enabled = not self.state.pump.is_enabled
        self.state_updated.emit(self.state)
