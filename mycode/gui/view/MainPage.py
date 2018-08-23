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

        self.__setDefaultValues()

        self.row = 0
        self.canvasFrame = Frame(self.window)
        self.canvasFrame.grid(row=self.row, column=0, columnspan=1)
        self.__createCanvasFrame()

        self.__createEmptyRow()
        self.row += 1
        self.abrichtScheibeFrame = Frame(self.window)
        self.abrichtScheibeFrame.grid(row=self.row, column=0, columnspan=7)
        self.__createAbrichtScheibeFrame()

        self.__createEmptyRow()
        self.row += 1
        self.diamondScheibeFrame = Frame(self.window)
        self.diamondScheibeFrame.grid(row=self.row, column=0, columnspan=5)
        self.__createDiamondScheibeFrame()

        self.__createEmptyRow()
        self.row += 1
        self.calcButton = Button(text="calc", bg="yellow", fg="red")
        self.calcButton.grid(row=self.row, column=0)

    def __setDefaultValues(self):
        # abricht scheibe value
        self.abricht_p1x.set(-2)
        self.abricht_p1y.set(0)
        self.abricht_p2x.set(2)
        self.abricht_p2y.set(0)

        # diamond scheibe value
        self.diamond_p1x.set(-3)
        self.diamond_p1y.set(-2)
        self.diamond_p2x.set(-1)
        self.diamond_p2y.set(0)
        self.diamond_p3x.set(1)
        self.diamond_p3y.set(0)
        self.diamond_p4x.set(3)
        self.diamond_p4y.set(-2)

    def __createCanvasFrame(self):
        # canvas.create_line(0, 0, 200, 100)
        # canvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        # canvas.create_rectangle(50, 25, 150, 75, fill="blue")
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

        DrawUtil.drawAxis(60, 80, 50, "red", 0, canvas)

    def __drawDiamondScheibe(self):
        canvas = Canvas(self.canvasFrame, width=200, height=200)
        canvas.grid(row=0, column=1, columnspan=1)
        p1x = p4x = 60
        p1y = p6y = 120
        p2x = p3x = 40
        p2y = 100
        p3y = 60
        p4y = p5y = 40
        p5x = p6x = 160
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

    def __createAbrichtScheibeFrame(self):
        row = 0
        Label(self.abrichtScheibeFrame, text='Abricht Scheibe: ').grid(row=row, column=0, columnspan=1)
        row += 1
        self.__createInputEntry(self.abrichtScheibeFrame, "Abricht P1", row, self.abricht_p1x, self.abricht_p1y)
        row += 1
        self.__createInputEntry(self.abrichtScheibeFrame, "Abricht P2", row, self.abricht_p2x, self.abricht_p2y)

    def __createDiamondScheibeFrame(self):
        row = 0
        Label(self.diamondScheibeFrame, text='Diamond Scheibe: ').grid(row=row, column=0, columnspan=1)
        row += 1
        self.__createInputEntry(self.diamondScheibeFrame, "DiamondScheibe P1", row, self.diamond_p1x, self.diamond_p1y)
        row += 1
        self.__createInputEntry(self.diamondScheibeFrame, "DiamondScheibe P2", row, self.diamond_p2x, self.diamond_p2y)
        row += 1
        self.__createInputEntry(self.diamondScheibeFrame, "DiamondScheibe P3", row, self.diamond_p3x, self.diamond_p3y)
        row += 1
        self.__createInputEntry(self.diamondScheibeFrame, "DiamondScheibe P4", row, self.diamond_p4x, self.diamond_p4y)

    def __createInputEntry(self, frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1)
        Entry(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1)
        Entry(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1)

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)

    def __createEmptyRow(self):
        self.row += 1
        Label(self.window).grid(row=self.row, column=0)
