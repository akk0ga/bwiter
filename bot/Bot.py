from twitter.User import User
from notification.Notification import Notification
from threading import Timer


class Bot:
    def __init__(self, refresh_time: int = 30):
        self.__notify: Notification = Notification()
        self.__user: User = User(screen_name='_dieuoff')
        self.__refresh_time: int = refresh_time if refresh_time >= 30 else 30
        self.__run: bool = False

    def search_tweet(self):
        """
        search new tweet each x second
        :return:
        """
        if not self.__run:
            self.display_status_run()
        print('search...')
        print(self.__user.last_tweet())
        Timer(self.__refresh_time, self.search_tweet).start()

    def display_status_run(self):
        self.__notify.bot_status('run')
        self.__run = True
