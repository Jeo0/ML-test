def onelayer(ar1, weightssss, bias):
    """
    ar1:    1D
    weightssss:    2D
    bias:   1D
    """
    
    
    cache = []          # temporary small storage
    summation = 0       # temporary storage
    weight_index = 0            # temporary iterator
    neuron_index = 0            # temporary iterator



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


import matplotlib.pyplot as plt

if __name__ == "__main__":
    inputs = [1,2,3,2.5]
    for x in range(len(inputs)):
        inputs[x] /= 4

    weights = [[0.2,0.8,-0.5,1.],
               [0.5,-0.91,0.26,-0.5],
               [-0.26,-0.27,0.17,0.87]
            ]
    bias = [2,3,0.5]
    output = []
    
    weights2 = [[0.2,0.4,0.3],
    [0.2,0.9,-0.8],
    [0.3,0.5,0.7]]
    
    output.append(onelayer(inputs, weights, bias))
    print(output)



    x = output[0][0]
    y = output[0][1]
    z = output[0][2]

    ax = plt.figure().add_subplot(projection='3d')
    ax.quiver(0,0,0, x,y,z)

    # plotting
    ax.set_title('3D line plot geeks for geeks')
    plt.show()

