from win10toast import ToastNotifier as Notify


class Notification:
    def __init__(self, name: str = 'username', title: str = 'tweet title', desc: str = 'tweet text'):
        self.__notify = Notify()
        self.__name: str = name
        self.__title: str = title
        self.__desc: str = desc

    def tweet(self):
        title: str = f'New Tweet from {self.__name}'
        msg: str = f'title: {self.__title}\ncontent: {self.__desc}'
        self.__notify.show_toast(title=title, msg=msg, icon_path='misc/logo.ico')

    def user(self):
        """
        notify for user info when changed track account
        :return:
        """
        title: str = f'You are now listening tweet from {self.__name}'
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

    # getter and setter
    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_title(self, title: str):
        self.__title = title

    def get_title(self):
        return self.__title

    def set_desc(self, desc: str):
        self.__desc = desc

    def get_desc(self):
        return self.__desc

    name = property(fget=get_name, fset=set_name)
    title = property(fget=get_title, fset=set_title)
    desc = property(fget=get_desc, fset=set_desc)
