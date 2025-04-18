from datetime import time
from typing import Optional, Dict

from PySide6.QtCore import Signal, QTime, Qt, QObject, QEvent
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QTimeEdit, QHeaderView

from model.data_models import ApplicationState
from ui.ScheduleSettingsScreen import Ui_ScheduleSettingsWindow
from view.warning_dialog import WarningDialog
from viewmodel.schedule_settings_view_model import ScheduleSettingsViewModel


class ScheduleSettingsWindow(QMainWindow):
    schedule_closed = Signal()

    def __init__(self, state: ApplicationState):
        super().__init__()

        self._ui = Ui_ScheduleSettingsWindow()
        self._ui.setupUi(self)

        self._view_model = ScheduleSettingsViewModel(state)
        self._warning_dialog = WarningDialog(self)

        # VM → View
        self._view_model.sunset_mode_changed.connect(self._ui.sunrise_mode_check_box.setChecked)
        self._view_model.start_time_changed.connect(self._apply_time(self._ui.start_time_edit))
        self._view_model.end_time_changed.connect(self._apply_time(self._ui.end_time_edit))
        self._view_model.interval_changed.connect(self._apply_time(self._ui.watering_interval_time_edit))
        self._view_model.groups_loaded.connect(self._populate_groups_table)
        self._view_model.warning_requested.connect(self._show_warning)
        self._view_model.save_enabled.connect(self._on_save_enabled)

        # View → VM
        self._ui.sunrise_mode_check_box.toggled.connect(self._on_sunset_toggled)
        self._ui.start_time_edit.timeChanged.connect(self._view_model.set_start_time)
        self._ui.start_time_edit.installEventFilter(self)
        self._ui.end_time_edit.timeChanged.connect(self._view_model.set_end_time)
        self._ui.end_time_edit.installEventFilter(self)
        self._ui.watering_interval_time_edit.timeChanged.connect(self._view_model.set_interval)
        self._ui.watering_interval_time_edit.installEventFilter(self)

        self._ui.save_settings_btn.clicked.connect(self._on_save)
        self._ui.cancel_settings_btn.clicked.connect(self._on_cancel)

        self._view_model.sunset_mode_changed.connect(self._toggle_time_edits)

    def showEvent(self, event):
        self._view_model.load()
        super().showEvent(event)

    def _toggle_time_edits(self, sunset_on: bool):
        self._ui.start_time_edit.setEnabled(not sunset_on)
        self._ui.end_time_edit.setEnabled(not sunset_on)

    def _populate_groups_table(self, group_durations: Dict[int, time]):
        tbl = self._ui.group_duration_table
        tbl.clearContents()
        tbl.setRowCount(len(group_durations))
        for row, (gid, dur) in enumerate(sorted(group_durations.items(), key=lambda x: x[0])):
            # колонка 0: ID группы
            item = QTableWidgetItem(str(gid))
            item.setFlags(item.flags()
                          & ~Qt.ItemFlag.ItemIsEditable
                          & ~Qt.ItemFlag.ItemIsSelectable)

            tbl.setItem(row, 0, item)

            # колонка 1: Duration (QTimeEdit)
            te = QTimeEdit(self)
            te.setDisplayFormat("mm:ss")
            te.setTime(QTime(dur.hour, dur.minute, dur.second))
            te.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
            te.setStyleSheet('font-size: 20pt;')
            te.timeChanged.connect(lambda qt, group_id=gid: self._view_model.set_group_duration(group_id, qt))
            te.installEventFilter(self)
            tbl.setCellWidget(row, 1, te)

        tbl.resizeRowsToContents()
        tbl.resizeColumnsToContents()

        header = tbl.horizontalHeader()
        header.setSectionsClickable(False)
        header.setHighlightSections(False)
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        h_header = tbl.horizontalHeader().height()
        h_rows = sum(
            tbl.rowHeight(r)
            for r in range(tbl.rowCount())
        )
        tbl.setMinimumHeight(h_header + h_rows + 2)

    def _on_sunset_toggled(self, checked: bool):
        self._view_model.set_sunset_mode(checked)

    def _on_save_enabled(self, is_enabled: bool):
        if is_enabled:
            self._ui.save_settings_btn.setEnabled(True)
        else:
            self._ui.save_settings_btn.setDisabled(True)

    def _show_warning(self, text: str):
        self._warning_dialog.set_text(text)
        self._warning_dialog.show()

    def _on_save(self):
        self._view_model.save()
        self.schedule_closed.emit()

    def _on_cancel(self):
        self._view_model.close()
        self.schedule_closed.emit()

    def eventFilter(self, watched: QObject, event: QEvent):
        if isinstance(watched, QTimeEdit) and event.type() == QEvent.Type.Wheel:
            event.ignore()
            return True
        return super().eventFilter(watched, event)

    @staticmethod
    def _apply_time(widget):
        def setter(q_time: Optional[QTime]):
            if q_time is None:
                widget.clear()
            else:
                widget.setTime(q_time)

        return setter
