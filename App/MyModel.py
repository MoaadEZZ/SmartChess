import tensorflow as tf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from text2vec import *



chatBotModel = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=()),
    tf.keras.layer.Dense(32),
    tf.keras.layer.Activation("relu"),
    tf.keras.layer.dense(3),
    tf.keras.layer.Activation("softmax")
])


