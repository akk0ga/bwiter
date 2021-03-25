from api.Api import Api


class App:
    def run(self):
        api = Api()
        api.get()


if __name__ == '__main__':
    app = App()
    app.run()
