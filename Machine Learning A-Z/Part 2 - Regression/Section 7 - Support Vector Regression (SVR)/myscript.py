#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:53:33 2018

@author: saurav
"""

#%% Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#%% Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values # making sure X is matrix, not array
y = dataset.iloc[:, 2:3].values

#%% Feature Scaling
# standardization
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

#%% Fitting SVR to the dataset
y = np.squeeze(np.asarray(y))
from sklearn.svm import SVR
regressor = SVR(kernel='rbf')
regressor.fit(X,y)

#%% Predicting a new result
X_pred = np.array(6.5).reshape(-1,1)
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform(X_pred)))

#%% Visualizing the SVR results
plt.scatter(X,y,color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Truth or Bluff (SVR Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show() 