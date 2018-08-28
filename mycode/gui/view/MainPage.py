#!/usr/bin/python3
from mycode.gui.BeanFactory import *
from mycode.util.DrawUtil import *


class MainPage(Frame):
    def __init__(self, window):
        self.window = window
        # abricht scheibe value
        self.abricht_p1x = IntVar()
        self.abricht_p1y = IntVar()
        self.abricht_p2x = IntVar()
        self.abricht_p2y = IntVar()

        # diamond scheibe value
        self.diamond_p1x = IntVar()
        self.diamond_p1y = IntVar()
        self.diamond_p2x = IntVar()
        self.diamond_p2y = IntVar()
        self.diamond_p3x = IntVar()
        self.diamond_p3y = IntVar()
        self.diamond_p4x = IntVar()
        self.diamond_p4y = IntVar()

        # paras
        self.beginDistance = DoubleVar()
        self.abricht_flansch = IntVar()
        self.diamond_flansch = IntVar()
        self.deltax = IntVar()
        self.deltay = IntVar()
        self.abricht_diameter = DoubleVar()
        self.diamond_diameter = DoubleVar()

        self.canvasFrame = Frame(self.window)
        self.__createCanvasFrame()
        self.canvasFrame.place(x=200, y=20)
        # self.canvasFrame.pack()

        self.abrichtScheibeFrame = Frame(self.window)
        self.__createAbrichtScheibeFrame()
        self.abrichtScheibeFrame.place(x=25, y=250)
        # self.abrichtScheibeFrame.pack(side = LEFT)

        self.diamondScheibeFrame = Frame(self.window)
        self.__createDiamondScheibeFrame()
        self.diamondScheibeFrame.place(x=0, y=350)
        # self.diamondScheibeFrame.pack(side = LEFT)

        self.paraFrame = Frame(self.window)
        self.__createParaFrame()
        self.paraFrame.place(x=450, y=250)

        self.calcButton = Button(text="calc", bg="yellow", fg="red")
        self.calcButton.place(x=750, y=450)

    def __createCanvasFrame(self):
        self.__drawAbrichtScheibe()
        self.__drawDiamondScheibe()

    def __drawAbrichtScheibe(self):
        canvas = Canvas(self.canvasFrame, width=200, height=200)
        canvas.grid(row=0, column=0, columnspan=1)
        width = 40
        height = 80
        p1x = 40
        p1y = p2y = 80
        p2x = p3x = p1x + width
        p3y = p2y + height
        radius = 3
        canvas.create_text(50, 10, fill="darkblue", font="Times 10 italic bold", text="Abricht Scheibe")
        canvas.create_rectangle(p1x, p1y, p3x, p3y)
        DrawUtil.drawCicle(p1x, p1y, radius, canvas)
        canvas.create_text(p1x, p1y - 10, fill="darkblue", font="Times 10 italic bold", text="p1")
        DrawUtil.drawCicle(p2x, p2y, radius, canvas)
        canvas.create_text(p2x, p2y - 10, fill="darkblue", font="Times 10 italic bold", text="p2")

        axisX = p1x + (p2x - p1x) / 2
        axisY = p1y
        DrawUtil.drawAxis(axisX, axisY, 51, "red", 0, canvas)

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

    def __createAbrichtScheibeFrame(self):
        row = 0
        Label(self.abrichtScheibeFrame, text='Abricht Scheibe: ').grid(row=row)
        row += 1
        self.__createPointInputEntry(self.abrichtScheibeFrame, "Abricht P1", row, self.abricht_p1x, self.abricht_p1y)
        row += 1
        self.__createPointInputEntry(self.abrichtScheibeFrame, "Abricht P2", row, self.abricht_p2x, self.abricht_p2y)

    def __createDiamondScheibeFrame(self):
        row = 0
        Label(self.diamondScheibeFrame, text='Diamond Scheibe: ').grid(row=row)
        row += 1
        self.__createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P1", row, self.diamond_p1x,
                                     self.diamond_p1y)
        row += 1
        self.__createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P2", row, self.diamond_p2x,
                                     self.diamond_p2y)
        row += 1
        self.__createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P3", row, self.diamond_p3x,
                                     self.diamond_p3y)
        row += 1
        self.__createPointInputEntry(self.diamondScheibeFrame, "DiamondScheibe P4", row, self.diamond_p4x,
                                     self.diamond_p4y)

    def __createParaFrame(self):
        row = 0
        Label(self.paraFrame, text='Parameters: ').grid(row=row)
        row += 1
        self.__createInputEntry(self.paraFrame, "Anfang Abstand", row, self.beginDistance)
        row += 1
        self.__createInputEntry(self.paraFrame, "AbrichtScheibe Flansch", row, self.abricht_flansch)
        row += 1
        self.__createInputEntry(self.paraFrame, "DiamondScheibe Flansch", row, self.diamond_flansch)
        row += 1
        self.__createInputEntry(self.paraFrame, "Delta X", row, self.deltax)
        row += 1
        self.__createInputEntry(self.paraFrame, "Delta Y", row, self.deltay)
        row += 1
        self.__createInputEntry(self.paraFrame, "AbrichtScheibe Durchmesser", row, self.abricht_diameter)
        row += 1
        self.__createInputEntry(self.paraFrame, "DiamondScheibe Durchmesser", row, self.diamond_diameter)

    def __createPointInputEntry(self, frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1)
        Entry(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1)
        Entry(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1)

    def __createInputEntry(self, frame, name, row, entry):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1)
        Entry(frame, textvariable=entry).grid(row=row, column=1, columnspan=1)

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
