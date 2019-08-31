import tensorflow as tf
from cabbage.model import CabbageModel
import numpy as np

class CabbageController:
    def __init__(self, avg_temp, min_temp, max_temp, rain_fall):
        self._avg_temp = avg_temp
        self._min_temp = min_temp
        self._max_temp= max_temp
        self._rain_fall = rain_fall

    def service(self):
        #NONE -> 행 값
        #4 -> 열 값
        X = tf.placeholder(tf.float32, shape=[None,4])
        #Y는 미래의 값이기 때문에 현재 존재할 수 가없다. Y의 값을 예측하는 것
        W = tf.Variable(tf.random_normal([4,1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        saver = tf.train.Saver()
        #텐서 세션의 영역
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            saver.restore(sess, 'cabbage/saved_model/saved.ckpt')
            #매트릭스 구조
            data = [[self._avg_temp, self._min_temp, self._max_temp, self._rain_fall],]
            arr = np.array(data, dtype = np.float32)
            dict = sess.run(tf.matmul(X,W) +b,{X: arr[0:4]})
        return dict[0]
