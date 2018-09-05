#!/usr/bin/python3
import logging

from mycode.gui.controller.MainPageController import *


class Application:

    def start(self):
        logger = logging.getLogger(__name__)
        logger.warning("application start")
        MainPageController().openMainPage()


def main():
    Application().start()


if __name__ == '__main__':
    main()
