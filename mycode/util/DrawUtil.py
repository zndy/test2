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
        axisxP1 = MyPoint(x - r, y)
        axisxP2 = MyPoint(x + r, y)
        axisyP1 = MyPoint(x, y - r)
        axisyP2 = MyPoint(x, y + r)

        arrowxP1 = MyPoint(axisxP2.getX() - 5, axisxP2.getY() - 5)
        arrowxP2 = MyPoint(axisxP2.getX() - 5, axisxP2.getY() + 5)
        arrowyP1 = MyPoint(axisyP1.getX() - 5, axisyP1.getY() + 5)
        arrowyP2 = MyPoint(axisyP1.getX() + 5, axisyP1.getY() + 5)

        charxPos = MyPoint(axisxP2.getX() + 10, axisxP2.getY())
        charyPos = MyPoint(axisyP1.getX(), axisyP1.getY() - 10)

        rotationMatrix = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y)

        axisxP1 = rotationMatrix * axisxP1.toMatrix()
        axisxP2 = rotationMatrix * axisxP2.toMatrix()
        axisyP1 = rotationMatrix * axisyP1.toMatrix()
        axisyP2 = rotationMatrix * axisyP2.toMatrix()

        arrowxP1 = rotationMatrix * arrowxP1.toMatrix()
        arrowxP2 = rotationMatrix * arrowxP2.toMatrix()
        arrowyP1 = rotationMatrix * arrowyP1.toMatrix()
        arrowyP2 = rotationMatrix * arrowyP2.toMatrix()

        charxPos = rotationMatrix * charxPos.toMatrix()
        charyPos = rotationMatrix * charyPos.toMatrix()

        canvas.create_line(N(axisxP1[0]), N(axisxP1[1]), N(axisxP2[0]), N(axisxP2[1]), fill=color,
                           dash=(1, 1))
        canvas.create_line(N(axisyP1[0]), N(axisyP1[1]), N(axisyP2[0]), N(axisyP2[1]), fill=color,
                           dash=(1, 1))

        canvas.create_line(N(arrowxP1[0]), N(arrowxP1[1]), N(axisxP2[0]), N(axisxP2[1]), fill=color)
        canvas.create_line(N(arrowxP2[0]), N(arrowxP2[1]), N(axisxP2[0]), N(axisxP2[1]), fill=color)
        canvas.create_line(N(arrowyP1[0]), N(arrowyP1[1]), N(axisyP1[0]), N(axisyP1[1]), fill=color)
        canvas.create_line(N(arrowyP2[0]), N(arrowyP2[1]), N(axisyP1[0]), N(axisyP1[1]), fill=color)

        canvas.create_text(N(charxPos[0]), N(charxPos[1]), fill="red", font="Times 10 italic bold", text="x")
        canvas.create_text(N(charyPos[0]), N(charyPos[1]), fill="red", font="Times 10 italic bold", text="y")
