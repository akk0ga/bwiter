from twitter.User import User


class App:
    def run(self):
        user = User()
        print(user.get_user(user_id='2295631308', screen_name='RBW_MAMAMOO'))


if __name__ == '__main__':
    app = App()
    app.run()
