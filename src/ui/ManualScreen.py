# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ManualScreen.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import IconsResource_rc

class Ui_ManualWindow(object):
    def setupUi(self, ManualWindow):
        if not ManualWindow.objectName():
            ManualWindow.setObjectName(u"ManualWindow")
        ManualWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ManualWindow.sizePolicy().hasHeightForWidth())
        ManualWindow.setSizePolicy(sizePolicy)
        ManualWindow.setMinimumSize(QSize(800, 480))
        ManualWindow.setMaximumSize(QSize(800, 480))
        ManualWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(ManualWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.topBar = QHBoxLayout()
        self.topBar.setObjectName(u"topBar")
        self.topLeftLayout = QHBoxLayout()
        self.topLeftLayout.setSpacing(10)
        self.topLeftLayout.setObjectName(u"topLeftLayout")
        self.date_time_label = QLabel(self.centralwidget)
        self.date_time_label.setObjectName(u"date_time_label")
        self.date_time_label.setMinimumSize(QSize(250, 50))
        self.date_time_label.setStyleSheet(u"font-size: 30pt;")
        self.date_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topLeftLayout.addWidget(self.date_time_label)

        self.wifi_status_icon = QLabel(self.centralwidget)
        self.wifi_status_icon.setObjectName(u"wifi_status_icon")
        self.wifi_status_icon.setMinimumSize(QSize(0, 50))
        self.wifi_status_icon.setPixmap(QPixmap(u":/icons/icons8-wifi-off-48.png"))
        self.wifi_status_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topLeftLayout.addWidget(self.wifi_status_icon)


        self.topBar.addLayout(self.topLeftLayout)

        self.topRightLayout = QHBoxLayout()
        self.topRightLayout.setSpacing(10)
        self.topRightLayout.setObjectName(u"topRightLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 50))
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.topRightLayout.addWidget(self.label)

        self.auto_mode_btn = QPushButton(self.centralwidget)
        self.auto_mode_btn.setObjectName(u"auto_mode_btn")
        self.auto_mode_btn.setMinimumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/icons/icons8-auto-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.auto_mode_btn.setIcon(icon)
        self.auto_mode_btn.setIconSize(QSize(48, 48))

        self.topRightLayout.addWidget(self.auto_mode_btn)

        self.schedule_btn = QPushButton(self.centralwidget)
        self.schedule_btn.setObjectName(u"schedule_btn")
        self.schedule_btn.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-time-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.schedule_btn.setIcon(icon1)
        self.schedule_btn.setIconSize(QSize(48, 48))

        self.topRightLayout.addWidget(self.schedule_btn)

        self.settings_btn = QPushButton(self.centralwidget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-settings-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon2)
        self.settings_btn.setIconSize(QSize(49, 48))

        self.topRightLayout.addWidget(self.settings_btn)


        self.topBar.addLayout(self.topRightLayout)


        self.mainLayout.addLayout(self.topBar)

        self.channelsGrid = QGridLayout()
        self.channelsGrid.setSpacing(20)
        self.channelsGrid.setObjectName(u"channelsGrid")
        self.channelsGrid.setContentsMargins(-1, 10, -1, -1)
        self.channel_tile_1 = QWidget(self.centralwidget)
        self.channel_tile_1.setObjectName(u"channel_tile_1")
        self.channel_tile_1.setMinimumSize(QSize(180, 180))
        self.verticalLayout_1 = QVBoxLayout(self.channel_tile_1)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.name_label_1 = QLabel(self.channel_tile_1)
        self.name_label_1.setObjectName(u"name_label_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_label_1.sizePolicy().hasHeightForWidth())
        self.name_label_1.setSizePolicy(sizePolicy1)

        self.verticalLayout_1.addWidget(self.name_label_1)


        self.channelsGrid.addWidget(self.channel_tile_1, 0, 0, 1, 1)

        self.channel_tile_2 = QWidget(self.centralwidget)
        self.channel_tile_2.setObjectName(u"channel_tile_2")
        self.channel_tile_2.setMinimumSize(QSize(180, 180))
        self.verticalLayout_2 = QVBoxLayout(self.channel_tile_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.name_label_2 = QLabel(self.channel_tile_2)
        self.name_label_2.setObjectName(u"name_label_2")
        sizePolicy1.setHeightForWidth(self.name_label_2.sizePolicy().hasHeightForWidth())
        self.name_label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.name_label_2)


        self.channelsGrid.addWidget(self.channel_tile_2, 1, 0, 1, 1)

        self.channel_tile_3 = QWidget(self.centralwidget)
        self.channel_tile_3.setObjectName(u"channel_tile_3")
        self.channel_tile_3.setMinimumSize(QSize(180, 180))
        self.verticalLayout_3 = QVBoxLayout(self.channel_tile_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.name_label_3 = QLabel(self.channel_tile_3)
        self.name_label_3.setObjectName(u"name_label_3")
        sizePolicy1.setHeightForWidth(self.name_label_3.sizePolicy().hasHeightForWidth())
        self.name_label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.name_label_3)


        self.channelsGrid.addWidget(self.channel_tile_3, 0, 1, 1, 1)

        self.channel_tile_4 = QWidget(self.centralwidget)
        self.channel_tile_4.setObjectName(u"channel_tile_4")
        self.channel_tile_4.setMinimumSize(QSize(180, 180))
        self.verticalLayout_4 = QVBoxLayout(self.channel_tile_4)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.name_label_4 = QLabel(self.channel_tile_4)
        self.name_label_4.setObjectName(u"name_label_4")
        sizePolicy1.setHeightForWidth(self.name_label_4.sizePolicy().hasHeightForWidth())
        self.name_label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.name_label_4)


        self.channelsGrid.addWidget(self.channel_tile_4, 1, 1, 1, 1)

        self.channel_tile_5 = QWidget(self.centralwidget)
        self.channel_tile_5.setObjectName(u"channel_tile_5")
        self.channel_tile_5.setMinimumSize(QSize(180, 180))
        self.verticalLayout_5 = QVBoxLayout(self.channel_tile_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.name_label_5 = QLabel(self.channel_tile_5)
        self.name_label_5.setObjectName(u"name_label_5")
        sizePolicy1.setHeightForWidth(self.name_label_5.sizePolicy().hasHeightForWidth())
        self.name_label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.name_label_5)


        self.channelsGrid.addWidget(self.channel_tile_5, 0, 2, 1, 1)

        self.channel_tile_6 = QWidget(self.centralwidget)
        self.channel_tile_6.setObjectName(u"channel_tile_6")
        self.channel_tile_6.setMinimumSize(QSize(180, 170))
        self.verticalLayout_6 = QVBoxLayout(self.channel_tile_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.name_label_6 = QLabel(self.channel_tile_6)
        self.name_label_6.setObjectName(u"name_label_6")
        sizePolicy1.setHeightForWidth(self.name_label_6.sizePolicy().hasHeightForWidth())
        self.name_label_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.name_label_6)


        self.channelsGrid.addWidget(self.channel_tile_6, 1, 2, 1, 1)

        self.channel_tile_7 = QWidget(self.centralwidget)
        self.channel_tile_7.setObjectName(u"channel_tile_7")
        self.channel_tile_7.setMinimumSize(QSize(180, 180))
        self.verticalLayout_7 = QVBoxLayout(self.channel_tile_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.name_label_7 = QLabel(self.channel_tile_7)
        self.name_label_7.setObjectName(u"name_label_7")
        sizePolicy1.setHeightForWidth(self.name_label_7.sizePolicy().hasHeightForWidth())
        self.name_label_7.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.name_label_7)


        self.channelsGrid.addWidget(self.channel_tile_7, 0, 3, 1, 1)

        self.pump_channel_tile = QWidget(self.centralwidget)
        self.pump_channel_tile.setObjectName(u"pump_channel_tile")
        self.pump_channel_tile.setMinimumSize(QSize(170, 170))
        self.verticalLayout_8 = QVBoxLayout(self.pump_channel_tile)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pump_name_label = QLabel(self.pump_channel_tile)
        self.pump_name_label.setObjectName(u"pump_name_label")
        sizePolicy1.setHeightForWidth(self.pump_name_label.sizePolicy().hasHeightForWidth())
        self.pump_name_label.setSizePolicy(sizePolicy1)

        self.verticalLayout_8.addWidget(self.pump_name_label)


        self.channelsGrid.addWidget(self.pump_channel_tile, 1, 3, 1, 1)


        self.mainLayout.addLayout(self.channelsGrid)


        self.horizontalLayout.addLayout(self.mainLayout)

        ManualWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManualWindow)

        QMetaObject.connectSlotsByName(ManualWindow)
    # setupUi

    def retranslateUi(self, ManualWindow):
        ManualWindow.setWindowTitle(QCoreApplication.translate("ManualWindow", u"ManualWindow", None))
        self.date_time_label.setText(QCoreApplication.translate("ManualWindow", u"12:30 | 12.04.2025", None))
        self.wifi_status_icon.setText("")
        self.label.setText(QCoreApplication.translate("ManualWindow", u"MANUAL", None))
        self.label.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"manualModeLabel", None))
        self.auto_mode_btn.setText("")
        self.auto_mode_btn.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"topBarButton", None))
        self.schedule_btn.setText("")
        self.schedule_btn.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"topBarButton", None))
        self.settings_btn.setText("")
        self.settings_btn.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"topBarButton", None))
        self.name_label_1.setText(QCoreApplication.translate("ManualWindow", u"Channel 1", None))
        self.name_label_1.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.name_label_2.setText(QCoreApplication.translate("ManualWindow", u"Channel 2", None))
        self.name_label_2.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.name_label_3.setText(QCoreApplication.translate("ManualWindow", u"Channel 3", None))
        self.name_label_3.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.name_label_4.setText(QCoreApplication.translate("ManualWindow", u"Channel 4", None))
        self.name_label_4.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.name_label_5.setText(QCoreApplication.translate("ManualWindow", u"Channel 5", None))
        self.name_label_5.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.name_label_6.setText(QCoreApplication.translate("ManualWindow", u"Channel 6", None))
        self.name_label_6.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.name_label_7.setText(QCoreApplication.translate("ManualWindow", u"Channel 7", None))
        self.name_label_7.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
        self.pump_name_label.setText(QCoreApplication.translate("ManualWindow", u"Pump", None))
        self.pump_name_label.setProperty(u"class", QCoreApplication.translate("ManualWindow", u"channelTileLabel", None))
    # retranslateUi

