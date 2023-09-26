import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
m11=pd.read_csv("movies11.csv")
m12=pd.read_csv("movie12.csv",header=None)
m13=pd.read_csv("movies13.csv",header=None)
r11=pd.read_csv("rating11.csv")
m11.info()
m12.info()
m13.info()
r11.info()

m12.columns=m11.columns
m13.columns=m11.columns

moviedata=pd.concat([m11,m12,m13])
moviedata.info()

### 2. find all masala movie - (action ,romance,comedy,thriller)
 # Function to check all['Action','Romance','Comedy','Thriller'] genres are present or not
def checkgener(s,l): 
    lst=s.split('|')
    if len(lst)>=4:
        s=np.sum(list(map(lambda x:1 if x in lst else 0,l)))        
        if s==4:
            return True
        else:
            return False
    else: 
        return False
    
l=['Action','Romance','Comedy','Thriller']
df1=moviedata[moviedata['genres'].apply(checkgener,moviedata['genres'],l)]
df1

### 3. plot a pie chart to represent genre and frequency of movie count
genre_count=moviedata['genres'].str.split('|').explode().value_counts()
print(genre_count)
myexplode=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.3]
plt.pie(genre_count,labels=genre_count.index,startangle=90,counterclock=False,radius=4,rotatelabels=270,explode=myexplode)

### 4. average rating for each movie and merge 2 frames
g=r11.groupby(by="movieId")
g1=g['rating'].mean()
print(g1)






















