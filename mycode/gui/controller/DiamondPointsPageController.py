#!/usr/bin/python3
from mycode.gui.BeanFactory import *
from mycode.gui.view.DiamondPointsPage import *
from mycode.util.WindowUtil import *


class DiamondPointsPageController:
    def __init__(self,parent):
        self.parent = parent
        self.diamondPointsPageModel = BeanFactory.getInstance().diamondPointsPageModel
        self.diamondPointsPage = DiamondPointsPage

    def openDiamondPage(self):
        window = Toplevel(self.parent)
        WindowUtil.setWindowAttributes("Diamond Points Page", 650, 800, window)
        self.diamondPointsPage = DiamondPointsPage(window)
        self.__updateView()

    def __updateView(self):
        self.diamondPointsPage.abrichtScheibeWidth.set(self.diamondPointsPageModel.abrichtScheibeWidth)
        self.diamondPointsPage.abrichtAngle.set(self.diamondPointsPageModel.abrichtAngleDeg)
        self.diamondPointsPage.diamond_a1x.set(self.diamondPointsPageModel.diamondPointA1.getX())
        self.diamondPointsPage.diamond_a1y.set(self.diamondPointsPageModel.diamondPointA1.getY())
        self.diamondPointsPage.diamond_a2x.set(self.diamondPointsPageModel.diamondPointA2.getX())
        self.diamondPointsPage.diamond_a2y.set(self.diamondPointsPageModel.diamondPointA2.getY())
        self.diamondPointsPage.diamond_b1x.set(self.diamondPointsPageModel.diamondPointB1.getX())
        self.diamondPointsPage.diamond_b1y.set(self.diamondPointsPageModel.diamondPointB1.getY())
        self.diamondPointsPage.diamond_b2x.set(self.diamondPointsPageModel.diamondPointB2.getX())
        self.diamondPointsPage.diamond_b2y.set(self.diamondPointsPageModel.diamondPointB2.getY())
        self.diamondPointsPage.diamond_c1x.set(self.diamondPointsPageModel.diamondPointC1.getX())
        self.diamondPointsPage.diamond_c1y.set(self.diamondPointsPageModel.diamondPointC1.getY())
        self.diamondPointsPage.diamond_c2x.set(self.diamondPointsPageModel.diamondPointC2.getX())
        self.diamondPointsPage.diamond_c2y.set(self.diamondPointsPageModel.diamondPointC2.getY())

        self.diamondPointsPage.xResult.set(self.diamondPointsPageModel.xResult)
        self.diamondPointsPage.yResult.set(self.diamondPointsPageModel.yResult)

        WindowUtil.enableFrame(self.diamondPointsPage.isoFrame)
        self.diamondPointsPage.isoText.insert(INSERT, self.diamondPointsPageModel.iso)
        WindowUtil.disableFrame(self.diamondPointsPage.isoFrame)
