#!/usr/bin/python3
from tkinter import font
from mycode.util.DrawUtil import *
from mycode.util.WindowUtil import *


class MainPage(Frame):
    def __init__(self, window):
        self.window = window

        self.convertButtonText = StringVar()
        self.diamondFrameSelectNr = IntVar()  # Nr 1: 3 values, Nr 2: 4 points

        # abricht scheibe value
        self.abricht_p1x = DoubleVar()
        self.abricht_p1y = DoubleVar()
        self.abricht_p2x = DoubleVar()
        self.abricht_p2y = DoubleVar()

        # diamond scheibe value
        self.diamond_p1x = DoubleVar()
        self.diamond_p1y = DoubleVar()
        self.diamond_p2x = DoubleVar()
        self.diamond_p2y = DoubleVar()
        self.diamond_p3x = DoubleVar()
        self.diamond_p3y = DoubleVar()
        self.diamond_p4x = DoubleVar()
        self.diamond_p4y = DoubleVar()

        # paras
        self.beginDistance = DoubleVar()
        self.abricht_flansch = DoubleVar()
        self.diamond_flansch = DoubleVar()
        self.deltax = DoubleVar()
        self.deltay = DoubleVar()
        self.abricht_diameter = DoubleVar()
        self.diamond_diameter = DoubleVar()

        # Frames
        # self.canvasFrame = Frame(self.window)
        # self.__createCanvasFrame()
        # self.canvasFrame.place(x=200, y=20)
        #

        # self.diamondScheibeFrame = Frame(self.window)
        # self.__createDiamondScheibeFrame()
        # self.diamondScheibeFrame.place(x=0, y=20)

        self.diamondScheibeFrame = self.__createDiamondScheibeFrame()
        self.diamondScheibeFrame.place(x=0, y=10)

        self.abrichtScheibeFrame = self.__createAbrichtScheibeFrame()
        self.abrichtScheibeFrame.place(x=25, y=400)

        self.paraFrame = self.__createParaFrame()
        self.paraFrame.place(x=550, y=450)

        #
        # self.paraFrame = Frame(self.window)
        # self.__createParaFrame()
        # self.paraFrame.place(x=450, y=250)

        self.onClick()

        self.calcButton = Button(text="calc")
        WindowUtil.setDefaultButtonStyle(self.calcButton)
        self.calcButton.place(x=800, y=650)

    def __createDiamondScheibeFrame(self):
        diamondScheibeFrame = Frame(self.window)
        row = 0
        Label(diamondScheibeFrame, text='Diamond Scheibe: (Bitte waehlen Sie gewuenscht input values variant)').grid(
            row=row, sticky=W)

        row += 1
        self.__createThreeValueFrame(diamondScheibeFrame).grid(row=row, column=0)

        convertBtn = Button(diamondScheibeFrame, textvariable=self.convertButtonText)
        WindowUtil.setDefaultButtonStyle(convertBtn)
        convertBtn.grid(row=row, column=1, padx=20)

        self.__createFourPointFrame(diamondScheibeFrame).grid(row=row, column=2)

        return diamondScheibeFrame

    def __createThreeValueFrame(self, master=Frame):
        threeValueFrame = Frame(master)
        row = 0
        threeValuesRadioBtn = Radiobutton(threeValueFrame, text="Three Values Version",
                                          variable=self.diamondFrameSelectNr, value=1,
                                          command=self.onClick)
        threeValuesRadioBtn.grid(row=row, column=0)
        threeValuesRadioBtn.select()

        # row += 1
        self.__createFourPointCanvasFrame(threeValueFrame).grid(row=row, column=1)
        row += 1
        self.__createFourPointInputFrame(threeValueFrame).grid(row=row, column=0, columnspan=2)
        return threeValueFrame

    def __createFourPointFrame(self, master=Frame):
        fourPointFrame = Frame(master)
        row = 0
        fourPointsRadioBtn = Radiobutton(fourPointFrame, text="Four Points Version", variable=self.diamondFrameSelectNr,
                                         value=2,
                                         command=self.onClick)
        fourPointsRadioBtn.grid(row=row, column=0)
        # row += 1
        self.__createFourPointCanvasFrame(fourPointFrame).grid(row=row, column=1)
        row += 1
        self.__createFourPointInputFrame(fourPointFrame).grid(row=row, column=0, columnspan=2)
        return fourPointFrame

    def __createFourPointCanvasFrame(self, master=Frame):
        fourPointCanvasFrame = Frame(master)
        canvas = Canvas(fourPointCanvasFrame, width=200, height=200)
        canvas.grid(row=0, column=1, columnspan=1)
        p1x = p4x = 100
        p1y = p6y = 120
        p2x = p3x = 80
        p2y = 100
        p3y = 60
        p4y = p5y = 40
        p5x = p6x = 200
        radius = 3
        # canvas.create_text(50, 10, fill="darkblue", font="Times 10 italic bold", text="Diamond Scheibe")
        canvas.create_polygon(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, outline="black", fill="")
        DrawUtil.drawCicle(p1x, p1y, radius, canvas)
        canvas.create_text(p1x - 20, p1y, fill="darkblue", font="Times 10 italic bold", text="p1")
        DrawUtil.drawCicle(p2x, p2y, radius, canvas)
        canvas.create_text(p2x - 20, p2y, fill="darkblue", font="Times 10 italic bold", text="p2")
        DrawUtil.drawCicle(p3x, p3y, radius, canvas)
        canvas.create_text(p3x - 20, p3y, fill="darkblue", font="Times 10 italic bold", text="p3")
        DrawUtil.drawCicle(p4x, p4y, radius, canvas)
        canvas.create_text(p4x - 20, p4y, fill="darkblue", font="Times 10 italic bold", text="p4")

        axisX = p2x
        axisY = p3y + (p2y - p3y) / 2
        DrawUtil.drawAxis(axisX, axisY, 51, "red", 270, canvas)
        return fourPointCanvasFrame

    def __createFourPointInputFrame(self, master=Frame):
        fourPointInputFrame = Frame(master)
        row = 0
        WindowUtil.createPointInputEntry(fourPointInputFrame, "DiamondScheibe P1", row, self.diamond_p1x,
                                         self.diamond_p1y)
        row += 1
        WindowUtil.createPointInputEntry(fourPointInputFrame, "DiamondScheibe P2", row, self.diamond_p2x,
                                         self.diamond_p2y)
        row += 1
        WindowUtil.createPointInputEntry(fourPointInputFrame, "DiamondScheibe P3", row, self.diamond_p3x,
                                         self.diamond_p3y)
        row += 1
        WindowUtil.createPointInputEntry(fourPointInputFrame, "DiamondScheibe P4", row, self.diamond_p4x,
                                         self.diamond_p4y)
        return fourPointInputFrame

    def onClick(self):
        if self.diamondFrameSelectNr.get() == 1:
            self.convertButtonText.set("==>")
        else:
            self.convertButtonText.set("<==")
        print(self.diamondFrameSelectNr.get())

    def __drawDiamondScheibe(self):
        canvas = Canvas(self.canvasFrame, width=200, height=200)
        canvas.grid(row=0, column=1, columnspan=1)
        p1x = p4x = 100
        p1y = p6y = 120
        p2x = p3x = 80
        p2y = 100
        p3y = 60
        p4y = p5y = 40
        p5x = p6x = 200
        radius = 3
        canvas.create_text(50, 10, fill="darkblue", font="Times 10 italic bold", text="Diamond Scheibe")
        canvas.create_polygon(p1x, p1y, p2x, p2y, p3x, p3y, p4x, p4y, p5x, p5y, p6x, p6y, outline="black", fill="")
        DrawUtil.drawCicle(p1x, p1y, radius, canvas)
        canvas.create_text(p1x - 20, p1y, fill="darkblue", font="Times 10 italic bold", text="p1")
        DrawUtil.drawCicle(p2x, p2y, radius, canvas)
        canvas.create_text(p2x - 20, p2y, fill="darkblue", font="Times 10 italic bold", text="p2")
        DrawUtil.drawCicle(p3x, p3y, radius, canvas)
        canvas.create_text(p3x - 20, p3y, fill="darkblue", font="Times 10 italic bold", text="p3")
        DrawUtil.drawCicle(p4x, p4y, radius, canvas)
        canvas.create_text(p4x - 20, p4y, fill="darkblue", font="Times 10 italic bold", text="p4")

        axisX = p2x
        axisY = p3y + (p2y - p3y) / 2
        DrawUtil.drawAxis(axisX, axisY, 51, "red", 270, canvas)

    def ___createDiamondScheibeFrame(self):
        row = 0
        Label(self.diamondScheibeFrame, text='Diamond Scheibe: ').grid(row=row)
        row += 1
        WindowUtil.createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P1", row, self.diamond_p1x,
                                         self.diamond_p1y)
        row += 1
        WindowUtil.createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P2", row, self.diamond_p2x,
                                         self.diamond_p2y)
        row += 1
        WindowUtil.createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P3", row, self.diamond_p3x,
                                         self.diamond_p3y)
        row += 1
        WindowUtil.createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P4", row, self.diamond_p4x,
                                         self.diamond_p4y)

    def __createAbrichtScheibeFrame(self):
        abrichtScheibeFrame = Frame(self.window)
        self.__createAbrichtCanvasFrame(abrichtScheibeFrame)
        self.__createAbrichtInputFrame(abrichtScheibeFrame)
        return abrichtScheibeFrame

    def __createAbrichtCanvasFrame(self, master=Frame):
        abrichtCanvasFrame = Frame(master)
        abrichtCanvasFrame.pack()
        canvas = Canvas(abrichtCanvasFrame, width=200, height=180)
        canvas.pack()
        width = 40
        height = 80
        p1x = 70
        p1y = p2y = 90
        p2x = p3x = p1x + width
        p3y = p2y + height
        radius = 3
        canvas.create_text(90, 10, fill="darkblue", font="Times 10 italic bold", text="Abricht Scheibe")
        canvas.create_rectangle(p1x, p1y, p3x, p3y)
        DrawUtil.drawCicle(p1x, p1y, radius, canvas)
        canvas.create_text(p1x, p1y - 10, fill="darkblue", font="Times 10 italic bold", text="p1")
        DrawUtil.drawCicle(p2x, p2y, radius, canvas)
        canvas.create_text(p2x, p2y - 10, fill="darkblue", font="Times 10 italic bold", text="p2")

        axisX = p1x + (p2x - p1x) / 2
        axisY = p1y
        DrawUtil.drawAxis(axisX, axisY, 51, "red", 0, canvas)

    def __createAbrichtInputFrame(self, master=Frame):
        inputFrame = Frame(master)
        inputFrame.pack(side=BOTTOM)
        row = 0
        WindowUtil.createPointInputEntry(inputFrame, "Abricht P1", row, self.abricht_p1x,
                                         self.abricht_p1y)
        row += 1
        WindowUtil.createPointInputEntry(inputFrame, "Abricht P2", row, self.abricht_p2x,
                                         self.abricht_p2y)

    def __createParaFrame(self):
        paraFrame = Frame(self.window)
        row = 0
        Label(paraFrame, text='Parameters: ').grid(row=row)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "Anfang Abstand", row, self.beginDistance)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "AbrichtScheibe Flansch", row, self.abricht_flansch)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "DiamondScheibe Flansch", row, self.diamond_flansch)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "Delta X", row, self.deltax)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "Delta Y", row, self.deltay)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "AbrichtScheibe Durchmesser", row, self.abricht_diameter)
        row += 1
        WindowUtil.createInputEntry(paraFrame, "DiamondScheibe Durchmesser", row, self.diamond_diameter)
        return paraFrame

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
