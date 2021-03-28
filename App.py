from twitter.User import User
import time
import datetime


class App:
    def __init__(self):
        self.__user = User()

    def run(self):
        req_complete: bool = False
        print('bot is running...')
        time.sleep(0.5)
        while True:
            # launch request (2 per sec) to get the last tweet and check if the tweet is already show
            time_req: datetime = datetime.datetime.now()
            microsecond: int = time_req.microsecond
            if 200_000 <= microsecond <= 300_000 and not req_complete:
                print(microsecond)
                req_complete = True
                print(self.__user.last_tweet(screen_name="_dieuoff"))

            if 700_000 <= microsecond <= 800_000 and req_complete:
                print(microsecond)
                req_complete = False
                print(self.__user.last_tweet(screen_name="_dieuoff"))

    # print(user.get_users_list())
    # print(f'single user {user.get_user(user_id="2295631308", screen_name="RBW_MAMAMOO")}')


if __name__ == '__main__':
    app = App()
    app.run()
