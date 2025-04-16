from PySide6.QtWidgets import QMainWindow

from model.data_models import ApplicationState
from ui.ChannelSettingsScreen import Ui_ChannelSettingsWindow
from viewmodel.channel_settings_view_model import ChannelSettingsViewModel


class ChannelSettingsWindow(QMainWindow):

    def __init__(self, state: ApplicationState):
        super().__init__()
        self.ui = Ui_ChannelSettingsWindow()
        self.ui.setupUi(self)
        self.view_model = ChannelSettingsViewModel(state)

        self.ui.save_settings_btn.clicked.connect(self.on_save_settings_click)
        self.view_model.settings_saved.connect(self.on_state_updated)

    def showEvent(self, event):
        self.on_state_updated(self.view_model.state)
        super().showEvent(event)

    def on_state_updated(self, state: ApplicationState):
        self.ui.channel_number_label.setText(str(state.selected_channel_id))

        selected_channel = state.channels[state.selected_channel_id]
        self.ui.channel_active_check_box.setChecked(selected_channel.is_active)
        self.ui.group_combo_box.setCurrentIndex(selected_channel.group_id - 1)

    def on_save_settings_click(self):
        self.view_model.on_save(
            int(self.ui.channel_number_label.text()),
            self.ui.channel_active_check_box.isChecked(),
            int(self.ui.group_combo_box.currentIndex()) + 1
        )
