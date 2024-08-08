import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = 1 / np.tanh(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('coth(x)')
plt.title('Graph of Hyperbolic Cotangent Function')
plt.grid(True)
<<<<<<< HEAD
plt.show()

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('tanh(x)')
plt.title('Graph of Hyperbolic Tangent Function')
plt.grid(True)
=======
>>>>>>> b9df6e35e3a4593cc2d8a79e12a459220ac5e08e
plt.show()