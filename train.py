from main import *
from NeuralNetwork import *
import operator
import random

class Train():

    def __init__(self, count=4, best_ind=2, lucky=0):
        self.count = count
        self.best_ind = best_ind
        self.lucky = lucky

    def createpopulation(self):
        self.neural_net = []
        for _ in range(self.count):
            self.neural_net.append(NeuralNetwork())

    def call(self):
        for net in self.neural_net:
            net.setscore(run(net))
        population = self.selectbest(self.sortnets())
        self.breed(population)

    def sortnets(self):
        sorted_population = {}
        for individual in self.neural_net:
            sorted_population[individual] = individual.score
        return sorted(sorted_population.items(), key=operator.itemgetter(1), reverse=True)

    def selectbest(self, sorted_population):
        next_generation = []
        for i in range(self.best_ind):
            next_generation.append(sorted_population[i][0])
        
        for i in range(self.lucky):
            next_generation.append(random.choice(sorted_population)[0])

        return next_generation

    def breed(self, population):
        for i in range(0, self.best_ind + self.lucky - 1, 2):
            rand_layer = randint(0, 2)
            rand_neuron = randint(0, population[i].max_width - 1)
            new_weight = np.empty_like (population[i].weights)
            np.copyto(new_weight, population[i].weights)
            #new_weight[rand_layer][:, rand_neuron] = population[i+1].weights[rand_layer][:, rand_neuron]
            if (i == 0):
                print("CAMADA={}NEURONIO={}\n".format(rand_layer, rand_neuron))
                print(population[i].weights[rand_layer])
                print(new_weight[rand_layer])
                print(new_weight[rand_layer][:, rand_neuron])
                print(population[i+1].weights[rand_layer][:, rand_neuron])
                print("\n\n")
            #population.append(NeuralNetwork(weights=new_weight ,new_neural_net=False))
            new_weight = np.empty_like (population[i + 1].weights)
            np.copyto(new_weight, population[i + 1].weights)
            new_weight[rand_layer][:, rand_neuron] = population[i].weights[rand_layer][:, rand_neuron]
            if (i == 0):
                print(population[i + 1].weights[rand_layer])
                print(new_weight[rand_layer])
                print(new_weight[rand_layer][:, rand_neuron])
                print(population[i].weights[rand_layer][:, rand_neuron])
                print("\n\n")
            #population.append(NeuralNetwork(weights=new_weight ,new_neural_net=False))

        print(len(population))

train = Train()
train.createpopulation()
train.call()

