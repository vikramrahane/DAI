import requests
import re
from bs4 import BeautifulSoup
url='https://en.wikipedia.org/wiki/Academy_Award_for_Best_Picture'
response=requests.get(url)

html_soup=BeautifulSoup(response.text,'html.parser')

container=html_soup.find_all('tr',style="background:#FAEB86")
print(len(container))


directedby=[]
releasedate=[]
title=[]
    
for m in container:
    url1=m.a.attrs    
    url1='https://en.wikipedia.org'+url1['href']
    response1=requests.get(url1)
    
    html_soup1=BeautifulSoup(response1.text,'html.parser')
    
    container1=html_soup1.find_all('tr') 
    for m1 in container1:
        d=m1.find_all('th',class_="infobox-label")
        for th in d:
            if th.text=="Directed by":
                directedby.append(m1.a.text)
            if th.text=="Release dates":
                releasedate.append(m1.li.text)
                
                
print(len(directedby))
print(len(releasedate))
'''data={'directedby':directedby,'releasedate':releasedate}
import pandas as pd
df=pd.DataFrame(data)
df.head()'''
            