import nnfs


import matplotlib.pyplot as plt 
from nnfs.datasets import spiral_data

# Generate the spiral data
X, y = spiral_data(samples=100, classes=3)

# You can remove (), c=y, cmap='brg') it is just for coloring 
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
plt.show()
