#!/usr/bin/python3
from mycode.gui.model.MainPageModel import *
from mycode.gui.view.MainPage import *
from mycode.gui.view.DiamondPointsPage import *
from mycode.util.WindowUtil import *


class MainPageController:
    def __init__(self, root):
        self.root = root
        self.mainPageModel = MainPageModel()
        self.mainPage = MainPage(self.root)
        self.mainPage.addCalcBtnListener(self.calcBtnPressed)

    def calcBtnPressed(self, event):
        self.saveViewDataToModel()
        self.updateViewDistance()
        self.updateViewPoints()
        self.openDiamondPage()

    def saveViewDataToModel(self):
        self.mainPageModel.abricht_p1.setX(self.mainPage.abricht_p1x.get())
        self.mainPageModel.abricht_p1.setY(self.mainPage.abricht_p1y.get())
        self.mainPageModel.abricht_p2.setX(self.mainPage.abricht_p2x.get())
        self.mainPageModel.abricht_p2.setY(self.mainPage.abricht_p2y.get())
        self.mainPageModel.diamond_p1.setX(self.mainPage.diamond_p1x.get())
        self.mainPageModel.diamond_p1.setY(self.mainPage.diamond_p1y.get())
        self.mainPageModel.diamond_p2.setX(self.mainPage.diamond_p2x.get())
        self.mainPageModel.diamond_p2.setY(self.mainPage.diamond_p2y.get())
        self.mainPageModel.diamond_p3.setX(self.mainPage.diamond_p3x.get())
        self.mainPageModel.diamond_p3.setY(self.mainPage.diamond_p3y.get())
        self.mainPageModel.diamond_p4.setX(self.mainPage.diamond_p4x.get())
        self.mainPageModel.diamond_p4.setY(self.mainPage.diamond_p4y.get())

    def updateViewDistance(self):
        self.mainPage.distance.set(self.mainPageModel.calcAbrichtScheibeWidth())

    def updateViewPoints(self):
        diamondPointA1 = self.mainPageModel.calcDiamondPointA1()
        self.mainPage.diamond_a1x.set(diamondPointA1.getX())
        self.mainPage.diamond_a1y.set(diamondPointA1.getY())
        diamondPointA2 = self.mainPageModel.calcDiamondPointA2()
        self.mainPage.diamond_a2x.set(diamondPointA2.getX())
        self.mainPage.diamond_a2y.set(diamondPointA2.getY())
        diamondPointB1 = self.mainPageModel.calcDiamondPointB1()
        self.mainPage.diamond_b1x.set(diamondPointB1.getX())
        self.mainPage.diamond_b1y.set(diamondPointB1.getY())
        diamondPointB2 = self.mainPageModel.calcDiamondPointB2()
        self.mainPage.diamond_b2x.set(diamondPointB2.getX())
        self.mainPage.diamond_b2y.set(diamondPointB2.getY())
        diamondPointC1 = self.mainPageModel.calcDiamondPointC1()
        self.mainPage.diamond_c1x.set(diamondPointC1.getX())
        self.mainPage.diamond_c1y.set(diamondPointC1.getY())
        diamondPointC2 = self.mainPageModel.calcDiamondPointC2()
        self.mainPage.diamond_c2x.set(diamondPointC2.getX())
        self.mainPage.diamond_c2y.set(diamondPointC2.getY())

    def openDiamondPage(self):
        window = Toplevel(self.root)
        WindowUtil.setWindowAttributes("Diamond Points Page", 300, 200, window)
        DiamondPointsPage(window)
        window.mainloop()
