# importations à faire pour la réalisation d'une interface graphique
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        # set Window
        self.setWindowTitle('Bwitter')
        self.resize(1121, 600)

        # start bot button
        self.bot_start = QPushButton('Start bot')

        # create vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.bot_start)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print('left')
        if event.button() == Qt.RightButton:
            print('right')


app = QApplication(sys.argv)

# create and resize window
window = Window()
window.show()
# exec app
app.exec_()
