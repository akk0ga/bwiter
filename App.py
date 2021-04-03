import sys
from PyQt5.QtWidgets import QApplication
from bot.Bot import Bot


class App:
    def __init__(self):
        self.__bot = Bot(account_track='')

    def run(self):
        self.__bot.set_user_to_track()
        self.__bot.search_tweet()


if __name__ == '__main__':
    app = App()
    app.run()
