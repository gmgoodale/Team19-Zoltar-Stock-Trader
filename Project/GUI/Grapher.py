import matplotlib
matplotlib.use("TkAgg") # Allows for Tk use rather than the standard
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy
import seaborn
import pandas
from pandas.plotting import register_matplotlib_converters
from numpy.random import randint

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12, "bold")

register_matplotlib_converters()

class GrapherWindow(tk.Frame):
    def __init__(self, parent, controller):
        self.figure = plt.figure()
        figure = self.figure
        self.graphArea = figure.add_subplot(111)

        tk.Frame.__init__(self, parent)

        self.canvas = FigureCanvasTkAgg(figure, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

    #========================== Frame Functions =============================
    def changeLabel(self, newLabel):
        self.label['text'] = newLabel


    #========================= Graph Functions ==============================
    def generateGraph(self, fileName, stockNames, predictionName):
        # 'usecols' can be added to read_csv if multiple cols are present in file
        try:
            plotData = pandas.read_csv(fileName)

        except:
            print("ERROR: when reading csv file {}; aborting.".format(fileName))
            return False
        graphArea = self.graphArea
        if self.checkNumbers(plotData, stockNames):
            graphArea.clear()
            time = plotData['Date']

            for S in stockNames:
                graphArea.plot_date(time, plotData[S], label = S)

            graphArea.set(title = predictionName)
            graphArea.set_xlabel("Time (Days)")
            graphArea.set_ylabel("Price (USD)")
            graphArea.grid()

            self.canvas.draw()
            return True

        else:
            print("ERROR:  Data contains negative numbers")
            return False

    def checkNumbers(self, data, stockNames):
        try:
            for S in stockNames:
                if min(data[S]) < 0:
                    return False
                return True
        except:
            return False
