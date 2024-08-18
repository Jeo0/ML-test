"""
continuation of the yt sentdex neuron series
part 4

this file contains the implementation of 
- layer input and output
"""

import numpy as np

class Layer:
    def __init__(self, number_inputs, number_neurons):
        self.weights = np.random.randn(number_inputs, number_neurons)
        #self.biases = np.zeros((1, number_neurons))
        self.biases = np.random.rand(1, number_neurons)

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


if __name__ == "__main__":
    np.random.seed(0)
    inputLayer = np.array([[1., 0.2,    4., 255],
                           [0.2, 140,   0.3, 255],
                           [60, 100,    1., 40] ])
    """
    inputLayer = [[1., 0.2,4., 255],
                  [0.2, 140, 0.3, 255],
                  [60, 100, 1., 40] ]
    """
    print("inputs:\n", inputLayer, "\n\n")

    layer1 = Layer(4, 3)
    layer2 = Layer(3, 5)
    
    layer1.forward(inputLayer)
    print("layer1:\n", layer1.output, "\n\n")

    layer2.forward(layer1.output)
    print("layer2:\n", layer2.output, "\n\n")




