import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# tensorflow가 2.0으로 업그레이드 되면서 사용할 수 없는 attribute 생김.. 임시방편으로 버전 1.0을 사용할 수 있게 설정
from tensorflow.lite.python.lite import Optimize
# Ctrl+Shift+P 실행 > Python: Select Interpreter > Anaconda, Inc. Python 3.6.6
xData = [1,2,3,4,5,6,7]
yData = [25000,55000,75000,110000,128000,155000,180000]
W = tf.Variable(tf.random.uniform([1],-100,100))
b = tf.Variable(tf.random.uniform([1],-100,100))
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)
H = W + X + b
cost = tf.reduce_mean(tf.square(H - Y))
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(5000):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
print(sess.run(H, feed_dict={X: [8]}))