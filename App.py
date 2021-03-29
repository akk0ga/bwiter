from twitter.User import User
from api.Api import Api
from notification.Notification import Notification
from threading import Timer


class App:
    def __init__(self):
        self.__user = User()
        self.__api = Api()
        self.__notify = Notification()

    def __search_new_tweet(self):
        print('search...')
        print(self.__user.last_tweet(screen_name="AstolfoToga"))
        Timer(60, self.__search_new_tweet).start()

    def run(self):
        self.__notify.bot_status('run')
        self.__search_new_tweet()


if __name__ == '__main__':
    app = App()
    app.run()
