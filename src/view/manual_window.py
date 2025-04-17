from typing import cast

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QLabel

from model.data_models import ApplicationState
from ui.ManualScreen import Ui_ManualWindow
from view.styles.dynamic_styles import ENABLED_PUMP_STYLE, DISABLED_PUMP_STYLE, ENABLED_CHANNEL_STYLE, DISABLED_CHANNEL_STYLE
from viewmodel.manual_mode_view_model import ManualModeViewModel


class ManualModeWindow(QMainWindow):
    def __init__(self, state: ApplicationState):
        super().__init__()
        self.ui = Ui_ManualWindow()
        self.ui.setupUi(self)

        self.view_model = ManualModeViewModel(state)

        self.view_model.time_updated.connect(self.ui.date_time_label.setText)
        self.view_model.state_updated.connect(self.on_state_updated)

        self.ui.auto_mode_btn.clicked.connect(self.view_model.on_auto_mode_clicked)

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

        self.ui.pump_channel_tile.installEventFilter(self)

    def showEvent(self, event):
        self.view_model.update_time()
        self.on_state_updated(self.view_model.state)
        super().showEvent(event)

    def on_state_updated(self, state: ApplicationState):
        # update pump ui
        if state.pump.is_enabled:
            self.ui.pump_channel_tile.setStyleSheet(ENABLED_PUMP_STYLE)
        else:
            self.ui.pump_channel_tile.setStyleSheet(DISABLED_PUMP_STYLE)

        # update channel tiles ui
        for channel in state.channels.values():
            tile_name = f"channel_tile_{channel.id}"
            name_label_name = f"name_label_{channel.id}"

            tile_widget = cast(QWidget, getattr(self.ui, tile_name, None))
            name_label = cast(QLabel, getattr(self.ui, name_label_name, None))

            if name_label is not None:
                name_label.setText(channel.name)

            if tile_widget is not None:
                if channel.is_enabled:
                    tile_widget.setStyleSheet(ENABLED_CHANNEL_STYLE.format(channel_id=channel.id))
                else:
                    tile_widget.setStyleSheet(DISABLED_CHANNEL_STYLE.format(channel_id=channel.id))

    def eventFilter(self, source, event):
        if source in self.channel_tiles.keys() and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.view_model.on_channel_tale_click(self.channel_tiles[source])
            return True
        if source == self.ui.pump_channel_tile and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            self.view_model.on_pump_tale_click()
            return True

        return super().eventFilter(source, event)
