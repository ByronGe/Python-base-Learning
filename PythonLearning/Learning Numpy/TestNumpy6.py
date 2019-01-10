import numpy as np

a=np.array([1,1,1])
b=np.array([2,2,2])
print(a)
print(b)
c=np.vstack((a,b))
d=np.hstack((a,b))
print(c)
print(d)
print(a.shape,c.shape,d.shape)
