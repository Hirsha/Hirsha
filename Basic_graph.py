import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-100, 100, 1000)
y = np.tanh(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.title('Graph of Hyperbolic Tangent Function')
plt.grid(True)
plt.show()