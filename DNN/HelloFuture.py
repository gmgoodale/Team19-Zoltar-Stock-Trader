from keras.models import Sequential
from keras.layers import Dense
import os

# This turns of the use of AVX, AVX2 and FMA which are instructionset extions
# for vector operations. If you have a GPU or are not concerned with performance
# leave this off since GPU will run most expensive instructions. If you want to
# use AVX or FMA, do a more advanced build of TF here https://stackoverflow.com/questions/41293077/how-to-compile-tensorflow-with-sse4-2-and-avx-instructions
# or use this git issue here https://github.com/tensorflow/tensorflow/issues/8037
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

model = Sequential()

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
