import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ui"))

from PySide6 import QtWidgets
from qt_material import apply_stylesheet

from model.data_models import ApplicationState
from view.window_manager import WindowManager
from view.channel_settings_window import ChannelSettingsWindow
from view.main_window import MainWindow
from view.manual_window import ManualModeWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    app_state = ApplicationState._default_state()
    main_window = MainWindow(app_state)
    channel_settings_window = ChannelSettingsWindow(app_state)
    manual_mode_window = ManualModeWindow(app_state)

    window = WindowManager(main_window, channel_settings_window, manual_mode_window)

    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True, css_file='view/styles/style.css')

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
