#!/usr/bin/python3
from mycode.entity.MyPoint import *


class DiamondPointsPageModel:
    def __init__(self):
        self.abrichtScheibeWidth = 0.0
        self.abrichtAngleDeg = 0.0

        self.diamondPointA1 = MyPoint
        self.diamondPointA2 = MyPoint
        self.diamondPointB1 = MyPoint
        self.diamondPointB2 = MyPoint
        self.diamondPointC1 = MyPoint
        self.diamondPointC2 = MyPoint

        self.xResult = Add
        self.yResult = Add

        self.iso = "iso"+"\n"+"iso"
