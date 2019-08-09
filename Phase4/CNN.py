#Provided by <Practical Machine Learning and Image Processing> Himanshu Singh 2019
#Modified by Jian Gao
#Date: July, 2019

import pandas as pd
import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

def Call_CNN():
    input_data = pd.read_csv("./MNIST/Train.csv")
    y = input_data['label']
    input_data.drop('label',axis=1,inplace = True)
    X = input_data
    y = pd.get_dummies(y)
    classifier = Sequential()
    classifier.add(Dense(units = 300, kernel_initializer ='uniform', activation = 'relu', input_dim = 32256))
    classifier.add(Dense(units = 200, kernel_initializer ='uniform', activation = 'relu'))
    classifier.add(Dense(units = 100, kernel_initializer ='uniform', activation = 'relu'))
    classifier.add(Dense(units = 9, kernel_initializer ='uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'sgd', loss = 'mean_squared_error', metrics = ['accuracy'])
    classifier.fit(X, y, batch_size = 10, epochs = 30)

    test_data = pd.read_csv("./Test/Test.csv")
    y_pred = classifier.predict(test_data)
    np.savetxt("result.csv", y_pred, delimiter=",")
