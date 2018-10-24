import numpy as np
from random import randint
import math


# Cada linha da matriz é uma camada e cada coluna os pesos

class NeuralNetwork:
    actual_id = 0
    def __init__(self, weights=None, max_depth=1, max_width=10, input_size=12, output_size=4, actions=["up", "right", "down", "left"], new_neural_net=True):
        self.max_depth = max_depth
        self.max_width = max_width
        self.input_size = input_size
        self.output_size = output_size
        self.weights = []
        self.id = NeuralNetwork.actual_id
        NeuralNetwork.actual_id += 1

        self.actions = actions
        self.depth = self.max_depth
        self.width = self.max_width
        if new_neural_net:
            self.setweights()
        else:
            self.weights = weights

    def setweights(self):

        self.weights.append(2 *  np.random.random_sample((self.input_size, self.width)) - 1)

        for _ in range(self.depth - 1):
            self.weights.append(2 * np.random.random_sample((self.width, self.width)) - 1)

        self.weights.append(2 * np.random.random_sample((self.width, self.output_size)) - 1)

    def feedforward(self, input_data):
        sigmoid_v = np.vectorize(self.sigmoid)
        result_layer = input_data

        for weight in self.weights:
            result_layer = sigmoid_v(np.dot(result_layer, weight))
        return result_layer

    def setscore(self, score):
        self.score = score

    def nextaction(self, input_data):
        result = np.argmax(self.feedforward(input_data), axis=1)[0]
        return self.actions[result]

    def sigmoid(self, x):
        return 1 / (1 + math.exp(-x))

