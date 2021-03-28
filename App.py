from twitter.User import User
from api.Api import Api
from notification.Notify import Notify
from threading import Timer


class App:
    def __init__(self):
        self.__user = User()
        self.__api = Api()

    def __search_new_tweet(self):
        print('new tweet')
        print(self.__user.last_tweet(screen_name="_dieuoff"))
        Timer(60, self.__search_new_tweet).start()

    def run(self):
        notify = Notify()
        notify.bot_status()
        self.__search_new_tweet()


if __name__ == '__main__':
    app = App()
    app.run()
