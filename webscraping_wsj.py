from selenium import webdriver
import pandas as pd
from datetime import datetime




PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

year = [2020]
month = [1]
day = [1]
headlines = []
count = 0
date=[]

for y in year:
    for m in month:
        for d in day:
                url = ("https://www.wsj.com/news/archive/%i/%i/%i" % (y, m, d))
                driver.get(url)
                page=driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div/div/span')
                if int(page.text[3]) == 1:
                    try:
                        driver.implicitly_wait(20)
                        driver.find_element_by_xpath('//*[@id="main"]/div[1]/div')
                        for i in range(1, 51):
                            news_headlines = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/ol/article[' + str(i) + ']/div[3]/div/h2')
                            headlines.append(news_headlines.text)
                            da=datetime(year=y,month=m,day=d)
                            date.append(da)
                    except Exception as e:
                        print(e)
                else :
                    try:
                        for p in range (1,(int(page.text[3])+1)):
                            url2=("https://www.wsj.com/news/archive/%i/%i/%i?page=%i" % (y, m, d,p))
                            driver.get(url2)
                            driver.implicitly_wait(20)
                            driver.find_element_by_xpath('//*[@id="main"]/div[1]/div')
                            for i in range(1, 51):
                                news_headlines = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div/ol/article[' + str(i) + ']/div[3]/div/h2')
                                headlines.append(news_headlines.text)
                                da=datetime(year=y,month=m,day=d)
                                date.append(da)
                    except Exception as e:
                        print(e)
                
                df=pd.DataFrame({"headlines":headlines,"date":date})
                
                    
print(headlines)
df.to_csv("output.csv")
