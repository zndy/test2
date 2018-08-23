#!/usr/bin/python3
from tkinter import *


class DiamondPointsPage(Frame):
    def __init__(self, window):
        self.window = window

        self.abrichtScheibeWidth = IntVar()
        self.abrichtAngle = IntVar()

        # diamond points value
        self.diamond_a1x = IntVar()
        self.diamond_a1y = IntVar()
        self.diamond_a2x = IntVar()
        self.diamond_a2y = IntVar()
        self.diamond_b1x = IntVar()
        self.diamond_b1y = IntVar()
        self.diamond_b2x = IntVar()
        self.diamond_b2y = IntVar()
        self.diamond_c1x = IntVar()
        self.diamond_c1y = IntVar()
        self.diamond_c2x = IntVar()
        self.diamond_c2y = IntVar()

        self.row = 0
        self.abrichtScheibeFrame = Frame(self.window)
        self.abrichtScheibeFrame.grid(row=self.row, column=0, columnspan=2)
        self.__createAbrichtenScheibeFrame()

        self.__createEmptyRow(self.window)
        self.row += 1
        self.diamondPointFrame = Frame(self.window)
        self.diamondPointFrame.grid(row=self.row, column=0, columnspan=5)
        self.__createDiamondPointFrame()

    def __createAbrichtenScheibeFrame(self):
        row = 0
        Label(self.abrichtScheibeFrame, text="Abrichten Scheibe Width: ").grid(row=row, column=0, columnspan=1)
        Label(self.abrichtScheibeFrame, textvariable=self.abrichtScheibeWidth).grid(row=row, column=1, columnspan=1)
        row += 1
        Label(self.abrichtScheibeFrame, text="Abrichten Angle: ").grid(row=row, column=0, columnspan=1)
        Label(self.abrichtScheibeFrame, textvariable=self.abrichtAngle).grid(row=row, column=1, columnspan=1)

    def __createDiamondPointFrame(self):
        row = 0
        Label(self.diamondPointFrame, text='Diamond Points: ').grid(row=row, column=0)
        row += 1
        self.__createResultEntry(self.diamondPointFrame, "Diamond Point A1", row, self.diamond_a1x, self.diamond_a1y)
        row += 1
        self.__createResultEntry(self.diamondPointFrame, "Diamond Point A2", row, self.diamond_a2x, self.diamond_a2y)
        row += 1
        self.__createResultEntry(self.diamondPointFrame, "Diamond Point B1", row, self.diamond_b1x, self.diamond_b1y)
        row += 1
        self.__createResultEntry(self.diamondPointFrame, "Diamond Point B2", row, self.diamond_b2x, self.diamond_b2y)
        row += 1
        self.__createResultEntry(self.diamondPointFrame, "Diamond Point C1", row, self.diamond_c1x, self.diamond_c1y)
        row += 1
        self.__createResultEntry(self.diamondPointFrame, "Diamond Point C2", row, self.diamond_c2x, self.diamond_c2y)

    def __createResultEntry(self, frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1)
        Label(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1)
        Label(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1)

    def __createEmptyRow(self, window):
        self.row += 1
        Label(window).grid(row=self.row, column=0)
