#!/usr/bin/python3
from tkinter import *
from mycode.entity.MyPoint import *
from mycode.util.MatrixUtil import *


class DrawUtil:
    @staticmethod
    def drawCicle(x, y, r, canvas=Canvas):
        canvas.create_oval(x - r, y - r, x + r, y + r)

    @staticmethod
    def drawAxis(x, y, r, color, angle, canvas=Canvas):
        horizontalP1 = MyPoint(x - r, y).toMatrix()
        horizontalP2 = MyPoint(x + r, y).toMatrix()
        verticalP1 = MyPoint(x, y + r).toMatrix()
        verticalP2 = MyPoint(x, y - r).toMatrix()

        horizontalP1 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * horizontalP1
        horizontalP2 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * horizontalP2
        verticalP1 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * verticalP1
        verticalP2 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * verticalP2

        canvas.create_line(N(horizontalP1[0]), N(horizontalP1[1]), N(horizontalP2[0]), N(horizontalP2[1]), fill=color,
                           dash=(4, 4))
        canvas.create_line(N(verticalP1[0]), N(verticalP1[1]), N(verticalP2[0]), N(verticalP2[1]), fill=color,
                           dash=(4, 4))
