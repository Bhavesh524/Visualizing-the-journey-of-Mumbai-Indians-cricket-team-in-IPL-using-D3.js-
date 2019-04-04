# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 23:09:52 2019

@author: bhavesh2429
"""

import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('F:/TCD_HT/Data_Visualization/visualization/IPL/data/Wins.csv')

labels = df["Opposition"]
values = df["Won"]

trace = go.Pie(labels=labels, values=values)

py.iplot([trace])