# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WarningDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import IconsResource_rc

class Ui_WarningDialog(object):
    def setupUi(self, WarningDialog):
        if not WarningDialog.objectName():
            WarningDialog.setObjectName(u"WarningDialog")
        WarningDialog.resize(400, 250)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WarningDialog.sizePolicy().hasHeightForWidth())
        WarningDialog.setSizePolicy(sizePolicy)
        WarningDialog.setMinimumSize(QSize(400, 250))
        WarningDialog.setMaximumSize(QSize(400, 250))
        WarningDialog.setStyleSheet(u"background-color: white;\n"
"border-radius: 10px;")
        self.verticalLayout = QVBoxLayout(WarningDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.icon = QLabel(WarningDialog)
        self.icon.setObjectName(u"icon")
        self.icon.setPixmap(QPixmap(u":/icons/icons8-warning-48.png"))
        self.icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.icon)

        self.label = QLabel(WarningDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 24pt;")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.warning_text_label = QLabel(WarningDialog)
        self.warning_text_label.setObjectName(u"warning_text_label")
        self.warning_text_label.setMinimumSize(QSize(0, 110))
        font1 = QFont()
        font1.setPointSize(30)
        self.warning_text_label.setFont(font1)
        self.warning_text_label.setStyleSheet(u"font-size: 30pt;")
        self.warning_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.warning_text_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ok_btn = QPushButton(WarningDialog)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(150, 50))
        font2 = QFont()
        font2.setPointSize(20)
        self.ok_btn.setFont(font2)
        self.ok_btn.setStyleSheet(u"font-size: 20pt;")

        self.horizontalLayout.addWidget(self.ok_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(WarningDialog)

        QMetaObject.connectSlotsByName(WarningDialog)
    # setupUi

    def retranslateUi(self, WarningDialog):
        WarningDialog.setWindowTitle(QCoreApplication.translate("WarningDialog", u"Dialog", None))
        self.icon.setText("")
        self.label.setText(QCoreApplication.translate("WarningDialog", u"Warning", None))
        self.label.setProperty(u"class", QCoreApplication.translate("WarningDialog", u"dialogHeaderTextLabel", None))
        self.warning_text_label.setText(QCoreApplication.translate("WarningDialog", u"TextLabel", None))
        self.warning_text_label.setProperty(u"class", QCoreApplication.translate("WarningDialog", u"dialogTextLabel", None))
        self.ok_btn.setText(QCoreApplication.translate("WarningDialog", u" OK", None))
        self.ok_btn.setProperty(u"class", QCoreApplication.translate("WarningDialog", u"warning", None))
    # retranslateUi

