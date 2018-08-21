#!/usr/bin/python3
from mycode.gui.model.MainPageModel import *
from mycode.gui.view.MainPage import *


class MainPageController:
    def __init__(self):
        self.mainPageModel = MainPageModel()
        self.mainPage = MainPage()
        self.mainPage.addCalcBtnListener(self.calcBtnPressed)

    def calcBtnPressed(self, event):
        self.mainPageModel.abricht_p1.setX(self.mainPage.abricht_p1x.get())
        self.mainPageModel.abricht_p1.setY(self.mainPage.abricht_p1y.get())
        self.mainPageModel.abricht_p2.setX(self.mainPage.abricht_p2x.get())
        self.mainPageModel.abricht_p2.setY(self.mainPage.abricht_p2y.get())

        self.mainPage.distance.set("distance: " + str(self.mainPageModel.calcAbrichtScheibeWidth()))


def main():
    window = Tk()  # create a Tk root window
    window.title('Abrichten')
    w = 800  # width for the Tk root
    h = 650  # height for the Tk root

    # get screen width and height
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    MainPageController()
    window.mainloop()


if __name__ == '__main__':
    main()
