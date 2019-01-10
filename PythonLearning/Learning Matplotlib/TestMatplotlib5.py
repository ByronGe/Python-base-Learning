import matplotlib.pyplot as plt
import numpy as np

a=1000
X=np.random.normal(0,1,a)
Y=np.random.normal(0,1,a)
n=np.arctan2(X,Y)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.scatter(X,Y,s=75,c=n,alpha=0.5)
plt.bar(X,Y)
plt.xlabel(())
plt.ylabel(())
plt.show()