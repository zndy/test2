#!/usr/bin/python3
from mycode.entity.MyPoint import *
from mycode.gui.AbrichtPositionCalculator import AbrichtenPositionCalculator


class IsoGenerator:

    @staticmethod
    def generate(formelx, formely, myPoints):
        iso = ""
        for i in range(len(myPoints)):
            if i % 2 == 0:
                iso += "G0"
            else:
                iso += "G1"
            x = IsoGenerator.calcFormel(formelx, myPoints[i])
            y = IsoGenerator.calcFormel(formely, myPoints[i])
            iso += "X:" + str(x) + " " + "Y:" + str(y) + "\n"
        return iso

    @staticmethod
    def calcFormel(formel, myPoint):
        return formel.subs(
            {AbrichtenPositionCalculator.px: myPoint.getX(), AbrichtenPositionCalculator.py: myPoint.getY()})
