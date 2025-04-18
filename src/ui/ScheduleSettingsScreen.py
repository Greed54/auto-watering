# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScheduleSettingsScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QAbstractSpinBox, QApplication, QCheckBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_ScheduleSettingsWindow(object):
    def setupUi(self, ScheduleSettingsWindow):
        if not ScheduleSettingsWindow.objectName():
            ScheduleSettingsWindow.setObjectName(u"ScheduleSettingsWindow")
        ScheduleSettingsWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ScheduleSettingsWindow.sizePolicy().hasHeightForWidth())
        ScheduleSettingsWindow.setSizePolicy(sizePolicy)
        ScheduleSettingsWindow.setMinimumSize(QSize(800, 480))
        ScheduleSettingsWindow.setMaximumSize(QSize(800, 480))
        ScheduleSettingsWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(ScheduleSettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setObjectName(u"headerLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer)

        self.header_label = QLabel(self.centralwidget)
        self.header_label.setObjectName(u"header_label")
        self.header_label.setMaximumSize(QSize(16777215, 70))
        self.header_label.setStyleSheet(u"font-size: 48pt;")

        self.headerLayout.addWidget(self.header_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.headerLayout)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Shadow.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 776, 344))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sunriseLayout = QHBoxLayout()
        self.sunriseLayout.setObjectName(u"sunriseLayout")
        self.sunrize_sunset_label = QLabel(self.scrollAreaWidgetContents)
        self.sunrize_sunset_label.setObjectName(u"sunrize_sunset_label")
        self.sunrize_sunset_label.setStyleSheet(u"font-size: 25pt;")

        self.sunriseLayout.addWidget(self.sunrize_sunset_label)

        self.sunrise_mode_check_box = QCheckBox(self.scrollAreaWidgetContents)
        self.sunrise_mode_check_box.setObjectName(u"sunrise_mode_check_box")
        self.sunrise_mode_check_box.setMinimumSize(QSize(50, 50))
        self.sunrise_mode_check_box.setStyleSheet(u"QCheckBox::indicator { width:50px; height: 50px;}")
        self.sunrise_mode_check_box.setTristate(False)

        self.sunriseLayout.addWidget(self.sunrise_mode_check_box)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.sunriseLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.sunriseLayout)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.startTimeLayout = QHBoxLayout()
        self.startTimeLayout.setObjectName(u"startTimeLayout")
        self.sunrize_sunset_label_2 = QLabel(self.scrollAreaWidgetContents)
        self.sunrize_sunset_label_2.setObjectName(u"sunrize_sunset_label_2")
        self.sunrize_sunset_label_2.setStyleSheet(u"font-size: 25pt;")

        self.startTimeLayout.addWidget(self.sunrize_sunset_label_2)

        self.start_time_edit = QTimeEdit(self.scrollAreaWidgetContents)
        self.start_time_edit.setObjectName(u"start_time_edit")
        self.start_time_edit.setMinimumSize(QSize(100, 0))
        self.start_time_edit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.start_time_edit.setStyleSheet(u"font-size: 20pt;")
        self.start_time_edit.setWrapping(False)
        self.start_time_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.start_time_edit.setProperty(u"showGroupSeparator", False)
        self.start_time_edit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.start_time_edit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.startTimeLayout.addWidget(self.start_time_edit)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.startTimeLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.startTimeLayout)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.endTimeLayout = QHBoxLayout()
        self.endTimeLayout.setObjectName(u"endTimeLayout")
        self.sunrize_sunset_label_3 = QLabel(self.scrollAreaWidgetContents)
        self.sunrize_sunset_label_3.setObjectName(u"sunrize_sunset_label_3")
        self.sunrize_sunset_label_3.setStyleSheet(u"font-size: 25pt;")

        self.endTimeLayout.addWidget(self.sunrize_sunset_label_3)

        self.end_time_edit = QTimeEdit(self.scrollAreaWidgetContents)
        self.end_time_edit.setObjectName(u"end_time_edit")
        self.end_time_edit.setMinimumSize(QSize(100, 0))
        self.end_time_edit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.end_time_edit.setStyleSheet(u"font-size: 20pt;")
        self.end_time_edit.setWrapping(False)
        self.end_time_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.end_time_edit.setProperty(u"showGroupSeparator", False)
        self.end_time_edit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.end_time_edit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.endTimeLayout.addWidget(self.end_time_edit)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.endTimeLayout.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.endTimeLayout)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_4)

        self.wateringIntervalLayout = QHBoxLayout()
        self.wateringIntervalLayout.setObjectName(u"wateringIntervalLayout")
        self.sunrize_sunset_label_5 = QLabel(self.scrollAreaWidgetContents)
        self.sunrize_sunset_label_5.setObjectName(u"sunrize_sunset_label_5")
        self.sunrize_sunset_label_5.setStyleSheet(u"font-size: 25pt;")

        self.wateringIntervalLayout.addWidget(self.sunrize_sunset_label_5)

        self.watering_interval_time_edit = QTimeEdit(self.scrollAreaWidgetContents)
        self.watering_interval_time_edit.setObjectName(u"watering_interval_time_edit")
        self.watering_interval_time_edit.setMinimumSize(QSize(100, 0))
        self.watering_interval_time_edit.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.watering_interval_time_edit.setStyleSheet(u"font-size: 20pt;")
        self.watering_interval_time_edit.setWrapping(False)
        self.watering_interval_time_edit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.PlusMinus)
        self.watering_interval_time_edit.setProperty(u"showGroupSeparator", False)
        self.watering_interval_time_edit.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.watering_interval_time_edit.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.wateringIntervalLayout.addWidget(self.watering_interval_time_edit)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.wateringIntervalLayout.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.wateringIntervalLayout)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.group_duration_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.group_duration_table.columnCount() < 2):
            self.group_duration_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.group_duration_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.group_duration_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.group_duration_table.setObjectName(u"group_duration_table")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.group_duration_table.sizePolicy().hasHeightForWidth())
        self.group_duration_table.setSizePolicy(sizePolicy2)
        self.group_duration_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.group_duration_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.group_duration_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.group_duration_table.setAutoScroll(False)
        self.group_duration_table.setTabKeyNavigation(False)
        self.group_duration_table.setProperty(u"showDropIndicator", False)
        self.group_duration_table.setDragDropOverwriteMode(False)
        self.group_duration_table.setCornerButtonEnabled(False)
        self.group_duration_table.setColumnCount(2)
        self.group_duration_table.horizontalHeader().setVisible(True)
        self.group_duration_table.horizontalHeader().setCascadingSectionResizes(False)
        self.group_duration_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.group_duration_table.horizontalHeader().setStretchLastSection(True)
        self.group_duration_table.verticalHeader().setVisible(False)
        self.group_duration_table.verticalHeader().setMinimumSectionSize(50)
        self.group_duration_table.verticalHeader().setDefaultSectionSize(50)

        self.verticalLayout_2.addWidget(self.group_duration_table)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.footerLayout = QHBoxLayout()
        self.footerLayout.setObjectName(u"footerLayout")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer_12)

        self.cancel_settings_btn = QPushButton(self.centralwidget)
        self.cancel_settings_btn.setObjectName(u"cancel_settings_btn")
        self.cancel_settings_btn.setMinimumSize(QSize(200, 70))
        font = QFont()
        font.setPointSize(36)
        self.cancel_settings_btn.setFont(font)
        self.cancel_settings_btn.setStyleSheet(u"font-size: 36pt;")

        self.footerLayout.addWidget(self.cancel_settings_btn)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer_4)

        self.save_settings_btn = QPushButton(self.centralwidget)
        self.save_settings_btn.setObjectName(u"save_settings_btn")
        self.save_settings_btn.setMinimumSize(QSize(200, 70))
        self.save_settings_btn.setFont(font)
        self.save_settings_btn.setStyleSheet(u"font-size: 36pt;")

        self.footerLayout.addWidget(self.save_settings_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.footerLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.footerLayout)

        ScheduleSettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ScheduleSettingsWindow)

        QMetaObject.connectSlotsByName(ScheduleSettingsWindow)
    # setupUi

    def retranslateUi(self, ScheduleSettingsWindow):
        ScheduleSettingsWindow.setWindowTitle(QCoreApplication.translate("ScheduleSettingsWindow", u"ScheduleSettings", None))
        self.header_label.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"Schedule Settings", None))
        self.sunrize_sunset_label.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"Sunrise/sunset mode", None))
        self.sunrise_mode_check_box.setText("")
        self.sunrize_sunset_label_2.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"Start time (hh:mm):", None))
        self.sunrize_sunset_label_3.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"End time (hh:mm):", None))
        self.sunrize_sunset_label_5.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"Watering interval (hh:mm):", None))
        self.watering_interval_time_edit.setDisplayFormat(QCoreApplication.translate("ScheduleSettingsWindow", u"hh:mm", None))
        ___qtablewidgetitem = self.group_duration_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"Group", None));
        ___qtablewidgetitem1 = self.group_duration_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"Watering Duration (mm:ss)", None));
        self.group_duration_table.setProperty(u"class", QCoreApplication.translate("ScheduleSettingsWindow", u"groupDurationTable", None))
        self.cancel_settings_btn.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"CANCEL", None))
        self.cancel_settings_btn.setProperty(u"class", QCoreApplication.translate("ScheduleSettingsWindow", u"danger", None))
        self.save_settings_btn.setText(QCoreApplication.translate("ScheduleSettingsWindow", u"SAVE", None))
    # retranslateUi

