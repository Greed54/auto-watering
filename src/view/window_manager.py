from PySide6 import QtWidgets

from view.channel_settings_window import ChannelSettingsWindow
from view.main_window import MainWindow
from view.manual_window import ManualModeWindow


class WindowManager(QtWidgets.QStackedWidget):
    def __init__(self,
                 main_window: MainWindow,
                 channel_settings_window: ChannelSettingsWindow,
                 manual_mode_window: ManualModeWindow,
                 parent=None):
        super().__init__(parent)
        self.setFixedSize(800, 480)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        main_window.view_model.channel_selected.connect(self._show_channel_settings)
        main_window.view_model.manual_mode_requested.connect(self._show_manual_mode_window)

        channel_settings_window.view_model.settings_saved.connect(self._show_main_window)

        manual_mode_window.view_model.auto_mode_requested.connect(self._show_main_window)

        self.addWidget(main_window)
        self.addWidget(channel_settings_window)
        self.addWidget(manual_mode_window)

    def showEvent(self, event, /):
        self._show_main_window()
        super().showEvent(event)

    def _show_main_window(self):
        self.setCurrentIndex(0)

    def _show_channel_settings(self):
        self.setCurrentIndex(1)

    def _show_manual_mode_window(self):
        self.setCurrentIndex(2)
