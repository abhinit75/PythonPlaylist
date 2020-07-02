import tensorflow as tf
import numpy as np
import keras


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=()):
        if logs.get('loss') < 0.4:
            print("\nLoss is low so cancelling training")
            self.model.stop_training = True


callbacks = myCallback()
fashion_mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = fashion_mnist.load_data()

training_images = training_images / 255.0
test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # Takes images and converts into linear values
    keras.layers.Dense(128, activation=tf.nn.relu),  # Middle Layer --> Hidden Layer
    keras.layers.Dense(10, activation=tf.nn.softmax)
])

'''
Sequemtial: defines the sequence of the layers in the neural network
Flatten: Flatten takes squares or multi-dimensional images in 1 dimensional sets
Dense: Adds a new layer of neurons
Relu: Effectively means "If X>0 return X, else return 0" - so what it doe sis it passes values only greater than 0
Softmax: takes a set of values, and effectively picks the biggest one, so, for example, if the output of the last layer looks like [0.1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05], it saves you from fishing through it looking for the biggest value, 
and turns it into [0,0,0,0,1,0,0,0,0] -- The goal is to save a lot of coding!
'''

model.compile(optimizer=tf.train.AdamOptimizer(),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])

model.evaluate(test_images, test_labels)
'''
https://colab.research.google.com/github/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%204%20-%20Lesson%202%20-%20Notebook.ipynb#scrollTo=WnBGOrMiA1n5

'''




