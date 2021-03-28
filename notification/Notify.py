from win10toast import ToastNotifier as notify


class Notify:
    def __init__(self, name: str = 'username', title: str = 'tweet title', desc: str = 'tweet text'):
        self.__notify = notify()
        self.__name = name
        self.__title = title
        self.__desc: str = desc

    def tweet(self):
        title = f'New Tweet from {self.__name}'
        msg = f'title: {self.__title}\ncontent: {self.__desc}'
        self.__notify.show_toast(title=title, msg=msg, icon_path='misc/logo.ico')

    def user(self):
        title = f'You are now listening tweet from {self.__name}'
        self.__notify.show_toast(title=title, msg=' ', icon_path='misc/logo.ico')

    def bot_status(self):
        title = f'bot is running...'
        self.__notify.show_toast(title=title, msg=' ', icon_path='misc/logo.ico')


Notify().bot_status()
