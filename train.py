from main import *
from NeuralNetwork import *
import operator
import random
import copy


# todas as regras do AG estão bem fracas, só teste por enquanto


class Train():

    def __init__(self, count=100, best_ind=32, lucky=6, mutation_rate=0.1):
        self.count = count
        self.best_ind = best_ind
        self.lucky = lucky
        self.mutation_rate = mutation_rate
        self.best_score = 0
        self.gen_without_improv = 0

    def createpopulation(self):
        self.neural_net = []
        for _ in range(self.count):
            self.neural_net.append(NeuralNetwork())

    def fitness(self, params):
        return 10 * params[0] + 5 * params[1]


    def call(self):
        population = []
        for i in range(50000):
            print("GENERATION={}\n".format(i))
            for net in self.neural_net:
                net.setscore(self.fitness(run(net, True)))

            population = self.selectbest(self.sortnets())
            
            
            if(population[0].score > self.best_score):
                self.best_score = population[0].score
                self.gen_without_improv = 0
            else:
                self.gen_without_improv += 1

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


    # Escolher os best_ind melhores indivíduos 
    # e os lucky sortudos (escolhidos aleatóriamente)
    # para compor a próxima geração
    def selectbest(self, sorted_population):
        next_generation = []
        if(self.gen_without_improv > 30):
            elitism = int(self.best_ind/4)
            lucky = self.lucky + self.best_ind - int(self.best_ind/4)
        else:
            elitism = self.best_ind
            lucky = self.lucky

        for i in range(elitism):
            next_generation.append(sorted_population[i][0])

        for i in range(lucky):
            next_generation.append(random.choice(sorted_population)[0])

        return next_generation


    # iremos escolher um peso da rede pai/mãe e será gerado dois filhos. Um possui todos os pesos do início até o peso selecionado
    # identicos aos do pai e o resto identicos aos da mãe. No segundo filho a regra se inverte
    #
    # ex: rede com 3 camadas ocultas, uma de saída, 4 inputs/outputs e 10 neurônios em cada camada oculta.
    # peso escolhido: Camada 2, neurônio 3, peso 5.
    # Filho 1: Camada 1 -> identica à do pai. Camada 2 até o neurônio 3 -> idêntica à do pai. Neurônio 3 até o peso 4 -> identico ao do pai.
    # Neurônio 3, a partir do peso 4 -> igual da mãe. Neurônio 4 até neurônio 10 -> Igual da mãe. Camadas 3 e de saída -> Iguais a da mãe
    # para o filho 2 o contrário
    def breed(self, population):

        # Podução de filhos entre os indivíduos 0 e 1, 2 e 3, ... da população
        for i in range(0, self.best_ind + self.lucky, 2):

            # seleciona uma camada, um neurônio dessa camada e um peso desse neurônio
            rand_layer = randint(0, population[i].max_depth)
            rand_neuron = randint(0, population[i].weights[rand_layer].shape[1] - 1)
            rand_weight = randint(0, population[i].weights[rand_layer].shape[0] - 1)

            # PRIMEIRO FILHO

            # new_weigth é uma cópia do pai
            new_weight = copy.deepcopy(population[i].weights)

            # todos os pesos, a partir do peso escolhido (inclusive), do neeurônio escolhido, na camada escolhida, será igual o da mãe
            #print(population[i + 1].weights[rand_layer][rand_weight:])
            new_weight[rand_layer][rand_weight:, rand_neuron] = copy.deepcopy(population[i + 1].weights[rand_layer][rand_weight:, rand_neuron])

            # todos os neurônios subsequentes, da mesma camada, serão iguais aos da mãe
            # é preciso verifica se o neurônio escolhido não era o último da camada. Se for, já estamos feitos com a camada escolhida. Shape[1] -> número de colunas (neurônios) da camada rand_layer
            if rand_neuron != (new_weight[rand_layer].shape[1] - 1): 
                new_weight[rand_layer][:, rand_neuron + 1:] = copy.deepcopy(population[i + 1].weights[rand_layer][:, rand_neuron + 1:])

            # todas as camadas subsequentes serão iguais as da mãe
            # é preciso verificar se a camada escolhida não é a última camada. Se for, já estamos feitos com a rede.
            if rand_layer != population[i].max_depth: 
                new_weight[rand_layer + 1:] = copy.deepcopy(population[i + 1].weights[rand_layer + 1:])

            # adiciona o novo filho na população após a mutação
            population.append(NeuralNetwork(weights=self.mutation(new_weight), new_neural_net=False))

            ##############################

            # SEGUNDO FILHO

            # mesma dinâmica do anterior
            new_weight = copy.deepcopy(population[i + 1].weights)

            new_weight[rand_layer][rand_weight:, rand_neuron] = copy.deepcopy(population[i].weights[rand_layer][rand_weight:, rand_neuron])

            if rand_neuron != (new_weight[rand_layer].shape[1] - 1): 
                new_weight[rand_layer][:, rand_neuron + 1:] = copy.deepcopy(population[i].weights[rand_layer][:, rand_neuron + 1:])

            if rand_layer != population[i + 1].max_depth: 
                new_weight[rand_layer + 1:] = copy.deepcopy(population[i].weights[rand_layer + 1:])

            population.append(NeuralNetwork( weights=self.mutation(new_weight), new_neural_net=False))

        # Adição de população aleatório caso o número de pais + filhos não alcancem o total de indivíduos necessários para uma geração
        for _ in range(self.count - 2 * (self.best_ind + self.lucky)): population.append(NeuralNetwork())

        return population



    # A mutação de um indivíduo se dá da seguinte forma:
    # Para todos os pesos desse indivíduo é calculado uma probabilidade de mutação. Caso essa probabilidade se relacione com o índice
    # de mutação, o valor do peso corrente será alterado, somando ou subtraindo um valor entre (0, 1) do peso corrente
    def mutation(self, individual):

        # para cada peso no indivíduo...
        for layer in individual:
            for i in range(layer.shape[1]):
                for j in range(layer.shape[0]):

                    # calcula-se a chance de mutaçao, se esta for inferior a taxa de mutação, o peso será alterado
                    chance = random.random()

                    if(self.gen_without_improv > 30):
                        mutation_rate = 2*self.mutation_rate
                    else:
                        mutation_rate = self.mutation_rate

                    if chance < mutation_rate:
                        # a variação do peso é escolhida e, existe uma change igual da soma ou subtração ser escolhida como operação de mutação
                        delta_value = random.random()
                        if(random.randint(0, 1) == 1):
                            layer[j][i] -= delta_value
                        else:
                            layer[j][i] += delta_value

        return individual


train = Train()
train.createpopulation()
train.call()
