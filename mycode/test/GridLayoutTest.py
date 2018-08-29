#!/usr/bin/python3
from mycode.util.WindowUtil import *


class GridLayoutTest:
    def __init__(self):
        self.window = Tk()

    def openPage(self):
        WindowUtil.setWindowAttributes("GridLayoutTest Page", 800, 500, self.window)
        Label(self.window, text="First: ").grid(row=0, sticky=W)
        Label(self.window, text="Second: ").grid(row=1, sticky=W)

        e1 = Entry(self.window)
        e2 = Entry(self.window)

        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        self.window.mainloop()


def main():
    GridLayoutTest().openPage()


if __name__ == '__main__':
    main()
