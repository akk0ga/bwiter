from twitter.User import User
import time
import datetime


class App:

    def last_search(self, t0):
        calc: bool = True
        if calc:
            t1 = datetime.datetime.now()

    def run(self):
        user = User()
        print('bot is running...')
        time.sleep(0.5)
        req_done: int = 0
        while True:
            time_req: datetime = datetime.datetime.now()
            microsecond: int = time_req.microsecond
            second: int = time_req.second

            if 240_000 <= microsecond <= 260_000 and req_done == 0:
                print(f'last tweet {user.last_tweet(screen_name="_dieuoff")}')
                print(microsecond)
                req_done = 1
            if 740_000 <= microsecond <= 760_000 and req_done == 1:
                print(f'last tweet {user.last_tweet(screen_name="_dieuoff")}')
                print(microsecond)
                req_done = 0

        # print(user.get_users_list())
        # print(f'single user {user.get_user(user_id="2295631308", screen_name="RBW_MAMAMOO")}')
        # print(f'last tweet {user.last_tweet(screen_name="_dieuoff")}')


if __name__ == '__main__':
    app = App()
    app.run()
