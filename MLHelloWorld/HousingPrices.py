import tensorflow as tf
import numpy as np
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

model.compile(optimizer='sgd', loss='mean_squared_error')

xs = ([1, 2, 3, 4, 5])

ys = ([1.0, 1.5, 2.0, 2.5, 3.0])

model.fit(xs, ys, epochs=500)

print(model.predict([7.0]))