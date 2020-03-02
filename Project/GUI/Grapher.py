import matplotlib
matplotlib.use("TkAgg") # Allows for Tk use rather than the standard
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import numpy
import seaborn
import pandas
from numpy.random import randint

import tkinter as tk
from tkinter import tkk

LARGE_FONT = ("Verdana", 12)

class GrapherWindow:
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.label(self, text = "Graph Page", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        filename = ''


    def generateGraph(self, predictionFileName, stockName = "Stock Data"):
        # 'usecols' can be added to read_csv if multiple cols are present in file
        try:
            plotData = pandas.read_csv(predictionFileName)

        except:
            print("ERROR: when reading csv file while generating graph; aborting.")
            return False

        if self.checkNumbers(plotData):
            # Much of this code is based on the work found at
            # https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
            figure = Figure(figsize = (5, 5), dpi = 100)
            graph = figure.add_subplot(111)
            graph.plot('Time (Days)', 'Price (USD)', data = plotData)
            graph.set(title = stockName)
            graph.grid()

            canvas = FigureCanvasTkAgg(figure, self)
            canvas.show()
            canvas.get_tk_widget().pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)

            toolbar = NavigationToolbar2TkAgg(canvas, self)
            toolbar.update()
            canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)

            saveButton = ttk.Button(self, text = "Save Graph",
                                    command = fig.savefig(stockName + " Graph.png")
            saveButton.pack()

        else:
            print("ERROR:  Data contains negative numbers")
            return False


        def checkNumbers(self, data):
            for col in data.columns:
                if data[col].min < 0:
                    return False

class GrapherTester:
    def __init__(self):
        subject = Grapher()
        testFileName = 'TestData.csv'
        testStockName = 'Test Stock'
        testGenerateGraphWithAllPositiveNumbers(testFileName, testStockName)

    def createTestData(xAxis, yAxis):
        # Generates a graph with random Data
        plotData = {'X-Axis':xAxis, 'Y-Axis':yAxis}
        dataFrame = pandas.DataFrame(plotData)
        return dataFrame

    def testGenerateGraphWithAllPositiveNumbers(self, testFileName, stockName):
        dataFrame = self.createTestData([0, 1, 2, 3, 4], [3, 5, 1, 2, 6])
        subject.generateGraph(predictionFileName = "TestData.csv")
        assert os.path.exists(self.testStockName + " Graph.png")

    def testGenerateGraphWithSomeBadNumbers(self, testFileName, stockName):
        dataFrame = self.createTestData([0, 1, 2, 3, 4], [3, 5, -1, 2, 6])
        assert subject.generateGraph(testFileName, dataFrame) == False
