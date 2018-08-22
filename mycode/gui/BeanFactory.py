#!/usr/bin/python3
from mycode.gui.model.MainPageModel import *
from mycode.gui.model.DiamondPointsPageModel import *


class BeanFactory:
    def __init__(self):
        self.mainPageModel = MainPageModel()
        self.diamondPointsPageModel = DiamondPointsPageModel()

beanFactory = BeanFactory()