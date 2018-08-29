#!/usr/bin/python3
from mycode.gui.view.MainPage import *
from mycode.gui.controller.DiamondPointsPageController import *
from mycode.util.WindowUtil import *
from mycode.gui.AbrichtPositionCalculator import *


class MainPageController:
    def __init__(self):
        self.window = Tk
        self.mainPageModel = beanFactory.mainPageModel
        self.diamondPointsPageModel = beanFactory.diamondPointsPageModel
        self.mainPage = MainPage

    def openMainPage(self):
        self.window = Tk()
        WindowUtil.setWindowAttributes("Abrichten Page", 800, 500, self.window)
        self.mainPage = MainPage(self.window)
        self.refreshViewFromModel()
        self.mainPage.addCalcBtnListener(self.calcBtnPressed)
        self.window.mainloop()

    def calcBtnPressed(self, event):
        self.saveViewDataToModel()
        self.updateDiamondPointsPageModel()
        self.calcResult()
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

        # parameters
        self.mainPage.beginDistance.set(self.mainPageModel.beginDistance)
        self.mainPage.abricht_flansch.set(self.mainPageModel.abricht_flansch)
        self.mainPage.diamond_flansch.set(self.mainPageModel.diamond_flansch)
        self.mainPage.deltax.set(self.mainPageModel.deltax)
        self.mainPage.deltay.set(self.mainPageModel.deltay)
        self.mainPage.abricht_diameter.set(self.mainPageModel.abricht_diameter)
        self.mainPage.diamond_diameter.set(self.mainPageModel.diamond_diameter)

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

        # parameters
        self.mainPageModel.beginDistance = self.mainPage.beginDistance.get()
        self.mainPageModel.abricht_flansch = self.mainPage.abricht_flansch.get()
        self.mainPageModel.diamond_flansch = self.mainPage.diamond_flansch.get()
        self.mainPageModel.deltax = self.mainPage.deltax.get()
        self.mainPageModel.deltay = self.mainPage.deltay.get()
        self.mainPageModel.abricht_diameter = self.mainPage.abricht_diameter.get()
        self.mainPageModel.diamond_diameter = self.mainPage.diamond_diameter.get()

    def updateDiamondPointsPageModel(self):
        self.diamondPointsPageModel.abrichtScheibeWidth = self.mainPageModel.calcAbrichtScheibeWidth()
        self.diamondPointsPageModel.abrichtAngleDeg = self.mainPageModel.calcAbrichtAngleDeg()

        self.diamondPointsPageModel.diamondPointA1 = self.mainPageModel.calcDiamondPointA1()
        self.diamondPointsPageModel.diamondPointA2 = self.mainPageModel.calcDiamondPointA2()
        self.diamondPointsPageModel.diamondPointB1 = self.mainPageModel.calcDiamondPointB1()
        self.diamondPointsPageModel.diamondPointB2 = self.mainPageModel.calcDiamondPointB2()
        self.diamondPointsPageModel.diamondPointC1 = self.mainPageModel.calcDiamondPointC1()
        self.diamondPointsPageModel.diamondPointC2 = self.mainPageModel.calcDiamondPointC2()

    def calcResult(self):
        calculator = AbrichtenPositionCalculator()
        result = calculator.calc()
        xResult = result.get(calculator.x)
        yResult = result.get(calculator.y)

        parameters = {}
        parameters[calculator.v] = self.diamondPointsPageModel.abrichtAngleDeg
        parameters[calculator.a_d] = self.mainPageModel.abricht_diameter
        parameters[calculator.d_d] = self.mainPageModel.diamond_diameter
        parameters[calculator.dx] = self.mainPageModel.deltax
        parameters[calculator.dy] = self.mainPageModel.deltay
        parameters[calculator.a_f] = self.mainPageModel.abricht_flansch
        parameters[calculator.d_f] = self.mainPageModel.diamond_flansch

        # remove parameter which value = -1
        for k, v in list(parameters.items()):
            if v == -1:
                del parameters[k]

        self.diamondPointsPageModel.xResult = xResult.subs(parameters).evalf()
        self.diamondPointsPageModel.yResult = yResult.subs(parameters).evalf()

    def openDiamondPage(self):
        DiamondPointsPageController(self.window).openDiamondPage()
