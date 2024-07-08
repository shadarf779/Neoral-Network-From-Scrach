import numpy as np

layer_outputs = np.array([
    [4.8,1.21,2.385],
    [8.9,-1.81,0.2],
    [1.41,1.051,0.026]
])
print('sum without axis: ' , np.sum(layer_outputs))


print('axis is None that mean it doesnt caculate Axis: ' , np.sum(layer_outputs , axis=None))