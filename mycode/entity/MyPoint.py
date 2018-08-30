#!/usr/bin/python3
from sympy import *


class MyPoint:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "MyPoint(" + str(self.__x) + ", " + str(self.__y) + ")"

    def setXY(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def setX(self, x):
        self.__x = x

    def getY(self):
        return self.__y

    def setY(self, y):
        self.__y = y

    def toMatrix(self):
        return Matrix([self.__x, self.__y, 1])

    def toSympyPoint(self):
        return Point(self.__x, self.__y)

    def calcDistance(self, other):
        return sqrt((self.__x - other.getX()) ** 2 + (self.__y - other.getY()) ** 2)
