#!/usr/bin/python3
from tkinter import *


class MainPage(Frame):
    def __init__(self):
        self.abrichtScheibeFrame = Frame("")
        self.abrichtScheibeFrame.grid(row=0, column=0)
        self.diamondScheibeFrame = Frame("")
        self.diamondScheibeFrame.grid(row=1, column=0)

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

        Label().grid(row=2, column=0, columnspan=1)  # empty row
        self.calcButton = Button(text="calc", bg="yellow", fg="red")
        self.calcButton.grid(row=3, column=0)

        self.__createAbrichtScheibeFrame()
        self.__createDiamondScheibeFrame()

    def __createAbrichtScheibeFrame(self):
        Label(self.abrichtScheibeFrame, text='Abricht Scheibe: ').grid(row=0, column=0, columnspan=1)
        self.__createEntry(self.abrichtScheibeFrame, "Abricht P1", 1, self.abricht_p1x, self.abricht_p1y)
        self.__createEntry(self.abrichtScheibeFrame, "Abricht P2", 2, self.abricht_p2x, self.abricht_p2y)

        Label(self.abrichtScheibeFrame, textvariable=self.distance).grid(row=3, column=0, columnspan=1)

    def __createDiamondScheibeFrame(self):
        Label(self.diamondScheibeFrame, text='Diamond Scheibe: ').grid(row=0, column=0, columnspan=1)
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P1", 1, self.diamond_p1x, self.diamond_p1y)
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P2", 2, self.diamond_p2x, self.diamond_p2y)
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P3", 3, self.diamond_p3x, self.diamond_p3y)
        self.__createEntry(self.diamondScheibeFrame, "DiamondScheibe P4", 4, self.diamond_p4x, self.diamond_p4y)

    def __createEntry(self, frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1)
        Entry(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1)
        Entry(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1)

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
