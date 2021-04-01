import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        #define status label
        self.status = QtWidgets.QLabel("status")
        self.status.setGeometry(QtWidgets, x=1)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.status)

        self.button.clicked.connect(self.change_text)

    @QtCore.Slot()
    def change_text(self):
        if self.text.text() == 'hello world':
            self.text.setText('test')
        else:
            self.text.setText('hello world')



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = App()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
