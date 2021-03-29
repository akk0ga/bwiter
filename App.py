from twitter.User import User
from api.Api import Api
from notification.Notification import Notification
from threading import Timer


class App:
    def __init__(self):
        self.__user = User(screen_name='_dieuoff')
        self.__api = Api()
        self.__notify = Notification()

    def __search_new_tweet(self, refresh_time: int = 30):
        if refresh_time >= 1:
            print('search...')
            print(self.__user.last_tweet())
            Timer(refresh_time, self.__search_new_tweet).start()
        else:
            raise Exception('you can\'t have less than 30 second (api rate limit u know)')

    def run(self):
        self.__notify.bot_status('run')
        self.__search_new_tweet()


if __name__ == '__main__':
    app = App()
    app.run()
