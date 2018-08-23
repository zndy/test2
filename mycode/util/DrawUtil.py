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

        arrowxPos1 = MyPoint(horizontalP2.getX() - 5, horizontalP2.getY() - 5)
        arrowxPos2 = MyPoint(horizontalP2.getX() - 5, horizontalP2.getY() + 5)
        arrowyPos1 = MyPoint(verticalP1.getX() - 5, verticalP1.getY() + 5)
        arrowyPos2 = MyPoint(verticalP1.getX() + 5, verticalP1.getY() + 5)

        charxPos = MyPoint(horizontalP2.getX() + 10, horizontalP2.getY())
        charyPos = MyPoint(verticalP1.getX(), verticalP1.getY() - 10)

        rotationMatrix = MatrixUtil.translationMatrix2D(x, y) * MatrixUtil.rotationMatrix2D(
            angle) * MatrixUtil.translationMatrix2D(-x, -y)

        horizontalP1 = rotationMatrix * horizontalP1.toMatrix()
        horizontalP2 = rotationMatrix * horizontalP2.toMatrix()
        verticalP1 = rotationMatrix * verticalP1.toMatrix()
        verticalP2 = rotationMatrix * verticalP2.toMatrix()

        arrowxPos1 = rotationMatrix*arrowxPos1.toMatrix()
        arrowxPos2 = rotationMatrix*arrowxPos2.toMatrix()
        arrowyPos1 = rotationMatrix*arrowyPos1.toMatrix()
        arrowyPos2 = rotationMatrix*arrowyPos2.toMatrix()

        charxPos = rotationMatrix * charxPos.toMatrix()
        charyPos = rotationMatrix * charyPos.toMatrix()

        canvas.create_line(N(horizontalP1[0]), N(horizontalP1[1]), N(horizontalP2[0]), N(horizontalP2[1]), fill=color,
                           dash=(1, 1))
        canvas.create_line(N(verticalP1[0]), N(verticalP1[1]), N(verticalP2[0]), N(verticalP2[1]), fill=color,
                           dash=(1, 1))

        canvas.create_line(N(arrowxPos1[0]), N(arrowxPos1[1]), N(horizontalP2[0]), N(horizontalP2[1]), fill=color)
        canvas.create_line(N(arrowxPos2[0]), N(arrowxPos2[1]), N(horizontalP2[0]), N(horizontalP2[1]), fill=color)
        canvas.create_line(N(arrowyPos1[0]), N(arrowyPos1[1]), N(verticalP1[0]), N(verticalP1[1]), fill=color)
        canvas.create_line(N(arrowyPos2[0]), N(arrowyPos2[1]), N(verticalP1[0]), N(verticalP1[1]), fill=color)

        canvas.create_text(N(charxPos[0]), N(charxPos[1]), fill="red", font="Times 10 italic bold", text="x")
        canvas.create_text(N(charyPos[0]), N(charyPos[1]), fill="red", font="Times 10 italic bold", text="y")
