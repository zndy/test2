#!/usr/bin/python3
from mycode.gui.BeanFactory import *


def test1():
    print(BeanFactory.getDiamondPointsPageModel())
    print(BeanFactory.getDiamondPointsPageModel())
    print(BeanFactory.getMainPageModel())
    print(BeanFactory.getMainPageModel())


def main():
    test1()


if __name__ == '__main__':
    main()
