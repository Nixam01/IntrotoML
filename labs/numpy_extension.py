# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 13:09:16 2024

@author: marcin
"""

import numpy as np

X = np.arange(25).reshape(5,5)
X

Ones = np.ones(25).reshape(5,5)
Ones

Dot = np.dot(X, Ones)
Dot

diag = np.zeros(25).reshape(5,5)
diag

np.fill_diagonal(diag, 1)
diag

Dot = np.dot(X, diag)

np.where(X > 10, 1, 0)

np.where(X % 2 == 0, 1, 0)

np.where(X % 2 == 0, X, X+1)

X_bis = np.where( X > 10, 2*X, 0)
np.count_nonzero(X_bis)

x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])

np.append(x, y, axis=1)
np.append(x, x, axis=0)