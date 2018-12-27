#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 09:29:44 2018

@author: saurav
"""


# Data Preprocessing

#%% Importing the libraries

import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd

#%% Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

#%% Encoding the categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(
        [('onehot_enc', OneHotEncoder(),[3])],
        remainder='passthrough')
X = ct.fit_transform(X)
X = X.astype(np.float64)
#%% Avoiding the dummy variable trap
X = X[:,1:] # no need to do this as library take care of it

#%% Splitting the data set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
        X,y, test_size=0.2, random_state=0)

#%% Fitting Multiple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression().fit(X_train, y_train)

#%% Prediction the Test Set Results
y_pred = regressor.predict(X_test)

#%% Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values = X,
              axis=1)
# modify X to contain only statiscally significant features
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#%%
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#%%
X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#%%
X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#%%
X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#%%
X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog=y, exog=X_opt).fit()
regressor_OLS.summary()
#%%
