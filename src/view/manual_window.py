from typing import Dict

from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow, QWidget

from model.data_models import ApplicationState
from ui.ManualScreen import Ui_ManualWindow
from view.styles.dynamic_styles import (
    ENABLED_PUMP_TILE_STYLE,
    DISABLED_PUMP_TILE_STYLE,
    ENABLED_CHANNEL_STYLE,
    DISABLED_CHANNEL_STYLE,
)
from viewmodel.manual_mode_view_model import ManualModeViewModel


class ManualModeWindow(QMainWindow):
    auto_mode_requested = Signal()

    def __init__(self, state: ApplicationState):
        super().__init__()
        self._ui = Ui_ManualWindow()
        self._ui.setupUi(self)

        self._view_model = ManualModeViewModel(state)

        self._view_model.time_updated.connect(self._ui.date_time_label.setText)
        self._view_model.state_updated.connect(self._on_state_updated)

        self._ui.auto_mode_btn.clicked.connect(self._on_auto_mode_clicked)

        self._channel_tiles: Dict[QWidget, int] = {}
        for cid in state.channels:
            tile = getattr(self._ui, f"channel_tile_{cid}", None)
            if tile is not None:
                tile.installEventFilter(self)
                self._channel_tiles[tile] = cid

        self._pump_tile = self._ui.pump_channel_tile
        self._pump_tile.installEventFilter(self)

    def showEvent(self, event):
        self._view_model.refresh_time()
        self._on_state_updated(self._view_model.state)
        super().showEvent(event)

    def _on_state_updated(self, state: ApplicationState):
        self._update_pump(state.pump.is_enabled)
        self._update_channels(state)

    def _update_pump(self, enabled: bool):
        style = ENABLED_PUMP_TILE_STYLE if enabled else DISABLED_PUMP_TILE_STYLE
        self._ui.pump_channel_tile.setStyleSheet(style)

    def _update_channels(self, state: ApplicationState):
        for cid, channel in state.channels.items():
            tile = getattr(self._ui, f"channel_tile_{cid}", None)
            name_label = getattr(self._ui, f"name_label_{cid}", None)
            if name_label:
                name_label.setText(channel.name)
            if tile:
                style = ENABLED_CHANNEL_STYLE if channel.is_enabled else DISABLED_CHANNEL_STYLE
                tile.setStyleSheet(style.format(channel_id=cid))

    def _on_auto_mode_clicked(self):
        self._view_model.enable_auto_mode()
        self.auto_mode_requested.emit()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress:
            if source in self._channel_tiles:
                cid = self._channel_tiles[source]
                self._view_model.toggle_channel(cid)
                return True

            if source is self._pump_tile:
                self._view_model.toggle_pump()
                return True

        return super().eventFilter(source, event)
