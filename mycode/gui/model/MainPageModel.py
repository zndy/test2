#!/usr/bin/python3
from mycode.entity.MyPoint import *
from mycode.util.CalcUtil import *


class MainPageModel:
    def __init__(self):
        self.abricht_p1 = MyPoint()
        self.abricht_p2 = MyPoint()

        self.diamond_p1 = MyPoint()
        self.diamond_p2 = MyPoint()
        self.diamond_p3 = MyPoint()
        self.diamond_p4 = MyPoint()

    def calcAbrichtScheibeWidth(self):
        return CalcUtil.calcDistanceBetween(self.abricht_p1, self.abricht_p2)

    def calcAbrichtPointA1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p1, self.diamond_p2, self.calcAbrichtScheibeWidth())

    def calcAbrichtPointA2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p2, self.diamond_p1, self.calcAbrichtScheibeWidth())


    def calcAbrichtPointB1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p2, self.diamond_p3, self.calcAbrichtScheibeWidth())


    def calcAbrichtPointB2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p3, self.diamond_p2, self.calcAbrichtScheibeWidth())


    def calcAbrichtPointC1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p3, self.diamond_p4, self.calcAbrichtScheibeWidth())


    def calcAbrichtPointC2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p4, self.diamond_p3, self.calcAbrichtScheibeWidth())

