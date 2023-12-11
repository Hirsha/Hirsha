import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = 1 / np.tanh(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('coth(x)')
plt.title('Graph of Hyperbolic Cotangent Function')
plt.grid(True)
plt.show()
