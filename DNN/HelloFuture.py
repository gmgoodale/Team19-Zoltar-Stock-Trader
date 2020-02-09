from keras.models import Sequential
from keras.layers import Dense, Dropout
import os
import numpy as np

# This turns of the use of AVX, AVX2 and FMA which are instruction set extensions
# for vector operations. If you have a GPU or are not concerned with performance
# leave this off since GPU will run most expensive instructions. If you want to
# use AVX or FMA, do a more advanced build of TF here https://stackoverflow.com/questions/41293077/how-to-compile-tensorflow-with-sse4-2-and-avx-instructions
# or use this git issue here https://github.com/tensorflow/tensorflow/issues/8037
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Generate dummy data
trainingData = np.random.random((1000, 20))
trainingLabels = np.random.randint(2, size=(1000, 1))
testData = np.random.random((100, 20))
testLabels = np.random.randint(2, size=(100, 1))

model = Sequential()
model.add(Dense(64, input_dim=20, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(trainingData, trainingLabels,
          epochs=20,
          batch_size=128)
score = model.evaluate(testData, testLabels, batch_size=128)
