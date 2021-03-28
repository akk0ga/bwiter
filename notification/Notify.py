import subprocess as notif


class Notify:
    def __init__(self, title: str, desc: str, like_link: str, show_link: str):
        self.__title: str = title
        self.__desc: str = desc
        self.__like_link: str = like_link
        self.__show_link: str = show_link

    def display_tweet(self):
        pass

    def display_user(self):
        pass

    def display_bot_status(self):
        pass
