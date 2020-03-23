from keras.models import Sequential
from keras.layers import Dense, Dropout
import os
import datetime
import numpy as np
import DataHandlerGarett as DataHandler
import tensorflow as tf

# This turns of the use of AVX, AVX2 and FMA which are instruction set extensions
# for vector operations. If you have a GPU or are not concerned with performance
# leave this off since GPU will run most expensive instructions. If you want to
# use AVX or FMA, do a more advanced build of TF here https://stackoverflow.com/questions/41293077/how-to-compile-tensorflow-with-sse4-2-and-avx-instructions
# or use this git issue here https://github.com/tensorflow/tensorflow/issues/8037
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class Model:

    def __init__(self):
        self.dh = DataHandler.Datahandler();

    def createDummyData(self, setSize, numSets):
        self.trainingData = np.random.random((numSets, setSize))
        self.trainingLabels = np.random.randint(2, size=(numSets, 1))
        self.testData = np.random.random((numSets, setSize))
        self.testLabels = np.random.randint(2, size=(numSets, 1))

    # The set size defines the width of the data frame (i.e train off sets of
    # 100 data points)
    def realData(self, setSize, Symbol):
        end = datetime.datetime.now()
        allData = self.dh.toNumpy(end, setSize, Symbol)
        numSets = np.size(allData,0)
        halfNumSets = int(numSets/2)
        self.halfNumSetsTest = halfNumSets

        # Let's create labels for the training data. This is bacially labeling
        # whether or not the stock went up or down in the last setSize worth of
        # data points. 1 means up, 0 means down
        allLabels = np.zeros([numSets, 1])
        for i in range(0, numSets):
            if (allData[i][0] < allData[i][setSize-1]):
                allLabels[i][0] = 1
            else: allLabels[i][0] = 0

        # Cut the set in half to create training data
        self.trainingData = np.zeros([halfNumSets, setSize])
        self.trainingLabels = np.zeros([halfNumSets, 1])
        for i in range(0, halfNumSets):
            self.trainingData[i] = np.copy(allData[i])
            self.trainingLabels[i] = np.copy(allLabels[i])

        # Cut the set in half to create test data
        self.testData = np.zeros([halfNumSets, setSize])
        self.testLabels = np.zeros([halfNumSets, 1])
        for i in range(0, halfNumSets):
            self.testData[i] = np.copy(allData[i+halfNumSets])
            self.testLabels[i] = np.copy(allLabels[i+halfNumSets])

    def createModel(self, inputDim):
        self.model = Sequential()
        self.model.add(Dense(64, input_dim=inputDim, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(64, activation='relu'))
        self.model.add(Dropout(0.5))
        self.model.add(Dense(1, activation='sigmoid'))

    def compileModel(self):
        self.model.compile(loss='binary_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])

    def trainModel(self, numEpochs):
        self.model.fit(self.trainingData, self.trainingLabels,
                  epochs=numEpochs,
                  batch_size=128)

    def evalModel(self):
        score = self.model.evaluate(self.testData, self.testLabels, batch_size=128)

    def main(self):
        self.realData(100, 'AOS')
        self.createModel(100)
        self.compileModel()
        self.trainModel(20)
        self.evalModel()

if __name__== "__main__":
    md = Model()
    md.main()
