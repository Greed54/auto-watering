from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QResizeEvent, QMouseEvent
from PySide6.QtWidgets import QWidget

from ui.WarningDialog import Ui_WarningDialog


class WarningDialog(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 128);")

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch()

        self.container = QtWidgets.QFrame(self)
        self.container.setFixedSize(500, 400)
        self.container.setStyleSheet("background-color: white; border-radius: 10px;")

        layout.addWidget(self.container, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addStretch()

        self.ui = Ui_WarningDialog()
        self.ui.setupUi(self.container)

        self.ui.ok_btn.clicked.connect(self.hide)

        self.hide()

    def show(self):
        self.resize(self.parent().size())
        super().show()
        self.raise_()

    def set_text(self, text: str):
        self.ui.warning_text_label.setText(text)

    def resizeEvent(self, event: QResizeEvent):
        self.resize(self.parent().size())
        super().resizeEvent(event)

    def mousePressEvent(self, event: QMouseEvent):
        event.accept()
