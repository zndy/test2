#!/usr/bin/python3
from mycode.util.WindowUtil import *


class RBtnSwitchFrameTest:
    def __init__(self):
        self.window = Tk()
        self.leftFrame = Frame(self.window, width=200, height=100, bg="blue",  borderwidth=1)
        self.rightFrame = Frame(self.window, width=200, height=100, bg="red",  borderwidth=1)
        self.selectNr = IntVar()

    def openPage(self):
        WindowUtil.setWindowAttributes("RBtnSwitchFrameTest Page", 800, 500, self.window)
        self.createRBtns()
        self.createLeftFrame()
        self.createRightFrame()
        self.window.mainloop()

    def createRBtns(self):
        Radiobutton(self.window, text="one", variable=self.selectNr, value=1, command=self.onClick).pack(anchor=W)
        Radiobutton(self.window, text="two", variable=self.selectNr, value=2, command=self.onClick).pack(anchor=W)

    def onClick(self):
        print(self.selectNr.get())
        WindowUtil.enableFrame(self.leftFrame)
        WindowUtil.enableFrame(self.rightFrame)
        if self.selectNr.get() == 1:
            WindowUtil.disableFrame(self.rightFrame)
        elif self.selectNr.get() == 2:
            WindowUtil.disableFrame(self.leftFrame)



    def createLeftFrame(self):
        row = 0
        Label(self.leftFrame, text='Abricht Scheibe: ').grid(row=row)
        self.leftFrame.pack(anchor=W)

    def createRightFrame(self):
        row = 0
        Label(self.rightFrame, text='Diamond Scheibe: ').grid(row=row)
        self.rightFrame.pack(anchor=E)


def main():
    RBtnSwitchFrameTest().openPage()


if __name__ == '__main__':
    main()
