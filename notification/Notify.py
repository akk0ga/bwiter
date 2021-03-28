from win10toast import ToastNotifier as notify


class Notify:
    def __init__(self, title: str, desc: str, like_link: str, show_link: str):
        self.__notify = notify()
        self.__title: str = title
        self.__desc: str = desc
        self.__like_link: str = like_link
        self.__show_link: str = show_link

    def display_tweet(self):
        self.__notify.show_toast(title=self.__title, msg=self.__desc, icon_path='../misc/logo.ico')

    def display_user(self):
        pass

    def display_bot_status(self):
        pass


Notify(title='test', desc='test', like_link='like', show_link='show').display_tweet()
