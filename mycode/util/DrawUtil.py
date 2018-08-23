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
        horizontalP1 = MyPoint(x - r, y)
        horizontalP2 = MyPoint(x + r, y)
        verticalP1 = MyPoint(x, y - r)
        verticalP2 = MyPoint(x, y + r)
        charxPos = MyPoint(horizontalP2.getX() + 10, horizontalP2.getY())
        charyPos = MyPoint(verticalP1.getX(), verticalP1.getY() - 10)

        horizontalP1 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * horizontalP1.toMatrix()
        horizontalP2 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * horizontalP2.toMatrix()
        verticalP1 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * verticalP1.toMatrix()
        verticalP2 = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * verticalP2.toMatrix()
        charxPos = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * charxPos.toMatrix()
        charyPos = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y) * charyPos.toMatrix()

        canvas.create_line(N(horizontalP1[0]), N(horizontalP1[1]), N(horizontalP2[0]), N(horizontalP2[1]), fill=color,
                           dash=(4, 4))
        canvas.create_line(N(verticalP1[0]), N(verticalP1[1]), N(verticalP2[0]), N(verticalP2[1]), fill=color,
                           dash=(4, 4))
        canvas.create_text(N(charxPos[0]), N(charxPos[1]), fill="red", font="Times 10 italic bold", text="x")
        canvas.create_text(N(charyPos[0]), N(charyPos[1]), fill="red", font="Times 10 italic bold", text="y")
