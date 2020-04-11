import matplotlib
matplotlib.use("TkAgg") # Allows for Tk use rather than the standard
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy
import seaborn
import pandas
from numpy.random import randint

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)

figure = plt.figure()
graphArea = figure.add_subplot(111)

class GrapherWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text = "Graph Page", font = LARGE_FONT)
        self.label.pack(pady = 10, padx = 10)

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

        graphButton = ttk.Button(self, text = "Generate Graph",
                                 command = lambda: controller.displayGraph())
        graphButton.pack()

    #========================== Frame Functions =============================
    def changeLabel(self, newLabel):
        self.label['text'] = newLabel

    #========================= Graph Functions ==============================
    def generateGraph(self, predictionFileName, stockName = "Stock Data"):
        # 'usecols' can be added to read_csv if multiple cols are present in file
        try:
            plotData = pandas.read_csv(predictionFileName)

        except:
            print("ERROR: when reading csv file while generating graph; aborting.")
            return False

        if self.checkNumbers(plotData):
            graphArea.clear()
            graphArea.plot(plotData)
            graphArea.set(title = stockName)
            graphArea.set_xlabel("Time (Days)")
            graphArea.set_ylabel("Price (USD)")
            graphArea.grid()
            self.canvas.draw()
            return True

        else:
            print("ERROR:  Data contains negative numbers")
            return False


    def checkNumbers(self, data):
        for col in data.columns:
            if min(data[col]) < 0:
                return False
        return True
