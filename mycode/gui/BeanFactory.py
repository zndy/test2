#!/usr/bin/python3
from mycode.gui.model.MainPageModel import *
from mycode.gui.model.DiamondPointsPageModel import *


class BeanFactory:
    __instance = None

    def __init__(self):
        self.mainPageModel = MainPageModel()
        self.diamondPointsPageModel = DiamondPointsPageModel()

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = BeanFactory()
        return cls.__instance
