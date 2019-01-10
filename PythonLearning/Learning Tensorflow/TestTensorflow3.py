import tensorflow as tf

value = tf.Variable(0,name='count')
one = tf.constant(1)

new_value = tf.add(value,one)
update = tf.assign(value,new_value)

init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(new_value))