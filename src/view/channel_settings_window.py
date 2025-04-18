from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow

from model.data_models import ApplicationState
from ui.ChannelSettingsScreen import Ui_ChannelSettingsWindow
from viewmodel.channel_settings_view_model import ChannelSettingsViewModel


class ChannelSettingsWindow(QMainWindow):
    settings_saved = Signal()

    def __init__(self, state: ApplicationState):
        super().__init__()
        self._ui = Ui_ChannelSettingsWindow()
        self._ui.setupUi(self)
        self._view_model = ChannelSettingsViewModel(state)

        self._ui.save_settings_btn.clicked.connect(self._on_save_clicked)
        self._view_model.state_changed.connect(self._on_state_updated)

    def showEvent(self, event):
        self._view_model.load()
        super().showEvent(event)

    def _on_state_updated(self, state: ApplicationState):
        cid = state.selected_channel_id
        channel = state.channels.get(cid)
        if channel is None:
            return

        self._ui.channel_number_label.setText(str(cid))

        self._ui.channel_active_check_box.setChecked(channel.is_active)

        idx = channel.group_id - 1
        if 0 <= idx < self._ui.group_combo_box.count():
            self._ui.group_combo_box.setCurrentIndex(idx)
        else:
            self._ui.group_combo_box.setCurrentIndex(-1)

    def _on_save_clicked(self):
        cid = self._view_model.state.selected_channel_id
        is_active = self._ui.channel_active_check_box.isChecked()
        group_id = self._ui.group_combo_box.currentIndex() + 1

        self._view_model.save_settings(cid, is_active, group_id)
        self.settings_saved.emit()
