import numpy as np

inputs = [
    [1,2,3,2.5],
    [2.,5., -1. , 2],
    [-1.5, 2.7, 3.3, -0.8]
]
weights1 = [
    [0.2,0.8,-0.5,1],
    [0.5 , -0.91 , 0.26,-0.5],
    [-0.26 , -0.27 , 0.17 , 0.87]
]
bias1 = [2,3,0.5]
# that is all we need for layer 1 


# layer 2 begain here 
weights2 = [
    [0.1,-0.14,0.5],
    [-0.5,0.12,-0.33],
    [-0.44,0.73,-0.13]
]
bias2 = [-1 , 2 , -0.5]
# layer 2 use layer 1 as inputs and i have own weights and bias 

layer1_output = np.dot(inputs , np.array(weights1).T) +bias1

layer2_output = np.dot(layer1_output , np.array(weights2).T) + bias2

print(layer2_output)