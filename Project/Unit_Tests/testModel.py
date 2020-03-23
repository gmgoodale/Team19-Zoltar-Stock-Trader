import Model
import numpy as mp

class TestModel:

    def __init__(self):
        self.md = Model.Model();

    def unitTest1(self):
        self.md.createDummyData(20, 1000)
        expectedDataSize = (1000, 20)
        expectedLabelSize = (1000, 1)
        if (self.md.trainingData.shape != expectedDataSize):
            print("Unit Test 1: FAIL")
        elif (self.md.testData.shape != expectedDataSize):
            print("Unit Test 1: FAIL")
        elif (self.md.trainingLabels.shape != expectedLabelSize):
            print("Unit Test 1: FAIL")
        elif (self.md.testLabels.shape != expectedLabelSize):
            print("Unit Test 1: FAIL")
        else: print("Unit Test 1: PASS")

    def unitTest2(self):
        self.md.realData(100, 'AOS')
        expectedDataSize = (self.md.halfNumSetsTest, 100)
        expectedLabelSize = (self.md.halfNumSetsTest, 1)
        if (self.md.trainingData.shape != expectedDataSize):
            print("Unit Test 2: FAIL")
        elif (self.md.testData.shape != expectedDataSize):
            print("Unit Test 2: FAIL")
        elif (self.md.trainingLabels.shape != expectedLabelSize):
            print("Unit Test 2: FAIL")
        elif (self.md.testLabels.shape != expectedLabelSize):
            print("Unit Test 2: FAIL")
        else: print("Unit Test 2: PASS")

    def unitTest3(self):
        

    def main(self):
        self.unitTest1()
        self.unitTest2()

if __name__== "__main__":
    test = TestModel()
    test.main()
