#!/usr/bin/python3
import unittest
from mycode.util.CalcUtil import *


class MyPointTest(unittest.TestCase):

    def test_calcDistance1(self):
        p1 = MyPoint(1, 1)
        p2 = MyPoint(4, 1)
        self.assertEqual(3, p1.calcDistance(p2))

    def test_calcDistance2(self):
        x1, x2, y1, y2 = symbols('x1,x2,y1,y2')
        p1 = MyPoint(x1, y1)
        p2 = MyPoint(x2, y2)

        expect = "((x1 - x2)**2 + (y1 - y2)**2)**0.5"
        self.assertEqual(expect, str(p1.calcDistance(p2).evalf()))

    def test_calcDistance3(self):
        x1, x2, y1, y2 = symbols('x1,x2,y1,y2')
        p1 = MyPoint(x1, y1)
        p2 = MyPoint(x2, y2)
        f = CalcUtil.calcDistanceBetween(p1, p2)
        self.assertEqual(3, f.subs({x1: 1, y1: 1, x2: 4, y2: 1}))

    def test_calcAbrichtPoint(self):
        p1 = MyPoint(1, 1)
        p2 = MyPoint(1, 4)
        expect = MyPoint(1, -9)
        self.assertEqual(expect, CalcUtil.calcAbrichtPoint(p1, p2, 10))
