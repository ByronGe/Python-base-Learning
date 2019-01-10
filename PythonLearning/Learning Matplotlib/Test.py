import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2)
y = np.arange(3)
print(x,y)
print('--------')
[X, Y] = np.meshgrid(x, y)
print(X)

plt.show()