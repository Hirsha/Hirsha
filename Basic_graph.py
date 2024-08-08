import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = np.tan(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('tan(x)')
plt.title('Graph of Tangent Function')
plt.grid(True)
plt.show()