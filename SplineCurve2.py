#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 22:01:41 2018

@author: tukai
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import MySQLdb
import random

x_axis = list()
y_axis = list()

graph_range = 100 

for x in range(graph_range):
    x_axis.append(x)
    y_axis.append(random.randint(80,100))


x_smooth = np.linspace(x_axis[1], x_axis[99],90)
y_smooth = spline(x_axis, y_axis,x_smooth)

plt.plot(x_axis, y_axis)

plt.show()

