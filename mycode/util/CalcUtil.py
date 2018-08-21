#!/usr/bin/python3
from mycode.entity.MyPoint import *
from sympy import *


class CalcUtil:

    @staticmethod
    def calcSpaceBetween(p1=MyPoint, p2=MyPoint):
        return sqrt(pow(p1.getX() - p2.getX(), 2) + pow(p1.getY() - p2.getY(), 2))


def main():
    print(CalcUtil.calcSpaceBetween(MyPoint(1, 0), MyPoint(2, 4)))


if __name__ == '__main__':
    main()
