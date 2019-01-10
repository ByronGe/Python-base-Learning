import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth=3,linestyle='--')
x_tick = np.linspace(-2,2,6)
plt.xlabel('i am xlabel')
plt.xticks(x_tick)
plt.yticks([0,2,4,7,8],[r'$terrible$','bad','normal','good','really good'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))
plt.show()