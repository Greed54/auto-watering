from PySide6.QtCore import QObject, Slot, Signal

from model.data_models import ApplicationState, Group


class ChannelSettingsViewModel(QObject):
    settings_saved = Signal(object)

    def __init__(self, state: ApplicationState, parent=None):
        super().__init__(parent)
        self.state = state

    @Slot(int, bool, int)
    def on_save(self, channel_id: int, is_active: bool, group_id: int):
        channel = self.state.channels[channel_id]
        if channel:
            self.state.selected_channel_id = channel_id
            channel.is_active = is_active
            channel.group_id = group_id

            if not self.state.groups.get(group_id, None):
                self.state.groups.setdefault(group_id, Group(group_id))

            self.settings_saved.emit(self.state)
