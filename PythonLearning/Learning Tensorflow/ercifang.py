import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


x_data=np.linspace(-1,1,200)[:,np.newaxis]
noise = np.random.normal(0,0.02,x_data.shape)
y_data=np.square(x_data)+noise

x=tf.placeholder(tf.float32,[None,1])
y=tf.placeholder(tf.float32,[None,1])

#定义神经网络中间层

Weight = tf.Variable(tf.random_normal([1,10]))
biases = tf.Variable(tf.zeros([1,10]))
Wx_plus_b_L1=tf.matmul(x,Weight)+biases
L1 = tf.nn.tanh(Wx_plus_b_L1)

WeightL2=tf.Variable(tf.random_normal([10,1]))
biasesL2=tf.Variable(tf.zeros(1,1))
Wx_plus_b_L2=tf.matmul(L1,WeightL2)+biasesL2
prediction = tf.nn.tanh(Wx_plus_b_L2)

loss = tf.reduce_mean(tf.square(y-prediction))

train = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for _ in range(200):
        sess.run(train,feed_dict={x:x_data,y:y_data})
    prediction_value = sess.run(prediction,feed_dict={x:x_data})

    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction_value,'r-',lw=5)
    plt.show()

