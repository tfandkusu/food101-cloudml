import numpy as np
import tensorflow as tf
import data

def decode(image_str_tensor):
    "画像1枚分のPNGデータをデコードする関数"
    image_str_tensor = tf.reshape(image_str_tensor,[])
    image = tf.image.decode_png(image_str_tensor,channels=3)
    x = tf.cast(image,tf.float32)
    return x

def decode_layer(x):
    "PNGデータをデコードするラムダレイヤーの関数"
    x = tf.map_fn(decode, x,dtype=tf.float32)
    return x

def make():
    "モデルを作成する"
    # PNGデータをデコードするモデル
    decode_model = tf.keras.models.Sequential()
    decode_model.add(tf.keras.layers.Lambda(decode_layer,
        input_shape=[None],dtype=tf.string))
    # 分類するモデル
    mobilenet = tf.keras.applications.MobileNet(
        input_shape=(224,224,3),
        alpha=0.5,weights=None, classes=101)
    # 2つをつなぐ
    return tf.keras.models.Sequential([decode_model,mobilenet])
