from typing import cast

from PySide6 import QtCore
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QLabel, QMainWindow

from model.data_models import ApplicationState
from ui.MainScreen import Ui_MainWindow
from view.styles.dynamic_styles import ENABLED_CHANNEL_STYLE, DISABLED_CHANNEL_STYLE, INACTIVE_CHANNEL_STYLE, ENABLED_PUMP_STYLE, \
    DISABLED_PUMP_STYLE, AUTO_WATERING_ENABLED_STYLE, AUTO_WATERING_DISABLED_STYLE
from view.warning_dialog import WarningDialog
from viewmodel.main_view_model import MainViewModel


class MainWindow(QMainWindow):
    def __init__(self, state: ApplicationState):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.warning_dialog = WarningDialog(self)

        self.view_model = MainViewModel(state)

        self.view_model.time_updated.connect(self.ui.date_time_label.setText)
        self.view_model.state_updated.connect(self.on_state_updated)
        self.view_model.warning_shown.connect(self.show_warning)

        self.ui.toggle_watering_btn.clicked.connect(self.view_model.toggle_auto_watering)
        self.ui.manual_mode_btn.clicked.connect(self.view_model.on_manual_mode_clicked)

        self.channel_tiles = {
            self.ui.channel_tile_1: 1,
            self.ui.channel_tile_2: 2,
            self.ui.channel_tile_3: 3,
            self.ui.channel_tile_4: 4,
            self.ui.channel_tile_5: 5,
            self.ui.channel_tile_6: 6,
            self.ui.channel_tile_7: 7
        }
        for channel_tile in self.channel_tiles.keys():
            channel_tile.installEventFilter(self)

    def showEvent(self, event):
        self.view_model.update_time()
        self.on_state_updated(self.view_model.state)
        super().showEvent(event)

    def on_state_updated(self, state: ApplicationState):

        if state.is_auto_watering_enabled:
            self.ui.toggle_watering_btn.setStyleSheet(AUTO_WATERING_ENABLED_STYLE)
            self.ui.toggle_watering_btn.setIcon(QIcon(":/icons/pause_icon.svg"))
            self.ui.toggle_watering_btn.setText("STOP")
        else:
            self.ui.toggle_watering_btn.setStyleSheet(AUTO_WATERING_DISABLED_STYLE)
            self.ui.toggle_watering_btn.setIcon(QIcon(":/icons/play_icon.svg"))
            self.ui.toggle_watering_btn.setText("START")

        # update pump ui
        if state.pump.is_enabled:
            self.ui.pump_channel_tile.setStyleSheet(ENABLED_PUMP_STYLE)
        else:
            self.ui.pump_channel_tile.setStyleSheet(DISABLED_PUMP_STYLE)

        # update channel tiles ui
        for channel in state.channels.values():
            tile_name = f"channel_tile_{channel.id}"
            name_label_name = f"name_label_{channel.id}"
            group_label_name = f"group_label_number_{channel.id}"
            state_label_name = f"state_label_{channel.id}"

            tile_widget = cast(QWidget, getattr(self.ui, tile_name, None))
            name_label = cast(QLabel, getattr(self.ui, name_label_name, None))
            group_label = cast(QLabel, getattr(self.ui, group_label_name, None))
            state_label = cast(QLabel, getattr(self.ui, state_label_name, None))

            if name_label is not None:
                name_label.setText(channel.name)

            if group_label is not None:
                group_label.setText(str(channel.group_id))

            if state_label is not None:
                if channel.last_activation is not None:
                    state_label.setText(channel.last_activation.time().strftime('%H:%M'))
                else:
                    state_label.setText("N/A")

            if tile_widget is not None:
                if channel.is_active:
                    if channel.is_enabled:
                        tile_widget.setStyleSheet(ENABLED_CHANNEL_STYLE.format(channel_id=channel.id))
                    else:
                        tile_widget.setStyleSheet(DISABLED_CHANNEL_STYLE.format(channel_id=channel.id))
                else:
                    tile_widget.setStyleSheet(INACTIVE_CHANNEL_STYLE.format(channel_id=channel.id))

    def show_warning(self, text: str):
        self.warning_dialog.set_text(text)
        self.warning_dialog.show()

    def eventFilter(self, source, event):
        if source in self.channel_tiles.keys() and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.view_model.on_channel_tale_click(self.channel_tiles[source])
            return True
        return super().eventFilter(source, event)
