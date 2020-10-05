# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:37:29 2020

@author: Behnaz
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from time import sleep

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
year=[2020]
month=[1]
day=[2]
headlines=[]
count=0

driver = webdriver.Chrome('chromedriver.exe')
for y in year:
    for m in month:
        for d in day:
            url=("https://www.wsj.com/news/archive/%i/%i/%i"%(y,m,d))
            driver.get(url)
            try:
                driver.find_element_by_xpath('//*[@id="main"]/div[1]/div')
                for i in range(1,50):
                    try:
                        news_headlines = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/ol/article['+ str(i) + ']/div[3]/div/h2')
                        headlines.append(news_headlines.text)
                    except Exception as e:
                        print(e)
            except Exception as e:
                print(e)
print(headlines)                
                
                
       
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                