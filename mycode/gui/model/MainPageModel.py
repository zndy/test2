#!/usr/bin/python3
from mycode.util.CalcUtil import *


class MainPageModel:
    def __init__(self):
        self.inputVariationNr = 0  # Nr 1: 3 values, Nr 2: 4 points

        self.abricht_p1 = MyPoint(-2.0, 0.0)
        self.abricht_p2 = MyPoint(2.0, 0.0)

        self.diamond_p1 = MyPoint(-3.0, -2.0)
        self.diamond_p2 = MyPoint(-1.0, 0.0)
        self.diamond_p3 = MyPoint(1.0, 0.0)
        self.diamond_p4 = MyPoint(3.0, -2.0)

        self.diamond_beta = 45.0
        self.diamond_d1 = 10.0
        self.diamond_d2 = 20.0

        self.beginDistance = 1.0
        self.abricht_diameter = 40.0
        self.abricht_flansch = 20.0
        self.diamond_diameter = 40.0
        self.diamond_flansch = 20.0
        self.deltax = 100.0
        self.deltay = 100.0

    def calcAbrichtScheibeWidth(self):
        return CalcUtil.calcDistanceBetween(self.abricht_p1, self.abricht_p2)

    def convertDiamondParameters(self):
        if self.inputVariationNr == 1:
            self.convertThreeValuesToFourPoints()
        elif self.inputVariationNr == 2:
            self.convertFourPointsToThreeValues()

    def convertFourPointsToThreeValues(self):
        line12 = Line(self.diamond_p1.toSympyPoint(), self.diamond_p2.toSympyPoint())
        line34 = Line(self.diamond_p3.toSympyPoint(), self.diamond_p4.toSympyPoint())
        self.diamond_beta = N(deg(line12.angle_between(line34)))

        self.diamond_d1 = CalcUtil.calcDistanceBetween(self.diamond_p2, self.diamond_p3)
        self.diamond_d2 = CalcUtil.calcDistanceBetween(self.diamond_p1, self.diamond_p4)

    def convertThreeValuesToFourPoints(self):
        pass

    def calcAbrichtAngleDeg(self):
        line12 = Line(self.diamond_p1.toSympyPoint(), self.diamond_p2.toSympyPoint())
        line23 = Line(self.diamond_p2.toSympyPoint(), self.diamond_p3.toSympyPoint())
        return N(deg(line12.angle_between(line23)))

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
