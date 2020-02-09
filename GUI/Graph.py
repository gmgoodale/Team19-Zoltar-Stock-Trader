import matplotlib
import matplotlib.pyplot as plt
import numpy
import seaborn
import pandas
from numpy.random import randint

class Graph:
    def __init__(self):
        self.unitTests()

    def generateGraph(self, predictionFileName, stockName = "Stock Data"):
        # 'usecols' can be added to read_csv if multiple cols are present in file
        try:
            plotData = pandas.read_csv(predictionFileName)

        except:
            print("Error reading csv file while generating graph; aborting.")
            return

        fig, graph = plt.subplots()
        graph.plot('Time (Days)', 'Price (USD)', data = plotData)
        graph.set(title = stockName)
        graph.grid()
        fig.savefig(stockName + " Graph.png")
        plt.show()


    def unitTests(self):
        # Generates a graph with random Data
        plotData = pandas.DataFrame({'Time (Days)' : range(1, 101), 'Price (USD)': numpy.random.randint(1, 50, 100) })
        plotData.to_csv("TestData.csv")
        try:
            self.generateGraph("TestData.csv", stockName = "Test Data")

        except:
            print("FAIL:  generateGraph")

test = Graph()
