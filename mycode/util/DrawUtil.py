#!/usr/bin/python3
from tkinter import *


class DrawUtil:
    @staticmethod
    def drawCicle(x, y, r, canvas=Canvas):
        return canvas.create_oval(x - r, y - r, x + r, y + r)
