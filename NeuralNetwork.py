import numpy as np
from random import randint
import math


# Cada linha da matriz é uma camada e cada coluna os pesos

class NeuralNetwork:
    def __init__(self, weights=None, max_depth=2, max_width=2, input_size=10, output_size=4, actions=["up", "right", "down", "left"], new_neural_net=True):
        self.max_depth = max_depth
        self.max_width = max_width
        self.input_size = input_size
        self.output_size = output_size
        self.weights = []

        self.actions = actions
        self.depth = self.max_depth
        self.width = self.max_width
        if new_neural_net:
            self.setweights()
        else:
            self.weights = weights

    def setweights(self):
        #self.depth = randint(1, self.max_depth)
        #self.width = randint(1, self.max_width)

        self.weights.append(np.random.rand(self.input_size, self.width))

        for _ in range(self.depth - 1):
            self.weights.append(np.random.rand(self.width, self.width))

        self.weights.append(np.random.rand(self.width, self.output_size))

    def feedforward(self, input_data):
        sigmoid_v = np.vectorize(self.sigmoid)
        result_layer = np.interp(input_data, (1, 26), (-1, +1))


        for weight in self.weights:
            result_layer = sigmoid_v(np.dot(result_layer, weight))
        return result_layer

    def setscore(self, score):
        self.score = score

    def nextaction(self, input_data):
        return self.actions[np.argmax(self.feedforward(input_data), axis=1)[0]]

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

