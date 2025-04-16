from PySide6 import QtWidgets

from view.channel_settings_window import ChannelSettingsWindow
from view.main_window import MainWindow


class WindowManager(QtWidgets.QStackedWidget):
    def __init__(self,
                 main_window: MainWindow,
                 channel_settings_window: ChannelSettingsWindow,
                 parent=None):
        super().__init__(parent)
        self.setFixedSize(800, 480)
        self.setSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)

        main_window.view_model.channel_clicked.connect(self.show_channel_settings)
        channel_settings_window.view_model.settings_saved.connect(self.show_main_window)

        self.addWidget(main_window)
        self.addWidget(channel_settings_window)

    def showEvent(self, event, /):
        self.show_main_window()
        super().showEvent(event)

    def show_main_window(self):
        self.setCurrentIndex(0)

    def show_channel_settings(self):
        self.setCurrentIndex(1)
