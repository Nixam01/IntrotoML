# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline

months = ['Jan', 'Feb', 'March', 'April']
temperature = [-4, -6, 3, 12]


df = pd.DataFrame({'months': months, 'temperature': temperature})
df.plot.bar(x = 'months', y = 'temperature')

text = "Hello world!"
print(text)
