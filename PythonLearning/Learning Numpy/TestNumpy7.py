import numpy as np

a=np.array([1,1,1])
b=np.array([2,2,2])
print(a)
print(b)
c=a[:,np.newaxis]
d=b[:,np.newaxis]
print(c)
print(np.concatenate((d,d,c,c),axis=1))