from keras.models import Sequential
from keras.layers import Dense, Dropout
import os
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
        self.trainingData = tf.placeholder()
        self.trainingLabels = []
        self.testData = []
        self.testLabels =[]
        self.model = Sequential()

    def createDummyData(self, setSize, numSets):
        self.trainingData = np.random.random((1000, 20))
        self.trainingLabels = np.random.randint(2, size=(1000, 1))
        self.testData = np.random.random((100, 20))
        self.testLabels = np.random.randint(2, size=(100, 1))

    def realData(self, setSize, numSets):
        print("this does nothing")

    def createModel(self):
        model = Sequential()
        model.add(Dense(64, input_dim=20, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1, activation='sigmoid'))

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
        self.createDummyData(1000, 20)
        self.createModel()
        self.compileModel()
        self.trainModel()
        self.evalModel()

if __name__== "__main__":
    md = Model()
    md.main()
