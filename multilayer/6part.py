"""
this file contains a basic activation function implementation
"""

import numpy as np
import matplotlib.pyplot as plt
import nnfs

class Layer:
    def __init__(self, number_inputs, number_neurons):
        self.weights = np.random.randn(number_inputs, number_neurons)
        self.bias = np.zeros((1, number_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.bias


class Activation:
    def forward(self, inputs):
        #self.output = np.maximum(0, inputs)    # linear function
        #self.output = math.e ** inputs          # eulers activation
        self.output = np.exp(inputs)


#########################################
#########################################
########## initializations ##############
inputDataset = [[1,2,3,0.15,5],
                [2,4,1,5,2],
                [235,56,87,47,0.4] ]
################################################ trouble with norm_values
#inputDataset = [4.8, 1.21, 2.385]

layer1 = Layer(5, 10)
#layer2 = Layer(10,2)
layer1ACT = Activation()

## options
np.set_printoptions(precision=3, suppress=True)



#########################################
#########################################
########## process the neurons ##########

layer1.forward(inputDataset)
print("layer forward:\n", layer1.output, "\n\n===========")

layer1ACT.forward(layer1.output)
print("layer1 activation:\n", layer1ACT.output, "\nshape: ", layer1ACT.output.shape, "\n\n========")

# normalization
norm_base = np.sum(layer1ACT.output, axis=1)
print("normbase = ", norm_base)

################################################ trouble with norm_values
#norm_values = layer1ACT.output / np.sum(layer1ACT.output, axis=0)
#print(norm_values)
