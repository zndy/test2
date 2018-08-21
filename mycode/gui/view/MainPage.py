#!/usr/bin/python3
from tkinter import *


class MainPage(Frame):
    def __init__(self):
        # abricht scheibe value
        self.abricht_p1x = IntVar()
        self.abricht_p1y = IntVar()
        self.abricht_p2x = IntVar()
        self.abricht_p2y = IntVar()
        self.distance = StringVar()

        # diamond scheibe value
        self.diamond_p1x = IntVar()
        self.diamond_p1y = IntVar()
        self.diamond_p2x = IntVar()
        self.diamond_p2y = IntVar()
        self.diamond_p3x = IntVar()
        self.diamond_p3y = IntVar()
        self.diamond_p4x = IntVar()
        self.diamond_p4y = IntVar()

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
        self.abrichtScheibeFrame = Frame("")
        self.abrichtScheibeFrame.grid(row=self.row, column=0, columnspan=7)

        self.__createEmptyRow()

        self.row += 1
        self.diamondScheibeFrame = Frame("")
        self.diamondScheibeFrame.grid(row=self.row, column=0, columnspan=5)

        self.__createEmptyRow()

        self.row += 1
        self.calcButton = Button(text="calc", bg="yellow", fg="red")
        self.calcButton.grid(row=self.row, column=0)

        self.__createAbrichtScheibeFrame()
        self.__createDiamondScheibeFrame()

    def __createEmptyRow(self):
        self.row += 1
        Label().grid(row=self.row, column=0)

    def __createAbrichtScheibeFrame(self):
        row = 0
        Label(self.abrichtScheibeFrame, text='Abricht Scheibe: ').grid(row=row, column=0, columnspan=1)
        row += 1
        self.__createEntry(self.abrichtScheibeFrame, "Abricht P1", row, self.abricht_p1x, self.abricht_p1y)
        Label(self.abrichtScheibeFrame, text="distance: ").grid(row=row, column=5, rowspan=2)
        Label(self.abrichtScheibeFrame, textvariable=self.distance).grid(row=row, column=6, rowspan=2)
        row += 1
        self.__createEntry(self.abrichtScheibeFrame, "Abricht P2", row, self.abricht_p2x, self.abricht_p2y)

    def __createDiamondScheibeFrame(self):
        row = 0
        Label(self.diamondScheibeFrame, text='Diamond Scheibe: ').grid(row=row, column=0, columnspan=1)
        row += 1
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P1", row, self.diamond_p1x, self.diamond_p1y)
        row += 1
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P2", row, self.diamond_p2x, self.diamond_p2y)
        row += 1
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P3", row, self.diamond_p3x, self.diamond_p3y)
        row += 1
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P4", row, self.diamond_p4x, self.diamond_p4y)

    def __createEntry(self, frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1)
        Entry(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1)
        Entry(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1)

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
