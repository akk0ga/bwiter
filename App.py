from twitter.User import User


class App:
    def run(self):
        user = User()
        print(f'user list {user.get_users_list()}')
        print(f'single user {user.get_user(user_id="2295631308", screen_name="RBW_MAMAMOO")}')
        print(f'last tweet {user.last_tweet(screen_name="RBW_MAMAMOO")}')


if __name__ == '__main__':
    app = App()
    app.run()
