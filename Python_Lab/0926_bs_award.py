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
    
    tab = html_soup1.find_all("h1",class_="firstHeading mw-first-heading")
    title.append(tab[0].i.text)
    
    t = html_soup1.find_all("table",class_="infobox vevent")
    tr_row = t[0].find_all("tr")  
#from all rows we need only row no 2 for Director name and row no 13 for release date
    if tr_row[2].td.a!=None:        
        directedby.append(tr_row[2].td.a.text)
    else:
        directedby.append("None")
    if tr_row[13].td.li!=None:        
        releasedate.append(tr_row[13].td.li.text)
    else:
        releasedate.append("None")          
                
                
data={'title':title,'directedby':directedby,'releasedate':releasedate}
import pandas as pd
df=pd.DataFrame(data)
df.to_csv("award_movie.csv")
print(df.head(20))


