#!/usr/bin/python3
from mycode.util.WindowUtil import *


class DiamondPointsPage(Frame):
    def __init__(self, window):
        self.window = window

        self.padding = 15

        self.abrichtScheibeWidth = DoubleVar()
        self.abrichtAngle = DoubleVar()

        # diamond points value
        self.diamond_a1x = DoubleVar()
        self.diamond_a1y = DoubleVar()
        self.diamond_a2x = DoubleVar()
        self.diamond_a2y = DoubleVar()
        self.diamond_b1x = DoubleVar()
        self.diamond_b1y = DoubleVar()
        self.diamond_b2x = DoubleVar()
        self.diamond_b2y = DoubleVar()
        self.diamond_c1x = DoubleVar()
        self.diamond_c1y = DoubleVar()
        self.diamond_c2x = DoubleVar()
        self.diamond_c2y = DoubleVar()

        # result
        self.xResult = StringVar()
        self.yResult = StringVar()

        self.isoText = Text

        # callback example
        # self.isoStr = StringVar()
        # self.isoStr.trace("w", self.updateIsoFrame)

        self.row = 0
        self.abrichtScheibeFrame = self.__createAbrichtenScheibeFrame()
        self.abrichtScheibeFrame.grid(row=self.row, column=0, columnspan=2, pady=self.padding)

        self.row += 1
        self.diamondPointFrame = self.__createDiamondPointFrame()
        self.diamondPointFrame.grid(row=self.row, column=0, columnspan=5, pady=self.padding)

        self.row += 1
        self.resultFrame = self.__createResultFrame()
        self.resultFrame.grid(row=self.row, column=0, columnspan=2, sticky=W, pady=self.padding)

        self.row += 1
        self.isoFrame = self.__createIsoFrame()
        self.isoFrame.grid(row=self.row, column=0, columnspan=11, sticky=W, pady=self.padding)

    def __createAbrichtenScheibeFrame(self):
        abrichtScheibeFrame = Frame(self.window)
        row = 0
        Label(abrichtScheibeFrame, text="Abrichten Scheibe Width: ").grid(row=row, column=0, columnspan=1, sticky=W)
        Label(abrichtScheibeFrame, textvariable=self.abrichtScheibeWidth).grid(row=row, column=1, columnspan=1)
        row += 1
        Label(abrichtScheibeFrame, text="Abrichten Angle: ").grid(row=row, column=0, columnspan=1, sticky=W)
        Label(abrichtScheibeFrame, textvariable=self.abrichtAngle).grid(row=row, column=1, columnspan=1)
        return abrichtScheibeFrame

    def __createDiamondPointFrame(self):
        diamondPointFrame = Frame(self.window)
        row = 0
        Label(diamondPointFrame, text='Diamond Points: ').grid(row=row, column=0, sticky=W)
        row += 1
        self.__createPointResultEntry(diamondPointFrame, "Diamond Point A1", row, self.diamond_a1x, self.diamond_a1y)
        row += 1
        self.__createPointResultEntry(diamondPointFrame, "Diamond Point A2", row, self.diamond_a2x, self.diamond_a2y)
        row += 1
        self.__createPointResultEntry(diamondPointFrame, "Diamond Point B1", row, self.diamond_b1x, self.diamond_b1y)
        row += 1
        self.__createPointResultEntry(diamondPointFrame, "Diamond Point B2", row, self.diamond_b2x, self.diamond_b2y)
        row += 1
        self.__createPointResultEntry(diamondPointFrame, "Diamond Point C1", row, self.diamond_c1x, self.diamond_c1y)
        row += 1
        self.__createPointResultEntry(diamondPointFrame, "Diamond Point C2", row, self.diamond_c2x, self.diamond_c2y)
        return diamondPointFrame

    def __createResultFrame(self):
        resultFrame = Frame(self.window)
        row = 0
        Label(resultFrame, text='result: ').grid(row=row, column=0, sticky=W)
        row += 1
        self.__createResultEntry(resultFrame, "x", row, self.xResult)
        row += 1
        self.__createResultEntry(resultFrame, "y", row, self.yResult)
        return resultFrame

    def __createIsoFrame(self):
        isoFrame = Frame(self.window)
        row = 0
        Label(isoFrame, text='ISO: (copy text with right mouse click)').grid(row=row, column=0, sticky=W)
        row += 1
        self.isoText = Text(isoFrame, height=20, width=80)
        self.isoText.grid(row=row, column=0, sticky=W)
        self.isoText.bind("<Button-3>", WindowUtil.copyTextToClipboard)
        WindowUtil.disableFrame(isoFrame)
        return isoFrame

    def __createPointResultEntry(self, frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1, padx=(0, self.padding), sticky=W)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1, sticky=W)
        Label(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1, sticky=W)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1, padx=(self.padding, 0), sticky=W)
        Label(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1, sticky=W)

    def __createResultEntry(self, frame, name, row, entry):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1, sticky=W)
        Label(frame, textvariable=entry).grid(row=row, column=1, columnspan=1, sticky=W)

    def updateIsoFrame(self, *args):
        WindowUtil.enableFrame(self.isoFrame)
        self.isoText.insert(INSERT, self.isoStr.get())
        WindowUtil.disableFrame(self.isoFrame)
