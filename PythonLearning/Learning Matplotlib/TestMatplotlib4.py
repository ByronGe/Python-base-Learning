import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2


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
q, = plt.plot(x,y1,label='y=x',linewidth=10)
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='blue',edgecolor='None',alpha=0.7))





plt.show()