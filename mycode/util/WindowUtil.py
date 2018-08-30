#!/usr/bin/python3
from tkinter import *
from tkinter import Label, Entry, font


class WindowUtil:

    @staticmethod
    def setWindowAttributes(title, w, h, window=Misc):
        window.title(title)

        # get screen width and height
        ws = window.winfo_screenwidth()  # width of the screen
        hs = window.winfo_screenheight()  # height of the screen

        # calculate x and y coordinates for the Tk root window
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        # set the dimensions of the screen
        # and where it is placed
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        return window

    @staticmethod
    def disableFrame(frame=Frame):
        for child in frame.winfo_children():
            child.configure(state='disabled')

    @staticmethod
    def enableFrame(frame=Frame):
        for child in frame.winfo_children():
            child.configure(state='normal')

    @staticmethod
    def createPointInputEntry(frame, name, row, entryX, entryY):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1, sticky=W)
        Label(frame, text='x:').grid(row=row, column=1, columnspan=1)
        Entry(frame, textvariable=entryX).grid(row=row, column=2, columnspan=1)
        Label(frame, text='y:').grid(row=row, column=3, columnspan=1)
        Entry(frame, textvariable=entryY).grid(row=row, column=4, columnspan=1)

    @staticmethod
    def createInputEntry(frame, name, row, entry):
        Label(frame, text=name + ": ").grid(row=row, column=0, columnspan=1, sticky=W)
        Entry(frame, textvariable=entry).grid(row=row, column=1, columnspan=1, sticky=E)

    @staticmethod
    def setDefaultButtonStyle(button=Button):
        button['font'] = font.Font(family='Helvetica', size=14, weight='bold')
        button['bg'] = "yellow"
        button['fg'] = "red"
