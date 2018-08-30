#!/usr/bin/python3
from mycode.util.DrawUtil import *
from mycode.util.WindowUtil import *


class MainPage(Frame):
    def __init__(self, window):
        self.window = window
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

        self.abrichtScheibeFrame = self.__createAbrichtScheibeFrame()
        self.abrichtScheibeFrame.place(x=25, y=250)
        #
        # self.paraFrame = Frame(self.window)
        # self.__createParaFrame()
        # self.paraFrame.place(x=450, y=250)

        self.calcButton = Button(text="calc", bg="yellow", fg="red")
        self.calcButton.place(x=750, y=450)

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

    def __createDiamondScheibeFrame(self):
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
        Label(inputFrame, text='Abricht Scheibe: ').grid(row=row)
        row += 1
        WindowUtil.createPointInputEntry(inputFrame, "Abricht P1", row, self.abricht_p1x,
                                         self.abricht_p1y)
        row += 1
        WindowUtil.createPointInputEntry(inputFrame, "Abricht P2", row, self.abricht_p2x,
                                         self.abricht_p2y)

    def __createParaFrame(self):
        row = 0
        Label(self.paraFrame, text='Parameters: ').grid(row=row)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "Anfang Abstand", row, self.beginDistance)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "AbrichtScheibe Flansch", row, self.abricht_flansch)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "DiamondScheibe Flansch", row, self.diamond_flansch)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "Delta X", row, self.deltax)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "Delta Y", row, self.deltay)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "AbrichtScheibe Durchmesser", row, self.abricht_diameter)
        row += 1
        WindowUtil.createInputEntry(self.paraFrame, "DiamondScheibe Durchmesser", row, self.diamond_diameter)

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
