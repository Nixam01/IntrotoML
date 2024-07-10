# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:08:29 2024

@author: marcin
"""

import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.linear_model import LinearRegression

#ładowanie danych
auto = pd.read_csv(r"F:\Repozytoria\IntrotoML\data\auto-mpg.csv")
auto.head()
auto.shape

#przygotowanie danych
X = auto.iloc[:, 1:8]
X = X.drop('horsepower', axis=1)
y = auto.loc[:,'mpg']

#sprawdzenie
X.head()
y.head()


lr = LinearRegression()
lr.fit(X.to_numpy(),y)
lr.score(X.to_numpy(),y)

my_car1 = [4, 160, 190, 12, 90, 1]
my_car2 = [4, 200, 260, 15, 83, 1]
cars = [my_car1, my_car2]

mpg = lr.predict(cars)
print(mpg)