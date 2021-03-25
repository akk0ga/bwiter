from api.Api import Api


class App:
    def run(self):
        api = Api()
        api.get(url='https://api.twitter.com/1.1/account/verify_credentials.json')


if __name__ == '__main__':
    app = App()
    app.run()
