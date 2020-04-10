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
        super().__init__(*args, **kwargs)

        #tk.Tk.iconbitmap(self, default = "Zoltar_Icon.ico")
        tk.Tk.wm_title(self, "Zoltar")

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (MainPage.MainWindow, Grapher.GrapherWindow, LoadPage.LoadWindow,
                  NewModelPage.NewModelWindow, AddModelPage.AddModelWindow, DevToolsPage.DevToolsWindow):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(MainPage.MainWindow)

    # Attempts to show a frame given a container 'cont'
    # Success returns 0, failure returns -1
    def showFrame(self, cont):
        try:
            frame = self.frames[cont]

        except:
            return -1

        frame.tkraise()
        return 0

    # Commands to navigate to any page (better way?)
    def toHome(self):
        self.showFrame(MainPage.MainWindow)

    def toGrapher(self):
        self.showFrame(Grapher.GrapherWindow)

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
