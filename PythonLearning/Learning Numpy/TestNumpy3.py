import numpy as np
a=np.array([
    [1,2],
    [3,4]
])
b=np.arange(4).reshape((2,2))
print(a)
print(b)
print(a*b)
print(a.dot(b))
print(np.max(a))
print(a>2)