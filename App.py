from bot.Bot import Bot


class App:
    def __init__(self):
        self.__bot = Bot('RBW_MAMAMOO')

    def run(self):
        self.__bot.search_tweet()


if __name__ == '__main__':
    app = App()
    app.run()
