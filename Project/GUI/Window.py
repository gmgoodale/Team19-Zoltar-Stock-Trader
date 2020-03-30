#!/usr/bin/python
import importlib
import Grapher

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

        for F in (StartPage, Grapher.GrapherWindow):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.showFrame(StartPage)

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
        self.showFrame(StartPage)

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Zoltar Stock Trader Main Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        grapherButton = ttk.Button(self, text = "Grapher",
                            command = lambda: controller.showFrame(Grapher.GrapherWindow))
        grapherButton.pack()
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
