# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainScreen.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import IconsResource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setMaximumSize(QSize(800, 480))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
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
        self.topRightLayout.setContentsMargins(-1, 0, -1, -1)
        self.toggle_watering_btn = QPushButton(self.centralwidget)
        self.toggle_watering_btn.setObjectName(u"toggle_watering_btn")
        self.toggle_watering_btn.setMinimumSize(QSize(200, 50))
        icon = QIcon()
        icon.addFile(u":/icons/play_icon.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toggle_watering_btn.setIcon(icon)
        self.toggle_watering_btn.setIconSize(QSize(48, 48))
        self.toggle_watering_btn.setAutoDefault(False)
        self.toggle_watering_btn.setFlat(False)

        self.topRightLayout.addWidget(self.toggle_watering_btn)

        self.manual_mode_btn = QPushButton(self.centralwidget)
        self.manual_mode_btn.setObjectName(u"manual_mode_btn")
        self.manual_mode_btn.setMinimumSize(QSize(50, 50))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-manual-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.manual_mode_btn.setIcon(icon1)
        self.manual_mode_btn.setIconSize(QSize(48, 48))

        self.topRightLayout.addWidget(self.manual_mode_btn)

        self.schedule_btn = QPushButton(self.centralwidget)
        self.schedule_btn.setObjectName(u"schedule_btn")
        self.schedule_btn.setMinimumSize(QSize(50, 50))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons8-time-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.schedule_btn.setIcon(icon2)
        self.schedule_btn.setIconSize(QSize(48, 48))

        self.topRightLayout.addWidget(self.schedule_btn)

        self.settings_btn = QPushButton(self.centralwidget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setMinimumSize(QSize(50, 50))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons8-settings-48.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_btn.setIcon(icon3)
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

        self.group_layout_1 = QHBoxLayout()
        self.group_layout_1.setObjectName(u"group_layout_1")
        self.spacerLeftGroup_1 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_1.addItem(self.spacerLeftGroup_1)

        self.group_label_title_1 = QLabel(self.channel_tile_1)
        self.group_label_title_1.setObjectName(u"group_label_title_1")

        self.group_layout_1.addWidget(self.group_label_title_1)

        self.group_label_number_1 = QLabel(self.channel_tile_1)
        self.group_label_number_1.setObjectName(u"group_label_number_1")

        self.group_layout_1.addWidget(self.group_label_number_1)

        self.spacerRightGroup_1 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_1.addItem(self.spacerRightGroup_1)


        self.verticalLayout_1.addLayout(self.group_layout_1)

        self.state_label_1 = QLabel(self.channel_tile_1)
        self.state_label_1.setObjectName(u"state_label_1")
        sizePolicy1.setHeightForWidth(self.state_label_1.sizePolicy().hasHeightForWidth())
        self.state_label_1.setSizePolicy(sizePolicy1)

        self.verticalLayout_1.addWidget(self.state_label_1)


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

        self.group_layout_2 = QHBoxLayout()
        self.group_layout_2.setObjectName(u"group_layout_2")
        self.spacerLeftGroup_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_2.addItem(self.spacerLeftGroup_2)

        self.group_label_title_2 = QLabel(self.channel_tile_2)
        self.group_label_title_2.setObjectName(u"group_label_title_2")

        self.group_layout_2.addWidget(self.group_label_title_2)

        self.group_label_number_2 = QLabel(self.channel_tile_2)
        self.group_label_number_2.setObjectName(u"group_label_number_2")

        self.group_layout_2.addWidget(self.group_label_number_2)

        self.spacerRightGroup_2 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_2.addItem(self.spacerRightGroup_2)


        self.verticalLayout_2.addLayout(self.group_layout_2)

        self.state_label_2 = QLabel(self.channel_tile_2)
        self.state_label_2.setObjectName(u"state_label_2")
        sizePolicy1.setHeightForWidth(self.state_label_2.sizePolicy().hasHeightForWidth())
        self.state_label_2.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.state_label_2)


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

        self.group_layout_3 = QHBoxLayout()
        self.group_layout_3.setObjectName(u"group_layout_3")
        self.spacerLeftGroup_3 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_3.addItem(self.spacerLeftGroup_3)

        self.group_label_title_3 = QLabel(self.channel_tile_3)
        self.group_label_title_3.setObjectName(u"group_label_title_3")

        self.group_layout_3.addWidget(self.group_label_title_3)

        self.group_label_number_3 = QLabel(self.channel_tile_3)
        self.group_label_number_3.setObjectName(u"group_label_number_3")

        self.group_layout_3.addWidget(self.group_label_number_3)

        self.spacerRightGroup_3 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_3.addItem(self.spacerRightGroup_3)


        self.verticalLayout_3.addLayout(self.group_layout_3)

        self.state_label_3 = QLabel(self.channel_tile_3)
        self.state_label_3.setObjectName(u"state_label_3")
        sizePolicy1.setHeightForWidth(self.state_label_3.sizePolicy().hasHeightForWidth())
        self.state_label_3.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.state_label_3)


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

        self.group_layout_4 = QHBoxLayout()
        self.group_layout_4.setObjectName(u"group_layout_4")
        self.spacerLeftGroup_4 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_4.addItem(self.spacerLeftGroup_4)

        self.group_label_title_4 = QLabel(self.channel_tile_4)
        self.group_label_title_4.setObjectName(u"group_label_title_4")

        self.group_layout_4.addWidget(self.group_label_title_4)

        self.group_label_number_4 = QLabel(self.channel_tile_4)
        self.group_label_number_4.setObjectName(u"group_label_number_4")

        self.group_layout_4.addWidget(self.group_label_number_4)

        self.spacerRightGroup_4 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_4.addItem(self.spacerRightGroup_4)


        self.verticalLayout_4.addLayout(self.group_layout_4)

        self.state_label_4 = QLabel(self.channel_tile_4)
        self.state_label_4.setObjectName(u"state_label_4")
        sizePolicy1.setHeightForWidth(self.state_label_4.sizePolicy().hasHeightForWidth())
        self.state_label_4.setSizePolicy(sizePolicy1)

        self.verticalLayout_4.addWidget(self.state_label_4)


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

        self.group_layout_5 = QHBoxLayout()
        self.group_layout_5.setObjectName(u"group_layout_5")
        self.spacerLeftGroup_5 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_5.addItem(self.spacerLeftGroup_5)

        self.group_label_title_5 = QLabel(self.channel_tile_5)
        self.group_label_title_5.setObjectName(u"group_label_title_5")

        self.group_layout_5.addWidget(self.group_label_title_5)

        self.group_label_number_5 = QLabel(self.channel_tile_5)
        self.group_label_number_5.setObjectName(u"group_label_number_5")

        self.group_layout_5.addWidget(self.group_label_number_5)

        self.spacerRightGroup_5 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_5.addItem(self.spacerRightGroup_5)


        self.verticalLayout_5.addLayout(self.group_layout_5)

        self.state_label_5 = QLabel(self.channel_tile_5)
        self.state_label_5.setObjectName(u"state_label_5")
        sizePolicy1.setHeightForWidth(self.state_label_5.sizePolicy().hasHeightForWidth())
        self.state_label_5.setSizePolicy(sizePolicy1)

        self.verticalLayout_5.addWidget(self.state_label_5)


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

        self.group_layout_6 = QHBoxLayout()
        self.group_layout_6.setObjectName(u"group_layout_6")
        self.spacerLeftGroup_6 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_6.addItem(self.spacerLeftGroup_6)

        self.group_label_title_6 = QLabel(self.channel_tile_6)
        self.group_label_title_6.setObjectName(u"group_label_title_6")

        self.group_layout_6.addWidget(self.group_label_title_6)

        self.group_label_number_6 = QLabel(self.channel_tile_6)
        self.group_label_number_6.setObjectName(u"group_label_number_6")

        self.group_layout_6.addWidget(self.group_label_number_6)

        self.spacerRightGroup_6 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_6.addItem(self.spacerRightGroup_6)


        self.verticalLayout_6.addLayout(self.group_layout_6)

        self.state_label_6 = QLabel(self.channel_tile_6)
        self.state_label_6.setObjectName(u"state_label_6")
        sizePolicy1.setHeightForWidth(self.state_label_6.sizePolicy().hasHeightForWidth())
        self.state_label_6.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.state_label_6)


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

        self.group_layout_7 = QHBoxLayout()
        self.group_layout_7.setObjectName(u"group_layout_7")
        self.spacerLeftGroup_7 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_7.addItem(self.spacerLeftGroup_7)

        self.group_label_title_7 = QLabel(self.channel_tile_7)
        self.group_label_title_7.setObjectName(u"group_label_title_7")

        self.group_layout_7.addWidget(self.group_label_title_7)

        self.group_label_number_7 = QLabel(self.channel_tile_7)
        self.group_label_number_7.setObjectName(u"group_label_number_7")

        self.group_layout_7.addWidget(self.group_label_number_7)

        self.spacerRightGroup_7 = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.group_layout_7.addItem(self.spacerRightGroup_7)


        self.verticalLayout_7.addLayout(self.group_layout_7)

        self.state_label_7 = QLabel(self.channel_tile_7)
        self.state_label_7.setObjectName(u"state_label_7")
        sizePolicy1.setHeightForWidth(self.state_label_7.sizePolicy().hasHeightForWidth())
        self.state_label_7.setSizePolicy(sizePolicy1)

        self.verticalLayout_7.addWidget(self.state_label_7)


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

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toggle_watering_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.date_time_label.setText(QCoreApplication.translate("MainWindow", u"12:30 | 12.04.2025", None))
        self.wifi_status_icon.setText("")
        self.toggle_watering_btn.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.toggle_watering_btn.setProperty(u"class", QCoreApplication.translate("MainWindow", u"startStopButton", None))
        self.manual_mode_btn.setText("")
        self.manual_mode_btn.setProperty(u"class", QCoreApplication.translate("MainWindow", u"topBarButton", None))
        self.schedule_btn.setText("")
        self.schedule_btn.setProperty(u"class", QCoreApplication.translate("MainWindow", u"topBarButton", None))
        self.settings_btn.setText("")
        self.settings_btn.setProperty(u"class", QCoreApplication.translate("MainWindow", u"topBarButton", None))
        self.name_label_1.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.name_label_1.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_1.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_1.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.group_label_number_1.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_1.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_1.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.name_label_2.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.name_label_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_2.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.group_label_number_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_2.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_2.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.name_label_3.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.name_label_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_3.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.group_label_number_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_3.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_3.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.name_label_4.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.name_label_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_4.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.group_label_number_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_4.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_4.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.name_label_5.setText(QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.name_label_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_5.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.group_label_number_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_5.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_5.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.name_label_6.setText(QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.name_label_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_6.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.group_label_number_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_6.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_6.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.name_label_7.setText(QCoreApplication.translate("MainWindow", u"Channel 7", None))
        self.name_label_7.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_title_7.setText(QCoreApplication.translate("MainWindow", u"Group:", None))
        self.group_label_title_7.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.group_label_number_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.group_label_number_7.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.state_label_7.setText(QCoreApplication.translate("MainWindow", u"0 min", None))
        self.state_label_7.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
        self.pump_name_label.setText(QCoreApplication.translate("MainWindow", u"Pump", None))
        self.pump_name_label.setProperty(u"class", QCoreApplication.translate("MainWindow", u"channelTileLabel", None))
    # retranslateUi

