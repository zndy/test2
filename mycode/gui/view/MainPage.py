#!/usr/bin/python3
from mycode.util.DrawUtil import *
from mycode.util.WindowUtil import *


class MainPage(Frame):
    def __init__(self, window):
        self.window = window

        self.convertButtonText = StringVar()
        self.diamondFrameSelectNr = IntVar()  # Nr 1: 3 values, Nr 2: 4 points
        self.threeValuesCanvasFrame = Frame
        self.threeValuesInputFrame = Frame
        self.fourPointsCanvasFrame = Frame
        self.fourPointsInputFrame = Frame
        self.convertBtn = Button

        # diamond scheibe three values
        self.diamond_beta = DoubleVar()
        self.diamond_d1 = DoubleVar()
        self.diamond_d2 = DoubleVar()

        # diamond scheibe four Points
        self.diamond_p1x = DoubleVar()
        self.diamond_p1y = DoubleVar()
        self.diamond_p2x = DoubleVar()
        self.diamond_p2y = DoubleVar()
        self.diamond_p3x = DoubleVar()
        self.diamond_p3y = DoubleVar()
        self.diamond_p4x = DoubleVar()
        self.diamond_p4y = DoubleVar()

        # abricht scheibe value
        self.abricht_p1x = DoubleVar()
        self.abricht_p1y = DoubleVar()
        self.abricht_p2x = DoubleVar()
        self.abricht_p2y = DoubleVar()

        # paras
        self.beginDistance = DoubleVar()
        self.abricht_flansch = DoubleVar()
        self.diamond_flansch = DoubleVar()
        self.deltax = DoubleVar()
        self.deltay = DoubleVar()
        self.abricht_diameter = DoubleVar()
        self.diamond_diameter = DoubleVar()

        # Frames
        self.diamondScheibeFrame = self.__createDiamondScheibeFrame()
        self.diamondScheibeFrame.place(x=10, y=10)

        self.abrichtScheibeFrame = self.__createAbrichtScheibeFrame()
        self.abrichtScheibeFrame.place(x=10, y=400)

        self.paraFrame = self.__createParaFrame()
        self.paraFrame.place(x=550, y=450)

        self.onClick()

        self.calcButton = Button(text="calc")
        WindowUtil.setDefaultButtonStyle(self.calcButton)
        self.calcButton.place(x=790, y=650)

    def __createDiamondScheibeFrame(self):
        diamondScheibeFrame = Frame(self.window)
        row = 0
        Label(diamondScheibeFrame, text='Diamond Scheibe: (Bitte waehlen Sie eine gewuenschte Variation)').grid(
            row=row, sticky=W)

        row += 1
        self.__createThreeValuesFrame(diamondScheibeFrame).grid(row=row, column=0)

        self.convertBtn = Button(diamondScheibeFrame, textvariable=self.convertButtonText)
        WindowUtil.setDefaultButtonStyle(self.convertBtn)
        self.convertBtn.grid(row=row, column=1, padx=20)

        self.__createFourPointsFrame(diamondScheibeFrame).grid(row=row, column=2)

        return diamondScheibeFrame

    def __createThreeValuesFrame(self, master=Frame):
        threeValuesFrame = Frame(master)
        row = 0
        threeValuesRadioBtn = Radiobutton(threeValuesFrame, text="Three Values Version",
                                          variable=self.diamondFrameSelectNr, value=1,
                                          command=self.onClick)
        threeValuesRadioBtn.grid(row=row, column=0)
        threeValuesRadioBtn.select()

        # row += 1
        self.threeValuesCanvasFrame = self.__createThreeValuesCanvasFrame(threeValuesFrame)
        self.threeValuesCanvasFrame.grid(row=row, column=1)
        row += 1
        self.threeValuesInputFrame = self.__createThreeValuesInputFrame(threeValuesFrame)
        self.threeValuesInputFrame.grid(row=row, column=0, columnspan=2, sticky=W)
        return threeValuesFrame

    def __createThreeValuesCanvasFrame(self, master=Frame):
        threeValuesCanvasFrame = Frame(master)
        canvas = Canvas(threeValuesCanvasFrame, width=200, height=200)
        canvas.grid(row=0, column=1, columnspan=1)
        p1x = p4x = 100
        p1y = p6y = 120
        p2x = p3x = 80
        p2y = 100
        p3y = 60
        p4y = p5y = 40
        p5x = p6x = 200
        p0x = 60
        p0y = (p5y + p6y) / 2
        radius = 3
        canvas.create_polygon(p1x, p1y, p0x, p0y, p4x, p4y, p5x, p5y, p6x, p6y, outline="black", fill="")
        canvas.create_line(p2x, p2y, p3x, p3y, fill="blue", dash=(1, 1))
        canvas.create_text(p2x + 8, (p2y + p3y) / 2, fill="darkblue", text="d1")
        canvas.create_line(p1x, p1y, p4x, p4y, fill="blue", dash=(1, 1))
        canvas.create_text(p1x + 8, (p1y + p4y) / 2, fill="darkblue", text="d2")
        canvas.create_text(p0x + 8, p0y, fill="darkblue", text="ß")
        return threeValuesCanvasFrame

    def __createThreeValuesInputFrame(self, master=Frame):
        threeValuesInputFrame = Frame(master)
        row = 0
        WindowUtil.createInputEntry(threeValuesInputFrame, "DiamondScheibe ß", row, self.diamond_beta)
        row += 1
        WindowUtil.createInputEntry(threeValuesInputFrame, "DiamondScheibe d1", row, self.diamond_d1)
        row += 1
        WindowUtil.createInputEntry(threeValuesInputFrame, "DiamondScheibe d2", row, self.diamond_d2)
        return threeValuesInputFrame

    def __createFourPointsFrame(self, master=Frame):
        fourPointsFrame = Frame(master)
        row = 0
        fourPointsRadioBtn = Radiobutton(fourPointsFrame, text="Four Points Version",
                                         variable=self.diamondFrameSelectNr,
                                         value=2,
                                         command=self.onClick)
        fourPointsRadioBtn.grid(row=row, column=0)
        # row += 1
        self.fourPointsCanvasFrame = self.__createFourPointsCanvasFrame(fourPointsFrame)
        self.fourPointsCanvasFrame.grid(row=row, column=1)
        row += 1
        self.fourPointsInputFrame = self.__createFourPointsInputFrame(fourPointsFrame)
        self.fourPointsInputFrame.grid(row=row, column=0, columnspan=2)
        return fourPointsFrame

    def __createFourPointsCanvasFrame(self, master=Frame):
        fourPointsCanvasFrame = Frame(master)
        canvas = Canvas(fourPointsCanvasFrame, width=200, height=200)
        canvas.grid(row=0, column=1, columnspan=1)
        p1x = p4x = 100
        p1y = p6y = 120
        p2x = p3x = 80
        p2y = 100
        p3y = 60
        p4y = p5y = 40
        p5x = p6x = 200
        radius = 3
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
        return fourPointsCanvasFrame

    def __createFourPointsInputFrame(self, master=Frame):
        fourPointsInputFrame = Frame(master)
        row = 0
        WindowUtil.createPointInputEntry(fourPointsInputFrame, "DiamondScheibe P1", row, self.diamond_p1x,
                                         self.diamond_p1y)
        row += 1
        WindowUtil.createPointInputEntry(fourPointsInputFrame, "DiamondScheibe P2", row, self.diamond_p2x,
                                         self.diamond_p2y)
        row += 1
        WindowUtil.createPointInputEntry(fourPointsInputFrame, "DiamondScheibe P3", row, self.diamond_p3x,
                                         self.diamond_p3y)
        row += 1
        WindowUtil.createPointInputEntry(fourPointsInputFrame, "DiamondScheibe P4", row, self.diamond_p4x,
                                         self.diamond_p4y)
        return fourPointsInputFrame

    def onClick(self):
        if self.diamondFrameSelectNr.get() == 1:
            self.convertButtonText.set("==>")
            WindowUtil.enableFrame(self.threeValuesInputFrame)
            WindowUtil.disableFrame(self.fourPointsInputFrame)
        elif self.diamondFrameSelectNr.get() == 2:
            self.convertButtonText.set("<==")
            WindowUtil.enableFrame(self.fourPointsInputFrame)
            WindowUtil.disableFrame(self.threeValuesInputFrame)

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
        Label(paraFrame, text='Parameters: ').grid(row=row, sticky=W)
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

    def addCalcBtnActionListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)

    def addConvertBtnActionListener(self, func):
        self.convertBtn.bind("<ButtonRelease-1>", func)
