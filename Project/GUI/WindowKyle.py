#!/usr/bin/python
import importlib
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

        for F in (MainPage, Grapher.GrapherWindow, LoadPage, NewModelPage,
                    AddModelPage, DevToolsPage):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(MainPage)

    # Attempts to show a frame given a container 'cont'
    # Success returns 0, failure returns -1
    def showFrame(self, cont):
        try:
            frame = self.frames[cont]

        except:
            return -1

        frame.tkraise()
        return 0

    def returnToHome(self):
        self.showFrame(MainPage)

# TODO Settings and Graph Page
#        makeNewModelButton = ttk.Button(self, text="Settings",
#                            command = lambda: controller.showFrame())
#        makeNewModelButton.pack()

#        loadExistingModelButton = ttk.Button(self, text="Graph Page",
#                            command = lambda: controller.showFrame())
#        loadExistingModelButton.pack()

# When Window.py is run then it is assumed the program should run.


zoltar = UserInterface()
zoltar.geometry("1280x720")
zoltar.mainloop()
