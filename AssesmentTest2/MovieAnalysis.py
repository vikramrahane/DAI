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

def checkgener(s):
    lst=s.split('|')
    if len(lst)==4:
        l=['Action','Romance','Comedy','Thriller']
        s=np.sum(list(map(lambda x:1 if x in lst else 0,l)))
        if s==4:
            return True
        else:
            False
    else: 
        return False

#df1=moviedata[moviedata.apply(lambda x: checkgener(x['genres']),axis=1)]
df1=moviedata[moviedata['genres'].apply(checkgener)
df1.shape
print(df1.head)

g=r11.groupby(by="movieId")
g1=g['rating'].mean()
print(g1)


