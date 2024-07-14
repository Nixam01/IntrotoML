# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 20:48:53 2024

@author: marcin
"""

import numpy as np

arr = np.arange(5,30,2)
arr

boolArr = arr < 10
boolArr

newArr = arr[boolArr]
newArr

newArr = arr[arr < 20]
newArr 

newArr = arr[arr%3==0]
newArr

newArr = arr[(arr>10) & (arr<20)]
newArr

arr = np.arange(24).reshape(4,6)
arr

newArr = arr[0]
newArr

newArr = arr[1,2]
newArr

newArr = arr[1,2:4]
newArr


newArr = arr[1,2:5]
newArr

newArr = arr[1,:]
newArr

newArr = arr[2,:]
newArr

newArr = arr[0:3,2]
newArr

newArr = arr[:3,2]
newArr

newArr = arr[:3,2:4]
newArr

newArr = arr[:,-1]
newArr

newArr = arr[:,:-1]
newArr

arr = np.arange(50).reshape(10,5)
arr

split_level = 0.2
num_rows = arr.shape[0]
split_border = split_level * num_rows

arr = arr[:round(split_border),:]
arr = arr[round(split_border):,:]

np.random.shuffle(arr)
arr

arr[:round(split_border),:]
arr[round(split_border):,:]

data = np.arange(500).reshape(100,5)
np.random.shuffle(data)
data

split_level = 0.2
num_rows = data.shape[0]
split_border = split_level * num_rows

X_test = data[:round(split_border),:-1]
X_train = data[round(split_border):,:-1]
Y_test = data[:round(split_border),-1]
Y_train = data[round(split_border):,-1]

data.shape
X_train.shape
X_test.shape
Y_train.shape
Y_test.shape