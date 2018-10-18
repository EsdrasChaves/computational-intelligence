from main import *
from NeuralNetwork import *
import operator
import random
import copy




# todas as regras do AG estão bem fracas, só teste por enquanto


class Train():

    def __init__(self, count=100, best_ind=40, lucky=10, mutation_rate=0.1):
        self.count = count
        self.best_ind = best_ind
        self.lucky = lucky
        self.mutation_rate = mutation_rate

    def createpopulation(self):
        self.neural_net = []
        for _ in range(self.count):
            self.neural_net.append(NeuralNetwork())

    def fitness(self, params):
        return 30 * params[0] + 5 * params[1]

    def call(self):
        for i in range(50):
            print("GENERATION={}\n".format(i))
            for net in self.neural_net:
                net.setscore(self.fitness(run(net, True)))

            population = self.selectbest(self.sortnets())
            population = self.breed(population)
            self.neural_net = population

            if i % 10 == 0:
                run(self.neural_net[0], False)

        run(self.neural_net[0], False)
        print("Best score = {}\n".format(self.neural_net[0].score))

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
        for i in range(0, int((self.best_ind + self.lucky)/2), 2):
            
            # seleciona uma camada e um neurônio dessa camada aleatóriamente
            rand_layer = randint(0, 1)
            rand_neuron = randint(0, population[i].weights[rand_layer].shape[1] - 1)

            # primeiro filho -> cópia identica do pai, porém com os pesos de um único neurônio  herdados da mãe
            new_weight = copy.deepcopy(population[i].weights)
            new_weight[rand_layer][:, rand_neuron] = population[(self.best_ind + self.lucky) - i -1].weights[rand_layer][:, rand_neuron]
            #new_weight[:int(len(new_weight)/2)] = population[i + 1].weights[:int(len(new_weight)/2)]
            population.append(NeuralNetwork(weights=self.mutation(new_weight) ,new_neural_net=False))

            # segundo filho -> cópia identica da mãe, porém com os pesos de um único neurônio herdados do pai
            new_weight = copy.deepcopy(population[i+ 1].weights)
            new_weight[rand_layer][:, rand_neuron] = population[i].weights[rand_layer][:, rand_neuron]
            #new_weight[:int(len(new_weight)/2)] = population[i].weights[:int(len(new_weight)/2)]
            population.append(NeuralNetwork(weights=self.mutation(new_weight) ,new_neural_net=False))
        
        for _ in range(self.count - 2 * (self.best_ind + self.lucky)):
            population.append(NeuralNetwork())
        
        return population
    

    # ver se está realmente mudando
    def mutation(self, individual):
        for layer in individual:
            for i in range(layer.shape[1]):
                for j in range(layer.shape[0]):
                    chance = random.random()
                    if chance < self.mutation_rate:
                        delta_value = random.random()
                        if(random.randint(0, 1) == 1):
                            layer[j][i] += delta_value
                        else:
                            layer[j][i] -= delta_value


        return individual
        #for i in population:
            # seleciona uma rede aleatória, uma camada e um único peso
            #choosen_net = randint(0, len(population) - 1)
            #rand_layer = randint(0, 1)
            #rand_neuron = randint(0, i.weights[rand_layer].shape[1] - 1)
            #rand_weight = randint(0, population[choosen_net].weights[rand_layer].shape[0] - 1)
            #if(random.random() > 0.5):
                #i.weights[rand_layer][:, rand_neuron] -= random.random() / 10
            #else:
                #i.weights[rand_layer][:, rand_neuron] *= -1
            # torna o sinal negativo
            # population[choosen_net].weights[rand_layer][rand_weight, rand_neuron] *= -1

        



train = Train()
train.createpopulation()
train.call()

