#!/usr/bin/python
from pathlib import Path

import tkinter as tk
from tkinter import ttk

import pandas

LARGE_FONT = ("Verdana", 12, "bold")
SMALL_FONT = ("Verdana", 10)

class DNNWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.grid_columnconfigure(0, weight = 1)

        windowLabel = tk.Label(self, text = "DNN Statistics", font = LARGE_FONT)
        windowLabel.grid(row = 0, column = 0, columnspan = 10, sticky = tk.N, padx = 10, pady = 20)

        self.drawModelID(parent, controller)
        self.drawModelRatio(parent, controller)

    def drawModelID(self, parent, controller):
        widgetRow = 1
        widgetCol = 0

        modelIDLabel = tk.Label(self, text = "Current Model:  ", font = SMALL_FONT)
        modelIDLabel.grid(row = widgetRow, column = widgetCol, sticky = tk.W, padx = 2, pady = 5)

        self.modelIDText = tk.Text(self, height = 1, width = 15)
        self.modelIDText.grid(row = widgetRow, column = widgetCol + 1, sticky = tk.W, padx = 2, pady = 5)

    def drawModelRatio(self, parent, controller):
        widgetRow = 2
        widgetCol = 0

        modelRatioLabel = tk.Label(self, text = "Model Accuracy:  ", font = SMALL_FONT)
        modelRatioLabel.grid(row = widgetRow, column = widgetCol, sticky = tk.W, padx = 2, pady = 5)

        self.modelRatioText = tk.Text(self, height = 1, width = 7)
        self.modelRatioText.grid(row = widgetRow, column = widgetCol + 1, sticky = tk.W, padx = 2, pady = 5)
