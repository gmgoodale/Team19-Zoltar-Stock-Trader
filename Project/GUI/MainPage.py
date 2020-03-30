import importlib
import Grapher

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

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
