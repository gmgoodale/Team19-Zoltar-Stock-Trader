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

        button1 = tk.Button(self, text = "Load Model",
                            command = lambda: controller.show_frame(LoadPage))
        button1.pack()

        button2 = tk.Button(self, text = "Train New Model",
                            command = lambda: controller.show_frame(NewModelPage))
        button2.pack()

        button3 = tk.Button(self, text = "Add Model",
                            command = lambda: controller.show_frame(AddModelPage))
        button3.pack()

        button4 = tk.Button(self, text = "Developer Tools",
                            command = lambda: controller.show_frame(DevToolsPage))
        button4.pack()

# TODO Settings and Graph Page
#        makeNewModelButton = ttk.Button(self, text="Settings",
#                            command = lambda: controller.showFrame())
#        makeNewModelButton.pack()

#        loadExistingModelButton = ttk.Button(self, text="Graph Page",
#                            command = lambda: controller.showFrame())
#        loadExistingModelButton.pack()

# When Window.py is run then it is assumed the program should run.
