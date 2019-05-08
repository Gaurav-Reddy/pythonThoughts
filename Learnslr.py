# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:45:23 2019

@author: Gaurav Reddy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users\Gaurav Reddy\Downloads\Viralcount_Drug.csv")

x=df['drug']
x=x[:,np.newaxis]

y=df.iloc[:,1] #iloc is an integer based indexing function

df.plot.scatter(x="drug",y='viral count')

from sklearn.linear_model import LinearRegression
model=LinearRegression().fit(x,y)

y_cap=model.predict(x)

df.plot.scatter(x="drug",y_cap)

from sklearn.metrics import mean_squared_error,r2_score,adjusted_rand_score
mean_squared_error(y,y_cap)
r2_score(y,y_cap)
adjusted_rand_score(y,y_cap)