"""
Created on Tue Oct 7 2020
@author: Sai Madhuri Yerramsetti

"""
import pandas as pd
import pymongo
import json
import os

def import_content(file_dir):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['market_db'] 
    collection = db['market_collection']
    
    filepath_list = []
    
    file_path = os.path.abspath(file_dir) 
    filepath_list = [os.path.join(file_path, f) for f in os.listdir(file_path) if f.endswith('.csv')]

    print("file path list is", filepath_list)
    
    data_Abudhabi = pd.read_csv(filepath_list[0])
    data_Abudhabi['Country'] = 'UAE'
    data_Abudhabi.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Brazil = pd.read_csv(filepath_list[1])
    data_Brazil['Country'] = 'SouthAmerica'
    data_Brazil.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_France = pd.read_csv(filepath_list[2])
    data_France['Country'] = 'France'
    data_France.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Germany = pd.read_csv(filepath_list[3])
    data_Germany['Country'] = 'Germany'
    data_Germany.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_USA = pd.read_csv(filepath_list[4])
    data_USA['Country'] = 'USA'
    data_USA.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Britain = pd.read_csv(filepath_list[5])
    data_Britain['Country'] = 'Britain'
    data_Britain.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_HongKong = pd.read_csv(filepath_list[6])
    data_HongKong['Country'] = 'HongKong'
    data_HongKong.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Jakarta = pd.read_csv(filepath_list[7])
    data_Jakarta['Country'] = 'Indonesia'
    data_Jakarta.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Korea = pd.read_csv(filepath_list[8])
    data_Korea['Country'] = 'Korea'
    data_Korea.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_India = pd.read_csv(filepath_list[9])
    data_India['Country'] = 'India'
    data_India.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Japan = pd.read_csv(filepath_list[10])
    data_Japan['Country'] = 'Japan'
    data_Japan.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Australia = pd.read_csv(filepath_list[11])
    data_Australia['Country'] = 'Australia'
    data_Australia.rename(columns = {'Vol.':'Volume'}, inplace = True)
    
    data_Canada = pd.read_csv(filepath_list[12])
    data_Canada['Country'] = 'Canada'
    data_Canada.rename(columns = {'Vol':'Volume'}, inplace = True)
    
    data_Shanghai = pd.read_csv(filepath_list[13])
    data_Shanghai['Country'] = 'China'
    data_Shanghai.rename(columns = {'Vol.':'Volume'}, inplace = True)

    data = pd.concat([data_Abudhabi, data_Brazil, data_France, data_Germany, data_USA, data_Britain, data_HongKong,
                      data_Jakarta, data_Korea, data_India, data_Japan, data_Australia, data_Canada, data_Shanghai], axis=0)
    print(data.head(5))
    print(data.tail(5))
    print(data.info())

    data_json = json.loads(data.to_json(orient='records'))
    collection.remove()
    collection.insert_many(data_json)
    print(db.market_collection.find_one())

if __name__ == "__main__":
  file_dir = '/tmp/sai'  
  import_content(file_dir)
