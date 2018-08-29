#!/usr/bin/python3
from tkinter import *


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
