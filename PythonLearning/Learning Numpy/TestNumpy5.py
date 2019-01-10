import numpy as np

a=np.arange(2,11).reshape(3,3)
print(a)
print(np.transpose(a))
print(a.T)
print(np.nonzero(a))
print(np.cumsum(a))
print(np.mean(a))
print(np.argmax(a))
print(a[2])
for temp in a.T:
    print(temp)
