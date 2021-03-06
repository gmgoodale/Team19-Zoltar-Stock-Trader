import matplotlib
matplotlib.use("TkAgg") # Allows for Tk use rather than the standard
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
import numpy
from datetime import datetime
import seaborn
import pandas
from pandas.plotting import register_matplotlib_converters
from numpy.random import randint

import tkinter as tk
from tkinter import ttk

import os

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
    def generateGraph(self, predictionName, plotData, stockNames):

        graphArea = self.graphArea
        if self.checkNumbers(plotData, stockNames):
            graphArea.clear()
            dates = []
            for d in plotData['Date']:
                dates.append(datetime.strptime(d, '%Y-%m-%d'))

            for S in stockNames:
                graphArea.plot(dates, plotData[S], label = S)

            graphArea.set(title = predictionName)
            graphArea.legend(framealpha = 1, frameon = True)
            graphArea.set_xlabel("Date")
            graphArea.set_ylabel("Price (USD)")
            graphArea.xaxis.set_major_locator(plt.MaxNLocator(10))
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
                    print(S)
                    return False
                return True
        except:
            return False
