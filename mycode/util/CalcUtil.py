#!/usr/bin/python3
from mycode.entity.MyPoint import *
from sympy import *


class CalcUtil:

    @staticmethod
    def calcDistanceBetween(p1, p2):
        return sqrt(pow(p1.getX() - p2.getX(), 2) + pow(p1.getY() - p2.getY(), 2))

    @staticmethod
    def calcLineFuncBy(p1, p2):
        x, y = symbols('x,y')
        return (y - p1.getY()) / (p2.getY() - p1.getY()) - (x - p1.getX()) / (p2.getX() - p1.getX())

    @staticmethod
    def calcAbrichtPoint(near, far, distanceToNear):
        x, y = symbols('x,y')
        abrichtPoint = MyPoint(x, y)
        distanceBetweenNearFar = CalcUtil.calcDistanceBetween(near, far)

        pointToNearFunc = CalcUtil.calcDistanceBetween(abrichtPoint, near) - distanceToNear
        pointToFarFunc = CalcUtil.calcDistanceBetween(abrichtPoint, far) - distanceToNear - distanceBetweenNearFar

        result = solve([pointToNearFunc, pointToFarFunc], [x, y])
        return MyPoint(N(result[0][0]), N(result[0][1]))


def main():
    point1 = MyPoint(1, 1)
    point2 = MyPoint(2, 2)
    # print(CalcUtil.calcDistanceBetween(point1, point2))
    # print(CalcUtil.calcLineFuncBy(point1, point2))
    newPoint = CalcUtil.calcAbrichtPoint(point1, point2, 2)
    print(newPoint)


if __name__ == '__main__':
    main()
