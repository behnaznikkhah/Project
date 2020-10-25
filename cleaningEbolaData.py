# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:31:24 2020

@author: Behnaz
"""


import pandas as pd
# Read data 
df = pd.read_csv('C:/Users/Behnaz/Documents/fall term20/ebola_2014_2016_clean (2).csv', parse_dates=['Date'])

# aggrigate duplicate data

final_df=df.groupby(['Country','Date'],as_index=False).sum()

final_df.to_csv('C:/Users/Behnaz/Documents/fall term20/ebola_2014_2016_clean.csv', index=False)
