#!/usr/bin/python
import importlib

# Add page files here
import Grapher
import MainPage
import LoadPage
import NewModelPage
import AddModelPage
import DevToolsPage

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

# Base of the user interface; calls pages to be used from frames.
class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        #======================= Creating the window =====================
        super().__init__(*args, **kwargs)

        #tk.Tk.iconbitmap(self, default = "Zoltar_Icon.ico")
        tk.Tk.wm_title(self, "Zoltar")

        # Container = window seen
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1) # No priorities
        container.grid_columnconfigure(0, weight = 1)

        # Frame configuration: loop runs through right-side frames
        self.frames = {}

        # Add all right-side frames to this loop
        for F in (MainPage.MainWindow, LoadPage.LoadWindow,
                  NewModelPage.NewModelWindow, AddModelPage.AddModelWindow, DevToolsPage.DevToolsWindow):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 1, sticky = "nsew")

        # Only 1 Left-side frame, but same function as loop
        frame = Grapher.GrapherWindow(container, self)
        self.frames[Grapher.GrapherWindow] = frame

        frame.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(MainPage.MainWindow) # Initial page to show

    #====================== Data Handling Methods ======================
    # Needs list: report available csv, return csv path, get stock name

    #====================== DNN Handling Methods =======================
    # Needs List: Load model results, report available models,
    #             Train new DNN

    #===================== Grapher Interface Methods ========================
    # Needs List:
    def changeGrapherLabel(self, newLabel):
        Grapher.GrapherWindow.changeLabel(newLabel)

    def displayGraph(self, csvFileName = "TestData.csv", stockName = "Stock Data"):
        Grapher.GrapherWindow.generateGraph(csvFileName, stockName)

    #======================= Navigation Methods ========================
    def showFrame(self, cont):
        try:
            frame = self.frames[cont]

        except:
            return -1
        # raise; all other frames are underneath (Saves state of each)
        frame.tkraise()
        return 0

    def toHome(self):
        self.showFrame(MainPage.MainWindow)

    def toLoadPage(self):
        self.showFrame(LoadPage.LoadWindow)

    def toNewModel(self):
        self.showFrame(NewModelPage.NewModelWindow)

    def toAddModel(self):
        self.showFrame(AddModelPage.AddModelWindow)

    def toDevTools(self):
        self.showFrame(DevToolsPage.DevToolsWindow)



# When Window.py is run then it is assumed the program should run.

zoltar = UserInterface()
zoltar.geometry("1280x720")
zoltar.mainloop()
