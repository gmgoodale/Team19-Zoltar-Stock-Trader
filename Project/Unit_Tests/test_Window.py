# Class to test the GrapherWindow Class
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
