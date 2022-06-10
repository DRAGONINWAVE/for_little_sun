import requests
from bs4 import BeautifulSoup
import datetime
import csv
import os
import lxml
import re
import time
import pandas
hh = []
data = pandas.read_excel('749zhan.xlsx')
locations = data.iloc[:,0].values
# print(locations)
k = 0
for location in locations:
    # print(location)
    for j in range(2015,2020):
        yy = str(j)
        for i in range(1,12+1):
            # if j == 2019 and i==12:
            #     break
            # else:
            # print(location,j,i)
            mm = str(i).zfill(2)
            r = requests.get(url="http://www.tianqihoubao.com/lishi/"+location+"/month/"+yy+mm+".html")
            soup = BeautifulSoup(r.text,'lxml')
            tds = soup.find_all("tr")
            for i in tds:
                hh.append(i.get_text().replace("\r\n", "").replace("\n\n", "").replace("\n", "").replace(" ", ""))
    k = k + 1
    print(k,len(locations))
    data = pandas.DataFrame({location:hh})
    data.to_excel(location+"2015-2019.xlsx",index=False,encoding="gb2312")