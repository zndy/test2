#!/usr/bin/python3
from mycode.util.CalcUtil import *


class MainPageModel:
    def __init__(self):
        self.abricht_p1 = MyPoint(-2, 0)
        self.abricht_p2 = MyPoint(2, 0)

        self.diamond_p1 = MyPoint(-3, -2)
        self.diamond_p2 = MyPoint(-1, 0)
        self.diamond_p3 = MyPoint(1, 0)
        self.diamond_p4 = MyPoint(3, -2)

        self.abricht_diam = 40
        self.abricht_flansch = 20
        self.diamond_diam = 40
        self.diamond_flansch = 20
        self.deltax = 100
        self.deltay = 100

    def calcAbrichtScheibeWidth(self):
        return CalcUtil.calcDistanceBetween(self.abricht_p1, self.abricht_p2)

    def calcAbrichtAngleDeg(self):
        line1 = Line(self.diamond_p1.toSympyPoint(), self.diamond_p2.toSympyPoint())
        line2 = Line(self.diamond_p2.toSympyPoint(), self.diamond_p3.toSympyPoint())
        return N(deg(line1.angle_between(line2)))

    def calcDiamondPointA1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p1, self.diamond_p2, self.calcAbrichtScheibeWidth())

    def calcDiamondPointA2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p2, self.diamond_p1, self.calcAbrichtScheibeWidth())

    def calcDiamondPointB1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p2, self.diamond_p3, self.calcAbrichtScheibeWidth())

    def calcDiamondPointB2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p3, self.diamond_p2, self.calcAbrichtScheibeWidth())

    def calcDiamondPointC1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p3, self.diamond_p4, self.calcAbrichtScheibeWidth())

    def calcDiamondPointC2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p4, self.diamond_p3, self.calcAbrichtScheibeWidth())
