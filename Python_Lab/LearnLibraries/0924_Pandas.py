
import pandas as pd
df=pd.read_table('http://bit.ly/chiporders'); #by default separator is tab
#df=pd.read_table('http://bit.ly/movieusers',sep="|",header=None);

print(df.columns)
df1=df.rename(columns={"order_id":"new_order_id"}) #inplace=True if change same df
print(df1.columns)

df.columns=['col1','col2','col3','col4','col5'] # It changes df
print(df.columns)
print(df.ndim)
print(df.shape)
df.describe()

print(df['col1'])
print(df['col3'])

print(df.head())  #bydefault 1st 5 records show  df.head(12)->shows 1st 12 records
df.tail()  #bydefault last 5 records show  df.head(12)->shows last 12 records

df=pd.read_table('http://bit.ly/chiporders'); #by default separator is tab
print(df.info())
print(type(df))
print(type(df['quantity']))
print(type(df[['quantity','item_name']])) 

df1=df[['quantity','item_name']]
print(df1.columns)
print(df1.info())
print(df1.describe())
print(df1)

print(df.iloc[:,1])   # iloc with index

print(df.iloc[2:7,1:4])

print(df.loc[2:7,['order_id','item_name']])

import pandas as pd
df=pd.read_table('http://bit.ly/chiporders'); #by default separator is tab
print(df.describe())

##### Add new column from existing and also change dtype of column #######
df['new_price']=df['item_price'].map(lambda x:x.replace('$','0'))
df.describe()

df['new_price']=df['new_price'].astype('float')
df.describe()

df['discount_val']=df['new_price'].map(lambda x:x*0.85)
#df['discount_val']=df['discount_val']*0.85     This is another solution

df.head()

print(df.columns)

#### Delete the column #####
df.pop('new_price')
print(df.columns)

df.drop(['discount_val'],axis=1,inplace=True)

#### Delete the row #####
df.drop([2,4,10],axis=0,inplace=True)  # index no 2,4,10 three rows deleted

df.shape
df[df['discount_val']>8]
index=df[df['discount_val']>8].index
df.drop(index,axis=0,inplace=True)
df.shape
































