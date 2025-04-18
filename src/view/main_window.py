from typing import Dict

from PySide6 import QtCore
from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QMainWindow

from model.data_models import ApplicationState
from ui.MainScreen import Ui_MainWindow
from view.styles.dynamic_styles import (
    ENABLED_CHANNEL_STYLE,
    DISABLED_CHANNEL_STYLE,
    INACTIVE_CHANNEL_STYLE,
    ENABLED_PUMP_TILE_STYLE,
    DISABLED_PUMP_TILE_STYLE,
    AUTO_WATERING_ENABLED_BUTTON_STYLE,
    AUTO_WATERING_DISABLED_BUTTON_STYLE,
)
from view.warning_dialog import WarningDialog
from viewmodel.main_view_model import MainViewModel
from viewmodel.qt_scheduler_adapter import QtSchedulerAdapter


class MainWindow(QMainWindow):
    channel_selected = Signal()
    schedule_settings_requested = Signal()
    manual_mode_requested = Signal()

    def __init__(self, state: ApplicationState, auto_watering_scheduler: QtSchedulerAdapter):
        super().__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._view_model = MainViewModel(state, auto_watering_scheduler)
        self._warning_dialog = WarningDialog(self)

        self._view_model.time_updated.connect(self._ui.date_time_label.setText)
        self._view_model.state_updated.connect(self._on_state_updated)
        self._view_model.warning_requested.connect(self._show_warning)

        self._ui.toggle_watering_btn.clicked.connect(self._view_model.toggle_auto_watering)
        self._ui.manual_mode_btn.clicked.connect(self._on_manual_mode_clicked)
        self._ui.schedule_btn.clicked.connect(self._on_schedule_settings_clicked)

        self._channel_tiles: Dict[QWidget, int] = {}
        for cid, channel in self._view_model.state.channels.items():
            tile = getattr(self._ui, f"channel_tile_{cid}", None)
            if tile:
                tile.installEventFilter(self)
                self._channel_tiles[tile] = cid

    def showEvent(self, event):
        self._view_model.refresh_time()
        self._on_state_updated(self._view_model.state)
        super().showEvent(event)

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.Type.MouseButtonPress and source in self._channel_tiles:
            cid = self._channel_tiles[source]
            self._on_channel_selected(cid)
            return True
        return super().eventFilter(source, event)

    def _on_channel_selected(self, channel_id: int):
        self._view_model.select_channel(channel_id)
        self.channel_selected.emit()

    def _on_manual_mode_clicked(self):
        self._view_model.toggle_manual_mode(self.manual_mode_requested)

    def _on_schedule_settings_clicked(self):
        self.schedule_settings_requested.emit()

    def _on_state_updated(self, state: ApplicationState):
        self._update_auto_watering_button(state.schedule.is_auto_watering_enabled)
        self._update_pump_tile(state.pump.is_enabled)
        self._update_channels(state)

    def _update_auto_watering_button(self, enabled: bool):
        btn = self._ui.toggle_watering_btn
        style = AUTO_WATERING_ENABLED_BUTTON_STYLE if enabled else AUTO_WATERING_DISABLED_BUTTON_STYLE
        icon = QIcon(":/icons/pause_icon.svg") if enabled else QIcon(":/icons/play_icon.svg")
        text = "STOP" if enabled else "START"

        btn.setStyleSheet(style)
        btn.setIcon(icon)
        btn.setText(text)

    def _update_pump_tile(self, enabled: bool):
        style = ENABLED_PUMP_TILE_STYLE if enabled else DISABLED_PUMP_TILE_STYLE
        self._ui.pump_channel_tile.setStyleSheet(style)

    def _update_channels(self, state: ApplicationState):
        for cid, channel in state.channels.items():
            tile = getattr(self._ui, f"channel_tile_{cid}")
            name_label = getattr(self._ui, f"name_label_{cid}")
            group_label = getattr(self._ui, f"group_label_number_{cid}")
            state_label = getattr(self._ui, f"state_label_{cid}")

            name_label.setText(channel.name)
            group_label.setText(str(channel.group_id))
            state_label.setText(
                channel.next_watering_time.time().strftime("%H:%M")
                if channel.next_watering_time
                else "N/A"
            )

            if not channel.is_active:
                style = INACTIVE_CHANNEL_STYLE
            else:
                style = (
                    ENABLED_CHANNEL_STYLE
                    if channel.is_enabled
                    else DISABLED_CHANNEL_STYLE
                )

            tile.setStyleSheet(style.format(channel_id=cid))

    def _show_warning(self, text: str):
        self._warning_dialog.set_text(text)
        self._warning_dialog.show()
