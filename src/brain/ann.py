"""
Igor Busquets LML
"""

# Artifficial Neural Networks

# DEPENDENCIES
import numpy as np
#import matplotlib.pyplot as plt
#import pandas as pd

import tensorflow as af
from sklearn.model_selection import train_test_split
# ARTIFICIAL NEURAL NETWORK IMPLEMENTATION
#Sequencial - Initializes the Neural Network
from keras.models import Sequential
#Dense - Build the layers of the ANN
from keras.layers import Dense


    # Splitting the dataset into the Training set and Test set
    #from sklearn.model_selection import train_test_split
    #X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size = 0.2, )


# DATA PREPROCESSING
# Importing the dataset
class Network:
    def __init__(self):
        self.init_network()
        # X features
        # y target
        self.X = []
        self.y = []
        self.y_pred = 0

    # ARTIFICIAL NEURAL NETWORK IMPLEMENTATION
    #Sequencial - Initializes the Neural Network
    #Add input and first hidden layers
    #theres 5 inputs X and only 1 output y
    #output_dim = number of nodes in the layer  = avg of input x and output y so avg(1,11)=6
    #input_dim is compulsory to first layer onlym, because it doesnt know how many X it will recieve

    #Complle the ANN = Apply Stochastic Gradient Descent
    #adam = type of Stochastic Gradient Descent
    # loss = same as logistic regression - logaritic loss 
    #metrics = crteria for evaluate model, criteria is accuracy...a array is expected

    def init_network(self):        
        self.classifier = Sequential()
        self.classifier.add(Dense(activation = 'relu', input_dim = 6, units = 6, kernel_initializer ='uniform' ))
        #Add second hidden layer
        self.classifier.add(Dense(activation = 'relu', units = 6, kernel_initializer ='uniform', ))
        #Add the output layer
        self.classifier.add(Dense(activation = 'sigmoid', units = 1, kernel_initializer ='uniform', ))
        self.classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'] )

        # TRAINING
        #Fitting the ANN to traningset
        #X_train, X_test, y_train, y_test = train_test_split(self.X, self.y, test_size = 0.2, )    
    def train(self, observation_array):
        print("training")
        self.X = observation_array.iloc[:, 0:5].values
        self.classifier.fit(self.X , self.y, batch_size = 1, epochs = 10)

        
        #PREDICTION
    def predict(self):
        self.y_pred = self.classifier.predict(self.X)
        return self.y_pred
        #change predictions to 1 or 0 values with a treshold
        #y_pred = (y_pred  > 0.5)


    # # Making the Confusion Matrix
    # from sklearn.metrics import confusion_matrix
    # cm = confusion_matrix(y_test, y_pred)

    # #short evalualion, returns [loss_func, accuracy]
    # self.classifier.evaluate(X_train, y_train, batch_size=10, verbose=1)
    # self.classifier.summary()
