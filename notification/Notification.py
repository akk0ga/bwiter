from win10toast import ToastNotifier as Notify


class Notification:
    def __init__(self):
        self.__notify = Notify()

    def tweet(self, name: str, title: str, desc: str):
        """
        display notif when new tweet is get
        :return:
        """
        notify_title: str = f'New Tweet from {name}'
        notify_msg: str = f'title: {title}\ncontent: {desc}'
        self.__notify.show_toast(title=notify_title, msg=notify_msg, icon_path='misc/logo.ico')

    def user(self, name: str):
        """
        notify for user info when changed track account
        :return:
        """
        title: str = f'You are now listening tweet from {name}'
        self.__notify.show_toast(title=title, msg=' ', icon_path='misc/logo.ico')

    def bot_status(self, status: str):
        """
        notify if the bot is running or not, status accepted:\n
        run or stop
        :param status:
        :return:
        """
        title: str = 'bot is running...' if status == 'run' else 'bot stopped'
        self.__notify.show_toast(title=title, msg=' ', icon_path='misc/logo.ico')
