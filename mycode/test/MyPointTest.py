#!/usr/bin/python3
from mycode.entity.MyPoint import *
from mycode.util.CalcUtil import *


def test1():
    p1 = MyPoint(1, 0)
    p2 = MyPoint(2, 4)
    print(p1.getSpace(p2))
    print(N(p1.getSpace(p2)))

def test2():
    x1,x2,y1,y2 = symbols('x1,x2,y1,y2')
    p1 = MyPoint(x1,y1)
    p2 = MyPoint(x2,y2)
    print(p1.getSpace(p2))
    print(N(p1.getSpace(p2)))

def test3():
    x1, x2, y1, y2 = symbols('x1,x2,y1,y2')
    p1 = MyPoint(x1, y1)
    p2 = MyPoint(x2, y2)
    f = CalcUtil.calcSpaceBetween(p1, p2)
    print(f)
    print(N(f))
    print(f.subs({x1:1, y1:0, x2:2, y2:4}))
    print(N(f.subs({x1:1, y1:0, x2:2, y2:4})))

def main():
    test1()
    test2()
    test3()

if __name__ == '__main__':
    main()
