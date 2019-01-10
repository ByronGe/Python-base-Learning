import numpy as np
import matplotlib.pyplot as plt

x=np.array([[1,1,0,1,0,0],
            [1,0,1,0,0,1],
            [1,0,0,0,0,0],
            [1,1,1,1,1,1]])

y=np.array([1,1,-1,-1])
w=(np.random.random(6)-0.5)*2
lr = 0.11
O=0
def update():
    global x,y,lr,w
    O=np.dot(x,w.T)
    w_c = lr*(y-O.T).dot(x)/x.shape[0]
    w=w+w_c
for _ in range(1000):
    update()

x1=[0,1]
y1=[1,0]
x2=[0,1]
y2=[0,1]
def calculate(x,root):
    a = w[5]
    b = w[2] + x * w[4]
    c = w[0] + x * w[1] + x * x * w[3]
    if root == 1:
        return (-b + np.sqrt(b * b - 4 * a * c)) / (2 * a)
    if root == 2:
        return (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)

xdata = np.linspace(-1,2)
plt.figure()
plt.plot(xdata,calculate(xdata,1),'r')
plt.plot(xdata,calculate(xdata,2),'b')
plt.plot(x1,y1,'bo')
plt.plot(x2,y2,'yo')
plt.show()