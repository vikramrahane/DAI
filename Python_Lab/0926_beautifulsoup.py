import requests
from bs4 import BeautifulSoup
import re
url='https://www.imdb.com/search/title/?release_date=2022-01-01,2023-12-31'
response=requests.get(url)
#print(response.content)
print(response.text)

html_soup=BeautifulSoup(response.text,'html.parser')
type(html_soup)
print(html_soup)

movie_containers=html_soup.find_all('div',class_='lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

first_movie=movie_containers[0]
print(first_movie)

h3=first_movie.h3.find_all('a')
h3[1]

print(first_movie.h3)
print(first_movie.h3.a)
print(first_movie.h3.a.text)

y=first_movie.find('span',class_='lister-item-year text-muted unbold')
print(y)
print(y.text)


y=first_movie.find('div',class_='inline-block ratings-imdb-rating')
print(y)
print(y.text)

years=[]
ratings=[]
names=[]
for movi in movie_containers:
    names.append(movi.h3.a.text)
    y=movi.find('div',class_='inline-block ratings-imdb-rating')
    if y!=None:
        ratings.append(movi.strong.text)
    else:
        ratings.append(0)
    s=movi.find('span',class_='lister-item-year text-muted unbold')
    years.append(s.text)
    
print(len(years))
print(len(ratings))
print(len(names))

data={'name':names,'ratings':ratings,'years':years}
import pandas as pd
df=pd.DataFrame(data)
df.head()



















