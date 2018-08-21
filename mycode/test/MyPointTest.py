#!/usr/bin/python3
from mycode.entity.MyPoint import *


def main():
    p1 = MyPoint(1, 0)
    p2 = MyPoint(2, 4)
    print(p1.getSpace(p2))


if __name__ == '__main__':
    main()
