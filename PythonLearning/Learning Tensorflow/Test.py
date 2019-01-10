from __future__ import print_function
import tensorflow as tf
import numpy as np

x_data=np.linspace(-1,1,100)
y_data=x_data*0.1+0.3
Weights=tf.Variable(tf.random_uniform([1],-1,1))
biases = tf.Variable(tf.zeros([1]))
y=x_data*Weights+biases

loss=tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
for i in range(200):

















    f







    sess.run(train)
    if i%10==0:
        print(i, sess.run(Weights), sess.run(biases))