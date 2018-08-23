#!/usr/bin/python3
from mycode.gui.controller.MainPageController import *


class Application:
    def start(self):
        MainPageController().openMainPage()


def main():
    Application().start()


if __name__ == '__main__':
    main()
