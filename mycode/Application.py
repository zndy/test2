#!/usr/bin/python3
from tkinter import *
from mycode.util.WindowUtil import *
from mycode.gui.controller.MainPageController import *


class Application:
    def start(self):
        root = Tk()
        WindowUtil.setWindowAttributes("Abrichten Page", 800, 650, root)
        MainPageController(root)
        root.mainloop()


def main():
    Application().start()


if __name__ == '__main__':
    main()
