import numpy as np

layer_outputs = np.array([
    [4.8,1.21,2.385],
    [8.9,-1.81,0.2],
    [1.41,1.051,0.026]
])

for i in layer_outputs:
    print('sum with X axis: ' , np.sum(i))

print('sum with X axis: ' , np.sum(layer_outputs , axis=1))
#or
print('Or this way: ' , np.sum(layer_outputs , axis=1 ,keepdims=True))
