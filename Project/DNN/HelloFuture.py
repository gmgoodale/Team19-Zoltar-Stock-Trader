from keras.models import Sequential
from keras.layers import Dense, Dropout
import os
import datetime
import numpy as np
import DataHandler
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
        self.trainingData = np.random.random((1000, 20))
        self.trainingLabels = np.random.randint(2, size=(1000, 1))
        self.testData = np.random.random((100, 20))
        self.testLabels = np.random.randint(2, size=(100, 1))

    def realData(self, setSize):
        end = datetime.datetime.now()
        allData = self.dh.toNumpy(end, setSize, 'AOS')
        numSets = np.size(allData,0)

        # Cut the set in half to create training data
        self.trainingData = np.copy(allData[:int(numSets/2),setSize-1])
        self.trainingLabels = np.zeros([int(numSets/2), 1])
        for i in range(0, int(numSets/2)):
            if (self.trainingData[i][0] < self.trainingData[i][setSize-1]):
                self.trainingLabels[i][0] = 1
            else: self.trainingLabels[i][0] = 0

        # Cut the set in half to create test data
        self.testData = np.copy(allData[int(numSets/2)+1:,setSize-1])
        self.testLabels = np.zeros([int(numSets/2), 1])
        for i in range(0, int(numSets/2)):
            if (self.testData[i][0] < self.testData[i][setSize-1]):
                self.testLabels[i][0] = 1
            else: self.testLabels[i][0] = 0


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

    def trainModel(self):
        self.model.fit(self.trainingData, self.trainingLabels,
                  epochs=20,
                  batch_size=128)

    def evalModel(self):
        score = self.model.evaluate(self.testData, self.testLabels, batch_size=128)

    def main(self):
        self.createDummyData(20,1)
        self.createModel(20)
        self.compileModel()
        self.trainModel()
        self.evalModel()

if __name__== "__main__":
    md = Model()
    md.main()
