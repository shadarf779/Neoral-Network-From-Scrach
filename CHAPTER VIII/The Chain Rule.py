import numpy as np

# Example dimensions
m, n = 5, 10  # 5 samples, 10 features
h1, h2 = 8, 6  # 8 neurons in the first hidden layer, 6 in the second hidden layer
c = 3  # 3 classes

# Example input data
X = np.random.randn(m, n)

# Example weights and biases
w1 = np.random.randn(h1, n)
b1 = np.random.randn(h1)

w2 = np.random.randn(h2, h1)
b2 = np.random.randn(h2)

w3 = np.random.randn(c, h2)
b3 = np.random.randn(c)

# Example one-hot encoded labels
y = np.eye(c)[np.random.choice(c, m)]

# Calculate the loss
loss = -np.log(
    np.sum(
        y * np.exp(
            np.dot(
                np.maximum(
                    0,
                    np.dot(
                        np.maximum(
                            0,
                            np.dot(X, w1.T) + b1
                        ),
                        w2.T
                    ) + b2
                ),
                w3.T
            ) + b3
        ) /
        np.sum(
            np.exp(
                np.dot(
                    np.maximum(
                        0,
                        np.dot(
                            np.maximum(
                                0,
                                np.dot(X, w1.T) + b1
                            ),
                            w2.T
                        ) + b2
                    ),
                    w3.T
                ) + b3
            ),
            axis=1,
            keepdims=True
        )
    )
)

print("Loss:", loss)
