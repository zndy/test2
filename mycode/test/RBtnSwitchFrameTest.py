#!/usr/bin/python3
from mycode.util.WindowUtil import *


class RBtnSwitchFrameTest:
    def __init__(self):
        self.window = Tk()
        self.leftFrame = Frame(self.window, highlightbackground="green", highlightcolor="green", highlightthickness=1,
                               width=100, height=100, bd=0)
        self.rightFrame = Frame(self.window, highlightbackground="red", highlightcolor="red", highlightthickness=1,
                                width=100, height=100, bd=0)
        self.leftFrame.place(x=0, y=30)
        self.rightFrame.place(x=250, y=30)
        self.selectNr = IntVar()
        self.deltax = IntVar()
        self.deltay = IntVar()

    def openPage(self):
        WindowUtil.setWindowAttributes("RBtnSwitchFrameTest Page", 800, 500, self.window)
        self.createRBtns()
        self.createLeftFrame()
        self.createRightFrame()
        self.onClick()
        self.window.mainloop()

    def createRBtns(self):
        leftRadioBtn = Radiobutton(self.window, text="one", variable=self.selectNr, value=1, command=self.onClick)
        leftRadioBtn.place(x=0, y=0)
        leftRadioBtn.select()
        Radiobutton(self.window, text="two", variable=self.selectNr, value=2, command=self.onClick).place(x=250, y=0)

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
        row += 1
        WindowUtil.createInputEntry(self.leftFrame, "Delta X", row, self.deltax)

    def createRightFrame(self):
        row = 0
        Label(self.rightFrame, text='Diamond Scheibe: ').grid(row=row)
        row += 1
        WindowUtil.createInputEntry(self.rightFrame, "Delta Y", row, self.deltay)


def main():
    RBtnSwitchFrameTest().openPage()


if __name__ == '__main__':
    main()
