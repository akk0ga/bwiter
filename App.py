from twitter.User import User
from twitter.Tweet import Tweet


class App:
    def run(self):
        user = User()
        tweet = Tweet()
        print(user.get_user(user_id='2295631308', screen_name='RBW_MAMAMOO'))
        print(tweet.get_last(user_screen_name='RBW_MAMAMOO'))


if __name__ == '__main__':
    app = App()
    app.run()
