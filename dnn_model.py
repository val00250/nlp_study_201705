# -*- coding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding
from keras.layers import Convolution1D, MaxPooling1D
from keras.layers.recurrent import LSTM

# https://hogehuga.com/post-1464/

def create_model(max_features):
    """
        max_features = 正の整数．語彙数．入力データの最大インデックス + 1
    """

    model = Sequential()
    model.add(Embedding(max_features, output_dim=256))
    model.add(LSTM(128))

    #出力層
    model.add(Dense(1))
    model.add(Activation('linear'))

    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

    return model