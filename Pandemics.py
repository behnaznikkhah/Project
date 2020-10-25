# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 21:44:34 2020

@author: Behnaz
"""

import pandas as pd
import os

def import_content(file_dir):
    
    filepath_list = []
    
    file_path = os.path.abspath(file_dir) 
    filepath_list = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.csv')]

    #print("file path list is", filepath_list)
    
    data_Ebola = pd.read_csv(filepath_list[0])
    data_Ebola['Pandemic'] = 'Ebola'
    data_Ebola.rename(columns = {'Cumulative no. of confirmed, probable and suspected cases':'ActiveCases',
                                 'Cumulative no. of confirmed, probable and suspected deaths':'Deaths'}, inplace = True)
    data_Ebola=data_Ebola[['Date','Country','ActiveCases','Deaths','Pandemic']]

    
    data_Covid = pd.read_csv(filepath_list[1])
    data_Covid['Pandemic'] = 'Covid'
    data_Covid.rename(columns = {'total_cases':'ActiveCases',
                                  'total_deaths':'Deaths','location':'Country',
                                  'date':'Date'}, inplace = True)
    data_Covid=data_Covid[['Country','Date','ActiveCases','Deaths','Pandemic']]
    


    data_Sars = pd.read_csv(filepath_list[2])
    data_Sars['Pandemic'] = 'Sars'
    data_Sars.rename(columns = {'Cumulative number of case(s)':'ActiveCases',
                                'Number of deaths':'Deaths'}, inplace = True)
    data_Sars=data_Sars[['Date','Country','ActiveCases','Deaths','Pandemic']]

    
    data_Swineflu = pd.read_csv(filepath_list[3])
    data_Swineflu['Pandemic'] = 'Swine Flu'
    data_Swineflu.rename(columns = {'Cumulative no. of cases':'ActiveCases',
                                   'Cumulative no. of deaths':'Deaths'}, inplace = True)
    data_Swineflu=data_Swineflu[['Date','Country','ActiveCases','Deaths','Pandemic']]


    

    data = pd.concat([data_Sars,data_Swineflu,data_Covid,data_Ebola], axis=0)
    #print(data.head(5))
    #print(data.tail(5))
    #print(data.info())
    #data.rename(columns = {'Change %':'Change'}, inplace = True)
    #data['Change'] = data['Change'].str.replace('.$', '')
    #data['Volume'] = data['Volume'].str.replace('.$', '')
    #data[["Volume","Change"]] = data[["Volume","Change"]].apply(pd.to_numeric)
    data["Date"] = pd.to_datetime(data["Date"])
    data.to_csv(os.path.join(file_path, 'PandemicData.csv'),index=False)
    
if __name__ == "__main__":
  file_dir = 'pandemics'  
  import_content(file_dir)