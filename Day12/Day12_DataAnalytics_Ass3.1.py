import pandas as pd

mymoviedata=pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.head())
mymoviedata.info()

mymoviedata.columns=['sr.no', 'age', 'Gender', 'profession', 'Views']
print(mymoviedata.head())

print(mymoviedata['Gender'])

mymoviedata['agegen']=mymoviedata['age'].astype('str')+":"+mymoviedata['Gender']
print(mymoviedata.head())


mymoviedata=mymoviedata.replace({'Views':'[A-Za-z]'},0,regex=True)
mymoviedata['Views']=mymoviedata['Views'].astype('int64')

g=mymoviedata.groupby(by='age')

g1=g['Views'].mean()
import matplotlib.pyplot as plt
plt.bar(g1.index,g1.values)
plt.xlabel("Age")
plt.ylabel("Average Views")
plt.show()

g=mymoviedata.groupby(by="profession")
g1=g['Views'].mean()
plt.bar(g1.index,g1.values)
plt.xticks(rotation=90)
plt.xlabel("Profession")
plt.ylabel("Total Views")
plt.show()
