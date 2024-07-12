# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 15:06:21 2024

@author: marcin
"""

import numpy as np

a = np.arange(20)
a

a.shape
a[0]
a[3]

a = a.reshape(2, 10)
a.shape
a[0]
a[0][3]

a = a.reshape(2,5,2)
a.shape
a[0]
a[0][3]
a[0][3][1]

b = np.arange(0,40,2).reshape(4,5)

c = a_python_list =  [2**x for x in range(10)]
c=np.array(a_python_list)
c

zero_array = np.zeros(10)
one_array = np.ones(10)
empty_array = np.empty(100)
lucky_array = np.full(25, 13).reshape(5, 5)
diagonal_array = np.eye(5)
random_array = np.random.random(10)
linspace_array = np.linspace(100, 200, 5)


