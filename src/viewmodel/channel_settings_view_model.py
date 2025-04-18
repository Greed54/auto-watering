from PySide6.QtCore import QObject, Slot, Signal

from model.data_models import ApplicationState, Group


class ChannelSettingsViewModel(QObject):
    state_changed = Signal(ApplicationState)
    settings_saved = Signal()

    def __init__(self, state: ApplicationState, parent=None):
        super().__init__(parent)
        self.state = state

    def load(self):
        self.state_changed.emit(self.state)

    @Slot(int, bool, int)
    def save_settings(self, channel_id: int, is_active: bool, group_id: int):
        channel = self.state.channels.get(channel_id)
        if channel is None:
            return

        self.state.selected_channel_id = channel_id
        channel.is_active = is_active
        channel.group_id = group_id

        if group_id not in self.state.groups:
            self.state.groups[group_id] = Group(id=group_id)

        self.state_changed.emit(self.state)
        self.settings_saved.emit()
