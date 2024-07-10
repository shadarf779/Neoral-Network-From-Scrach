import matplotlib.pyplot as plt
import numpy as np

# Define the function f(x)
def f(x):
    return 2*x**2

# Generate x values
x = np.arange(0, 5, 0.001)
y = f(x)

# Plot the function f(x)
plt.plot(x, y)

# Parameters for the tangent line
p2_delta = 0.0001
x1 = 2
x2 = x1 + p2_delta

# Calculate y values at x1 and x2
y1 = f(x1)
y2 = f(x2)

# Print the points
print((x1, y1), (x2, y2))

# Calculate the approximate derivative (slope of the tangent line)
approximate_derivative = (y2 - y1) / (x2 - x1)

# Calculate the y-intercept of the tangent line
b = y1 - approximate_derivative * x1

# Define the tangent line function
def tangent_line(x):
    return approximate_derivative * x + b

# Plot the tangent line near x1
to_plot = [x1 - 0.9, x1, x1 + 0.9]
plt.plot(to_plot, [tangent_line(i) for i in to_plot], label='Tangent line at x=2')

# Print the approximate derivative
print(f'Approximate derivative for f(x) where x = {x1} is {approximate_derivative}')

# Show the plot
plt.legend()
plt.show()
