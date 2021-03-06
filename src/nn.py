import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU
##
import pandas as pd 
import pdb
import numpy as np
import random
import math
import argparse
import tensorflow as tf 
import matplotlib.pyplot as plt
from keras import losses
from keras import models
from keras import regularizers
from keras.layers.core import Dense
from keras.layers.core import Dropout
from keras.layers.core import Flatten
from keras.layers.recurrent import LSTM
from keras.layers.recurrent import GRU
from keras.layers.convolutional import Conv1D
from keras.callbacks import TensorBoard
from tensorflow.keras.optimizers import Adam
from keras.layers.advanced_activations import LeakyReLU
from shutil import copyfile
import pandas as pd
##

# Neural network
def train_network(params_dict, train_X, train_Y):
    '''
    inputs: parameters dictionary contianing layer values, mapping by indicies
    outputs:
    '''
    # model = Sequential()
    # model.add(Dense(1, input_dim=input_dim))
    # # model.add(Dense(16, input_dim=20, activation=’relu’))
    # model.add(Dense(12, activation=’relu’))
    # model.add(Dense(4, activation=’softmax’))

    num_inputs = params_dict["num_inputs"]
    layer_sizes = params_dict["layer_sizes"]

    model = Sequential()
    model.add(Dense(num_inputs)) #, input_shape=(input_dim,))) # params_dict["num_inputs"]
    model.add(LeakyReLU(alpha=0.03))

    for size in layer_sizes:
        model.add(Dense(size))
        model.add(LeakyReLU(alpha=0.03))
    
    model.add(Dense(1))

    model.compile(loss='mse', optimizer=Adam(lr=0.01), metrics=['mse'])

    if("epochs" in params_dict):
        model.fit(train_X, train_Y, epochs=params_dict["epochs"])
    else:
        model.fit(train_X, train_Y, epochs=300)

    return model

# For users that dont want to specify network specific params
def mlp_network(params_dict, train_X, train_Y):
    num_inputs = params_dict["num_inputs"]
    return train_network({"num_inputs" : num_inputs, "layer_sizes": [10, 10, 6], "epochs": 100}, train_X, train_Y)


# train_X = [1, 2, 3]
# train_Y = [4, 5, 6]

def test_network(test_X, model): 
    return model.predict(test_X)

# test sine
def test():
    # lindata = pd.read_csv('../traindata/lindata.csv')
    # lindata = np.genfromtxt('../traindata/lindata.csv')
    sine_train_data = np.genfromtxt('../traindata/sine_train_data.csv')
    sine_test_data = np.genfromtxt('../traindata/sine_test_data.csv')

    # train_X = lindata[:, 0]
    # train_Y = lindata[:, 1]

    train_X = sine_train_data[:, 0]
    train_Y = sine_train_data[:, 1]

    # model = train_network({"num_inputs": 1, "layer_sizes": [100], "epochs": 200}, train_X, train_Y)
    model = mlp_network({"num_inputs": 1}, train_X, train_Y)
    # model = train_network({}, train_X, train_Y)


    test_Y = test_network(train_X, model)
    print(test_Y)