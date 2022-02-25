import matplotlib.pyplot as plt
import numpy as np

x_from = 0.
x_to = 10.
x_step = 0.1

plt.title('Sin(x)')  # Title

x = np.arange(x_from, x_to, x_step)  # Created in 0.1 increments from 0 to 10
y = np.sin(x)  # Create a sine coordinate sequence from the x coordinate sequence

plt.plot(x, y)  # Drawing a graph
plt.show()  # Graph display