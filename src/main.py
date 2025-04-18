import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_FILE = os.path.join(BASE_DIR, 'view', 'styles', 'style.css')

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "ui"))

from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet

from hardware.hardware_interface import DummyHardwareInterface
from model.data_models import ApplicationState
from model.irrigation import IrrigationController
from view.channel_settings_window import ChannelSettingsWindow
from view.main_window import MainWindow
from view.manual_window import ManualModeWindow
from view.schedule_settings_window import ScheduleSettingsWindow
from view.window_manager import WindowManager
from viewmodel.qt_scheduler_adapter import QtSchedulerAdapter


def main():
    app = QtWidgets.QApplication(sys.argv)

    app_state = ApplicationState.default_state()

    # if sys.platform == 'darwin':
    #     hw = DummyHardwareInterface()
    # else:
    #     raise NotImplementedError(f"Unsupported platform: {sys.platform}")

    hw = DummyHardwareInterface()

    controller = IrrigationController(hw, app_state)
    scheduler = QtSchedulerAdapter(app_state, controller)
    app.aboutToQuit.connect(scheduler.stop)

    main_window = MainWindow(app_state, scheduler)
    channel_settings_window = ChannelSettingsWindow(app_state)
    manual_mode_window = ManualModeWindow(app_state)
    schedule_settings_window = ScheduleSettingsWindow(app_state)

    window = WindowManager(main_window, channel_settings_window, manual_mode_window, schedule_settings_window)

    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True, css_file=CSS_FILE)

    window.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    window.showFullScreen()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
