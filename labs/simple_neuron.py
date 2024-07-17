# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 18:47:04 2024

@author: marcin
"""

import numpy as np

X = np.arange(-25,25).reshape(10,5)
X

Y = np.ones((X.shape[0], 1))
Y

X_1 = np.append(X, Y, axis=1)

X_2 = np.append(X, Y, axis=1)

w = np.random.rand(6)

def predict (x, w):
    total_stimulation = np.dot(x, w)
    if total_stimulation > 0:
        return 1
    else:
        return -1
    
predict(X_1[0,], w)
for val in X_1:
    y_pred = predict(val, w)
    print(y_pred)

    
