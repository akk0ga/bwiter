from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from bot.Bot import Bot


class Window(QWidget):
    def __init__(self, account: str):
        QWidget.__init__(self)
        self.__bot = Bot(account_track=account)

        # set Window
        self.setWindowTitle('Bwitter')
        self.resize(1121, 600)

        # start bot button
        self.bot_start = QPushButton('Start bot')
        self.bot_start.clicked.connect(self.__bot.search_tweet)

        # create vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.bot_start)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print('left')
        if event.button() == Qt.RightButton:
            print('right')
