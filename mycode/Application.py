#!/usr/bin/python3
from tkinter import *
from mycode.util.WindowUtil import *
from mycode.gui.controller.MainPageController import *
from mycode.gui.BeanFactory import *


class Application:
    def start(self):
        root = beanFactory.root
        WindowUtil.setWindowAttributes("Abrichten Page", 800, 650, root)
        MainPageController()
        root.mainloop()


def main():
    Application().start()


if __name__ == '__main__':
    main()
