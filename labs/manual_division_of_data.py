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

newArr = arr[0,1]
newArr

newArr = arr[0,2:4]
newArr
