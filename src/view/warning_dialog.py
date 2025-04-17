from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QWidget

from ui.WarningDialog import Ui_WarningDialog


class WarningDialog(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.setGeometry(parent.rect())
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, False)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 128);")

        self.container = QtWidgets.QFrame(self)
        self.container.setFixedSize(400, 250)

        self.ui = Ui_WarningDialog()
        self.ui.setupUi(self.container)
        self.hide()

        self.ui.ok_btn.clicked.connect(self.hide)

        self.raise_()
        self._recenter()

    def set_text(self, text: str):
        self.ui.warning_text_label.setText(text)

    def _recenter(self):
        pw = self.parent().width()
        ph = self.parent().height()
        cw = self.container.width()
        ch = self.container.height()
        x = (pw - cw) // 2
        y = (ph - ch) // 2
        self.container.move(x, y)

    def mousePressEvent(self, event):
        event.accept()
