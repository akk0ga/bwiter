from bot.Bot import Bot
from gui.Window import Window


class App:
    def __init__(self):
        self.__bot = Bot('RBW_MAMAMOO')

    def run(self):
        Window()


if __name__ == '__main__':
    app = App()
    app.run()
