import numpy as np



x=np.linspace(-1,1,50)[:,np.newaxis]
y=np.square(x)

noise = np.random.normal(3)
index=0
z=[-x for x in range(10)]
while index<len(z):
    z=z[index:index+2]
    index +=2
print(z)

