#!/usr/bin/python3
from tkinter import *


class MainPage(Frame):
    def __init__(self):
        self.inputValueFrame = Frame("")
        self.inputValueFrame.grid(row=0, column=0)

        self.abricht_p1x = IntVar()
        self.abricht_p1y = IntVar()
        self.abricht_p2x = IntVar()
        self.abricht_p2y = IntVar()

        self.result = StringVar()

        self.calcButton = Button(self.inputValueFrame, text="calc", bg="yellow", fg="red")
        self.__createInputValueFrame()

    def __createInputValueFrame(self):
        Label(self.inputValueFrame, text='Abricht Scheibe: ').grid(row=0, column=0, columnspan=1)

        Label(self.inputValueFrame, text='Abricht P1: ').grid(row=1, column=0, columnspan=1)
        Label(self.inputValueFrame, text='x:').grid(row=1, column=1, columnspan=1)
        Entry(self.inputValueFrame, textvariable=self.abricht_p1x).grid(row=1, column=2, columnspan=1)
        Label(self.inputValueFrame, text='y:').grid(row=1, column=3, columnspan=1)
        Entry(self.inputValueFrame, textvariable=self.abricht_p1y).grid(row=1, column=4, columnspan=1)

        Label(self.inputValueFrame, text='Abricht P2: ').grid(row=2, column=0, columnspan=1)
        Label(self.inputValueFrame, text='x:').grid(row=2, column=1, columnspan=1)
        Entry(self.inputValueFrame, textvariable=self.abricht_p2x).grid(row=2, column=2, columnspan=1)
        Label(self.inputValueFrame, text='y:').grid(row=2, column=3, columnspan=1)
        Entry(self.inputValueFrame, textvariable=self.abricht_p2y).grid(row=2, column=4, columnspan=1)

        Label(self.inputValueFrame, textvariable=self.result).grid(row=3, column=0, columnspan=1)

        self.calcButton.grid(row=10, column=0)

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
