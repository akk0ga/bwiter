from twitter.User import User
from api.Api import Api
from threading import Timer
import time


class App:
    def __init__(self):
        self.__user = User()
        self.__api = Api()

    def __search_new_tweet(self):
        print('new tweet')
        print(self.__user.last_tweet(screen_name="_dieuoff"))
        Timer(60, self.__search_new_tweet).start()

    def run(self):
        print('bot is running...')
        time.sleep(0.5)
        self.__search_new_tweet()
    # print(user.get_users_list())
    # print(f'single user {user.get_user(user_id="2295631308", screen_name="RBW_MAMAMOO")}')


if __name__ == '__main__':
    app = App()
    app.run()
