from main import *
from NeuralNetwork import *
import operator
import random
import copy




# todas as regras do AG estão bem fracas, só teste por enquanto


class Train():

    def __init__(self, count=3, best_ind=1, lucky=1):
        self.count = count
        self.best_ind = best_ind
        self.lucky = lucky

    def createpopulation(self):
        self.neural_net = []
        for _ in range(self.count):
            self.neural_net.append(NeuralNetwork())

    def call(self):
        for _ in range(30):
            for net in self.neural_net:
                net.setscore(run(net))
            population = self.selectbest(self.sortnets())
            population = self.breed(population)
            population = self.mutation(population)
            self.neural_net = population

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

        # casamento entre 0 e 1, 2 e 3, ...
        for i in range(0, self.best_ind + self.lucky - 1, 2):

            # seleciona uma camada e um neurônio dessa camada aleatóriamente
            rand_layer = randint(0, 9)
            rand_neuron = randint(0, population[i].max_width - 1)

            # primeiro filho -> cópia identica do pai, porém com os pesos de um único neurônio  herdados da mãe
            new_weight = copy.deepcopy(population[i].weights)
            new_weight[rand_layer][:, rand_neuron] = population[i+1].weights[rand_layer][:, rand_neuron]
            population.append(NeuralNetwork(weights=new_weight ,new_neural_net=False))

            # segundo filho -> cópia identica da mãe, porém com os pesos de um único neurônio herdados do pai
            new_weight = copy.deepcopy(population[i + 1].weights)
            new_weight[rand_layer][:, rand_neuron] = population[i].weights[rand_layer][:, rand_neuron]
            population.append(NeuralNetwork(weights=new_weight ,new_neural_net=False))
        
        return population
    
    def mutation(self, population):
        # seleciona uma rede aleatória, uma camada e um único peso
        choosen_net = randint(0, len(population) - 1)
        rand_layer = randint(0, 9)
        rand_neuron = randint(0, population[choosen_net].max_width - 1)
        rand_weight = randint(0, population[choosen_net].weights[rand_layer].shape[0] - 1)

        # torna o sinal negativo
        population[choosen_net].weights[rand_layer][rand_weight, rand_neuron] *= -1

        return population



train = Train()
train.createpopulation()
train.call()

