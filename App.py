import sys
from bot.Bot import Bot
from PyQt5.QtWidgets import QApplication
from gui.Window import Window


class App(Window):
    def __init__(self, account: str):
        super().__init__(account)

    def run(self):
        self.show()


if __name__ == '__main__':
    run = QApplication(sys.argv)
    app = App('AstolfoToga')
    app.run()
    run.exec_()
