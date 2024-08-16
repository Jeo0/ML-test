"""
from https://www.youtube.com/watch?v=lGLto9Xd7bU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=2
@ 11:46
the output should be 4.8, 1.21, 2.385

this file contains a simple implmentation of calcualting the outputs of one layer with 
dyanmically (multiple input neurons and output neurons) numbered neurons
"""

def onelayer(ar1, weightssss, bias):
    """
    ar1:    1D
    weightssss:    2D
    bias:   1D
    """

    output = []         # stores total output that will be returned by the end of the functioncall
    cache = []          # temporary small storage
    summation = 0       # temporary storage
    weight_index = 0            # temporary iterator
    neuron_index = 0            # temporary iterator

    quantityInputs = len(ar1)       # number of input neurons
    bias_size = len(bias)           # number of output neurons


    # parsing and making calculations
    for neuron in weightssss:
        for weight in neuron:
            summation += (ar1[weight_index]*weight)
            weight_index += 1
        summation += bias[neuron_index]

        # store it in cache
        cache.append(summation)

        # reset weightindex  and summation for the next loop
        summation = 0
        weight_index = 0
        neuron_index +=1

    # must output: an array that contains objects
    # quantity: the number of output neurons
    return cache



if __name__ == "__main__":
    inputs = [1,2,3,2.5]

    weights = [[0.2,0.8,-0.5,1.],
               [0.5,-0.91,0.26,-0.5],
               [-0.26,-0.27,0.17,0.87]
            ]
    bias = [2,3,0.5]
    print(onelayer(inputs, weights, bias))

