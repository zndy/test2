#!/usr/bin/python3
from mycode.util.CalcUtil import *


class MainPageModel:
    def __init__(self):
        self.abricht_p1 = MyPoint(-2.0, 0.0)
        self.abricht_p2 = MyPoint(2.0, 0.0)

        self.diamond_p1 = MyPoint(-3.0, -2.0)
        self.diamond_p2 = MyPoint(-1.0, 0.0)
        self.diamond_p3 = MyPoint(1.0, 0.0)
        self.diamond_p4 = MyPoint(3.0, -2.0)

        self.beginDistance = 1.0
        self.abricht_diameter = 40.0
        self.abricht_flansch = 20.0
        self.diamond_diameter = 40.0
        self.diamond_flansch = 20.0
        self.deltax = 100.0
        self.deltay = 100.0

    def calcAbrichtScheibeWidth(self):
        return CalcUtil.calcDistanceBetween(self.abricht_p1, self.abricht_p2)

    def calcAbrichtAngleDeg(self):
        line1 = Line(self.diamond_p1.toSympyPoint(), self.diamond_p2.toSympyPoint())
        line2 = Line(self.diamond_p2.toSympyPoint(), self.diamond_p3.toSympyPoint())
        return N(deg(line1.angle_between(line2)))

    def calcDiamondPointA1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p1, self.diamond_p2,
                                         self.calcAbrichtScheibeWidth() + self.beginDistance)

    def calcDiamondPointA2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p2, self.diamond_p1,
                                         self.calcAbrichtScheibeWidth() + self.beginDistance)

    def calcDiamondPointB1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p2, self.diamond_p3,
                                         self.calcAbrichtScheibeWidth() + self.beginDistance)

    def calcDiamondPointB2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p3, self.diamond_p2,
                                         self.calcAbrichtScheibeWidth() + self.beginDistance)

    def calcDiamondPointC1(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p3, self.diamond_p4,
                                         self.calcAbrichtScheibeWidth() + self.beginDistance)

    def calcDiamondPointC2(self):
        return CalcUtil.calcAbrichtPoint(self.diamond_p4, self.diamond_p3,
                                         self.calcAbrichtScheibeWidth() + self.beginDistance)
