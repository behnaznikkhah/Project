# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:52:10 2020

@author: Behnaz
"""

import pandas as pd
import os

def import_content(file_dir):
    
    filepath_list = []
    
    file_path = os.path.abspath(file_dir) 
    filepath_list = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.csv')]

    #print("file path list is", filepath_list)
    
    data_Abudhabi = pd.read_csv(filepath_list[0],thousands=',')
    data_Abudhabi['Country'] = 'UAE'
    data_Abudhabi.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Brazil = pd.read_csv(filepath_list[1],thousands=',')
    data_Brazil['Country'] = 'SouthAmerica'
    data_Brazil.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_France = pd.read_csv(filepath_list[2],thousands=',')
    data_France['Country'] = 'France'
    data_France.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Germany = pd.read_csv(filepath_list[3],thousands=',')
    data_Germany['Country'] = 'Germany'
    data_Germany.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_USA = pd.read_csv(filepath_list[4],thousands=',')
    data_USA['Country'] = 'USA'
    data_USA.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Britain = pd.read_csv(filepath_list[5],thousands=',')
    data_Britain['Country'] = 'Britain'
    data_Britain.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_HongKong = pd.read_csv(filepath_list[6],thousands=',')
    data_HongKong['Country'] = 'HongKong'
    data_HongKong.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Jakarta = pd.read_csv(filepath_list[7],thousands=',')
    data_Jakarta['Country'] = 'Indonesia'
    data_Jakarta.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Korea = pd.read_csv(filepath_list[8],thousands=',')
    data_Korea['Country'] = 'Korea'
    data_Korea.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_India = pd.read_csv(filepath_list[9],thousands=',')
    data_India['Country'] = 'India'
    data_India.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Japan = pd.read_csv(filepath_list[10],thousands=',')
    data_Japan['Country'] = 'Japan'
    data_Japan.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Australia = pd.read_csv(filepath_list[11],thousands=',')
    data_Australia['Country'] = 'Australia'
    data_Australia.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Canada = pd.read_csv(filepath_list[12],thousands=',')
    data_Canada['Country'] = 'Canada'
    data_Canada.rename(columns = {'Vol':'Volume'}, inplace = True)
    
    data_Shanghai = pd.read_csv(filepath_list[13],thousands=',')
    data_Shanghai['Country'] = 'China'
    data_Shanghai.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Shanghai = pd.read_csv(filepath_list[14],thousands=',')
    data_Shanghai['Country'] = 'South Africa'
    data_Shanghai.rename(columns = {'Vol.':'Volume'}, inplace = True)

    data = pd.concat([data_Abudhabi, data_Brazil, data_France, data_Germany, data_USA, data_Britain, data_HongKong,
                      data_Jakarta, data_Korea, data_India, data_Japan, data_Australia, data_Canada, data_Shanghai], axis=0)
    #print(data.head(5))
    #print(data.tail(5))
    #print(data.info())
    data.rename(columns = {'Change %':'Change'}, inplace = True)
    data['Change'] = data['Change'].str.replace('.$', '')
    data['Volume'] = data['Volume'].str.replace('.$', '')
    data[["Volume","Change"]] = data[["Volume","Change"]].apply(pd.to_numeric)
    data["Date"] = pd.to_datetime(data["Date"])
    data.to_csv(os.path.join(file_path, 'Data.csv'),index=False)
    
if __name__ == "__main__":
  file_dir = 'indeces'  
  import_content(file_dir)


