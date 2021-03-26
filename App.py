from twitter.User import User


class App:
    def run(self):
        user = User()
        print(user.get_users_list())


if __name__ == '__main__':
    app = App()
    app.run()
