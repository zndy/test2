#!/usr/bin/python3
from mycode.gui.BeanFactory import *


def test1():
    print(BeanFactory.getInstance().mainPageModel)


def main():
    test1()


if __name__ == '__main__':
    main()
