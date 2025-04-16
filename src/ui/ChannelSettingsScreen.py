# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChannelSettingsScreen.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ChannelSettingsWindow(object):
    def setupUi(self, ChannelSettingsWindow):
        if not ChannelSettingsWindow.objectName():
            ChannelSettingsWindow.setObjectName(u"ChannelSettingsWindow")
        ChannelSettingsWindow.resize(800, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ChannelSettingsWindow.sizePolicy().hasHeightForWidth())
        ChannelSettingsWindow.setSizePolicy(sizePolicy)
        ChannelSettingsWindow.setMinimumSize(QSize(800, 480))
        ChannelSettingsWindow.setMaximumSize(QSize(800, 480))
        ChannelSettingsWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(ChannelSettingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.channel_label = QLabel(self.centralwidget)
        self.channel_label.setObjectName(u"channel_label")
        self.channel_label.setStyleSheet(u"font-size: 48pt;")

        self.horizontalLayout.addWidget(self.channel_label)

        self.channel_number_label = QLabel(self.centralwidget)
        self.channel_number_label.setObjectName(u"channel_number_label")
        self.channel_number_label.setStyleSheet(u"font-size: 48pt;")

        self.horizontalLayout.addWidget(self.channel_number_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.channel_active_label = QLabel(self.centralwidget)
        self.channel_active_label.setObjectName(u"channel_active_label")
        self.channel_active_label.setStyleSheet(u"font-size: 36pt;")

        self.horizontalLayout_2.addWidget(self.channel_active_label)

        self.channel_active_check_box = QCheckBox(self.centralwidget)
        self.channel_active_check_box.setObjectName(u"channel_active_check_box")
        self.channel_active_check_box.setMinimumSize(QSize(50, 50))
        self.channel_active_check_box.setStyleSheet(u"QCheckBox::indicator { width:50px; height: 50px;}")
        self.channel_active_check_box.setTristate(False)

        self.horizontalLayout_2.addWidget(self.channel_active_check_box)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.group_label = QLabel(self.centralwidget)
        self.group_label.setObjectName(u"group_label")
        self.group_label.setStyleSheet(u"font-size: 36pt;")

        self.horizontalLayout_3.addWidget(self.group_label)

        self.group_combo_box = QComboBox(self.centralwidget)
        self.group_combo_box.addItem("")
        self.group_combo_box.addItem("")
        self.group_combo_box.addItem("")
        self.group_combo_box.addItem("")
        self.group_combo_box.addItem("")
        self.group_combo_box.addItem("")
        self.group_combo_box.addItem("")
        self.group_combo_box.setObjectName(u"group_combo_box")
        self.group_combo_box.setMinimumSize(QSize(200, 50))
        self.group_combo_box.setStyleSheet(u"font-size: 20pt;")
        self.group_combo_box.setEditable(False)
        self.group_combo_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_3.addWidget(self.group_combo_box)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.save_settings_btn = QPushButton(self.centralwidget)
        self.save_settings_btn.setObjectName(u"save_settings_btn")
        self.save_settings_btn.setMinimumSize(QSize(200, 70))
        font = QFont()
        font.setPointSize(36)
        self.save_settings_btn.setFont(font)
        self.save_settings_btn.setStyleSheet(u"font-size: 36pt;")

        self.horizontalLayout_5.addWidget(self.save_settings_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 300, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        ChannelSettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ChannelSettingsWindow)

        QMetaObject.connectSlotsByName(ChannelSettingsWindow)
    # setupUi

    def retranslateUi(self, ChannelSettingsWindow):
        ChannelSettingsWindow.setWindowTitle(QCoreApplication.translate("ChannelSettingsWindow", u"ChannelSettings", None))
        self.channel_label.setText(QCoreApplication.translate("ChannelSettingsWindow", u"Channel:", None))
        self.channel_number_label.setText(QCoreApplication.translate("ChannelSettingsWindow", u"0", None))
        self.channel_active_label.setText(QCoreApplication.translate("ChannelSettingsWindow", u"Active: ", None))
        self.channel_active_check_box.setText("")
        self.group_label.setText(QCoreApplication.translate("ChannelSettingsWindow", u"Group: ", None))
        self.group_combo_box.setItemText(0, QCoreApplication.translate("ChannelSettingsWindow", u"1", None))
        self.group_combo_box.setItemText(1, QCoreApplication.translate("ChannelSettingsWindow", u"2", None))
        self.group_combo_box.setItemText(2, QCoreApplication.translate("ChannelSettingsWindow", u"3", None))
        self.group_combo_box.setItemText(3, QCoreApplication.translate("ChannelSettingsWindow", u"4", None))
        self.group_combo_box.setItemText(4, QCoreApplication.translate("ChannelSettingsWindow", u"5", None))
        self.group_combo_box.setItemText(5, QCoreApplication.translate("ChannelSettingsWindow", u"6", None))
        self.group_combo_box.setItemText(6, QCoreApplication.translate("ChannelSettingsWindow", u"7", None))

        self.save_settings_btn.setText(QCoreApplication.translate("ChannelSettingsWindow", u"OK", None))
    # retranslateUi

