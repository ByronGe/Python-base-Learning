import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


plt.subplot(211)
plt.plot([0,1],[0,1])
plt.subplot(234)
plt.plot([0,2],[0,2])
plt.subplot(235)
plt.plot([0,3],[0,3])
plt.subplot(236)

plt.plot([0,4],[0,4])
plt.show()