import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.tanh(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.title('Graph of Hyperbolic Tangent Function')
plt.grid(True)
plt.show()