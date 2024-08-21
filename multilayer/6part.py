"""
this file contains a basic activation function implementation
"""

import numpy as np
import matplotlib.pyplot as plt
import math


class Layer:
    def __init__(self, number_inputs, number_neurons):
        self.weights = np.random.randn(number_inputs, number_neurons)
        self.bias = np.zeros((1, number_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.bias


class Activation:
    def forward(self, inputs):
        #self.output = np.maximum(0, inputs)    # linear function
        self.output = math.e ** inputs          # eulers activation


#########################################
#########################################
########## initializations ##############
inputDataset = [[1,2,3,0.15,5],
                [2,4,1,5,2],
                [235,56,87,47,0.4] ]

layer1 = Layer(5, 10)
#layer2 = Layer(10,2)
layer1ACT = Activation()


#########################################
#########################################
########## process the neurons ##########

layer1.forward(inputDataset)
print("layer forward:\n", layer1.output, "\n\n===========")

layer1ACT.forward(layer1.output)
print("layer1 activation:\n", layer1ACT.output, "\n\n========")
