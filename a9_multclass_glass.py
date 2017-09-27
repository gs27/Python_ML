# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:27:32 2017

@author: gukalra
"""

import sklearn.metrics as sm
import numpy as np
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import cross_val_predict
from sklearn import metrics

data = 'C:\Users\gukalra\Downloads\knx\glass_9.csv'
dataframe = read_csv(data, names=None)

dataframe = dataframe.sample(frac=1).reset_index(drop=True)
dataset = dataframe.values

X = dataset[:,0:-1]
Y = dataset[:,-1]
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(
X, Y, test_size=0.25, random_state=0)

model = svm.SVC( C                        =   0.01,
                 gamma                    =  'auto',
                 kernel                   =  'linear',
                 degree                   =   3,
                 class_weight             =  'balanced',
                 coef0                    =   0.0,
                 decision_function_shape  =   None,
                 probability              =   False,
                 max_iter                 =  -1,
                 tol                      =   0.001,
                 cache_size               = 700,
                 random_state             =   None,
                 shrinking                =   True,
                 verbose                  =   False
                 )

model.fit(X_train, Y_train) 

Y_pred = model.predict(X_test)
print(Y_pred)

ACC = sm.accuracy_score(Y_test, Y_pred)
print ACC

target_names = ['A', 'B', 'C', 'D','E','F']
print(sm.classification_report(Y_test, Y_pred, target_names=target_names))

expected =  Y
predicted = cross_val_predict(model, X, expected, cv=5)
#predicted = model.predict(X)

# summarize the fit of the model
print(metrics.accuracy_score(expected, predicted))
#print(metrics.precision_score(expected, predicted))
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))