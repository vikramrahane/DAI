import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("weather_by_cities.csv")

g=df.groupby(by='city')    # MAke grup by city column

max_temp=g['temperature'].max() #get max temp of each city

plt.bar(max_temp.index,max_temp.values)
plt.xlabel('City')
plt.ylabel('Max Temperature')
plt.title("City wise Maximum Temperature")
plt.show()

plt.pie(max_temp.values,labels=max_temp.index,colors=['r','g','b'],explode=(0,0,0),counterclock=False,startangle=90)
plt.title("Temperature")
plt.show()