# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 11:47:39 2020

@author: Behnaz
"""


import pandas as pd
import os
import matplotlib.pyplot as plt                  # plots


file_path_pandemics = os.path.abspath("pandemics")
file_path_index = os.path.abspath("indeces")

data_pandemic = pd.read_csv(os.path.join(file_path_pandemics, 'PandemicData.csv'), parse_dates=['Date'], index_col='Date')

data_index = pd.read_csv(os.path.join(file_path_index, 'Data.csv'), parse_dates=['Date'], index_col='Date')

#plot index data
plt.subplot(221)
ts_index=data_index[data_index.Country.eq("Canada")]
ts_index = ts_index["Price"]
plt.plot(ts_index["2009"])
#plot pandemic data
plt.subplot(222)

ts_pandemic = data_pandemic[data_pandemic.Pandemic.eq("Ebola")]
ts_pandemic = data_pandemic[data_pandemic.Country.eq("Liberia")]
ts = ts_pandemic["ActiveCases"]
plt.plot(ts["2014"])


  
