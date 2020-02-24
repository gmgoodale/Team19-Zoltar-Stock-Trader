import matplotlib
import matplotlib.pyplot as plt
import numpy
import seaborn
import pandas
from numpy.random import randint

class Grapher:
    def __init__(self):
        filename = ''

    def generateGraph(self, predictionFileName, stockName = "Stock Data"):
        # 'usecols' can be added to read_csv if multiple cols are present in file
        try:
            plotData = pandas.read_csv(predictionFileName)

        except:
            print("ERROR: when reading csv file while generating graph; aborting.")
            return False

        if self.checkNumbers(plotData):
            fig, graph = plt.subplots()
            graph.plot('Time (Days)', 'Price (USD)', data = plotData)
            graph.set(title = stockName)
            graph.grid()
            fig.savefig(stockName + " Graph.png")
            plt.show()

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
        self.createTestData()
        testGenerateGraphWithAllPositiveNumbers(testFileName, testStockName)

    def createTestData(xAxis, yAxis):
        # Generates a graph with random Data
        plotData = {'X-Axis':xAxis, 'Y-Axis':yAxis}
        dataFrame = pandas.DataFrame(plotData)
        return dataFrame

    def testGenerateGraphWithAllPositiveNumbers(self, testFileName, stockName):
        subject.generateGraph(predictionFileName = "TestData.csv")
        assert os.path.exists(self.testStockName + " Graph.png")

    def testGenerateGraphWithBadNumbers(self, testFileName, stockName):
        dataFrame = self.createTestData([0, 1, 2, 3, 4], [3, 5, -1, 2, 6])
        assert subject.generateGraph(testFileName, dataFrame) == False
