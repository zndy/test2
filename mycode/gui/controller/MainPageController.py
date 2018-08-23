#!/usr/bin/python3
from mycode.gui.view.MainPage import *
from mycode.gui.controller.DiamondPointsPageController import *
from mycode.util.WindowUtil import *
from mycode.gui.BeanFactory import *


class MainPageController:
    def __init__(self):
        self.window = Tk
        self.mainPageModel = beanFactory.mainPageModel
        self.diamondPointsPageModel = beanFactory.diamondPointsPageModel
        self.mainPage = MainPage

    def openMainPage(self):
        self.window = Tk()
        WindowUtil.setWindowAttributes("Abrichten Page", 450, 550, self.window)
        self.mainPage = MainPage(self.window)
        self.refreshViewFromModel()
        self.mainPage.addCalcBtnListener(self.calcBtnPressed)
        self.window.mainloop()

    def calcBtnPressed(self, event):
        self.saveViewDataToModel()
        self.updateDiamondPointsPageModel()
        self.openDiamondPage()

    def refreshViewFromModel(self):
        # abricht scheibe value
        self.mainPage.abricht_p1x.set(self.mainPageModel.abricht_p1.getX())
        self.mainPage.abricht_p1y.set(self.mainPageModel.abricht_p1.getY())
        self.mainPage.abricht_p2x.set(self.mainPageModel.abricht_p2.getX())
        self.mainPage.abricht_p2y.set(self.mainPageModel.abricht_p2.getY())

        # diamond scheibe value
        self.mainPage.diamond_p1x.set(self.mainPageModel.diamond_p1.getX())
        self.mainPage.diamond_p1y.set(self.mainPageModel.diamond_p1.getY())
        self.mainPage.diamond_p2x.set(self.mainPageModel.diamond_p2.getX())
        self.mainPage.diamond_p2y.set(self.mainPageModel.diamond_p2.getY())
        self.mainPage.diamond_p3x.set(self.mainPageModel.diamond_p3.getX())
        self.mainPage.diamond_p3y.set(self.mainPageModel.diamond_p3.getY())
        self.mainPage.diamond_p4x.set(self.mainPageModel.diamond_p4.getX())
        self.mainPage.diamond_p4y.set(self.mainPageModel.diamond_p4.getY())

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

    def updateDiamondPointsPageModel(self):
        self.diamondPointsPageModel.abrichtScheibeWidth = self.mainPageModel.calcAbrichtScheibeWidth()
        self.diamondPointsPageModel.abrichtAngleDeg = self.mainPageModel.calcAbrichtAngleDeg()

        self.diamondPointsPageModel.diamondPointA1 = self.mainPageModel.calcDiamondPointA1()
        self.diamondPointsPageModel.diamondPointA2 = self.mainPageModel.calcDiamondPointA2()
        self.diamondPointsPageModel.diamondPointB1 = self.mainPageModel.calcDiamondPointB1()
        self.diamondPointsPageModel.diamondPointB2 = self.mainPageModel.calcDiamondPointB2()
        self.diamondPointsPageModel.diamondPointC1 = self.mainPageModel.calcDiamondPointC1()
        self.diamondPointsPageModel.diamondPointC2 = self.mainPageModel.calcDiamondPointC2()

    def openDiamondPage(self):
        DiamondPointsPageController(self.window).openDiamondPage()
