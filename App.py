from bot.Bot import Bot


class App:
    def __init__(self):
        self.__bot = Bot()

    def run(self):
        self.__bot.set_user_to_track()
        self.__bot.search_tweet()


if __name__ == '__main__':
    app = App()
    app.run()
