# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:25:11 2020

@author: Behnaz
"""
import pandas as pd
import pymongo
import json
import os



def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['markets'] 
    collection_name = 'canada' 
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert_many(data_json)

if __name__ == "__main__":
  filepath = 'C:\\Users\\Behnaz\\Documents\\fall term20\\indeces\\S&P_TSX.csv'  
  import_content(filepath)
  