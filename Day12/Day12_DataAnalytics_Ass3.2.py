import matplotlib.pyplot as plt
import numpy as np
year=[2010,2011,2012,2013,2014]
y10=[1,2,3,4,5]
y11=[2,3,4,5,9]
y12=[6,5,2,3,4]
y13=[2,5,8,9,3]
y14=[8,7,9,6,9]
max=[np.max(y10),np.max(y11),np.max(y12),np.max(y13),np.max(y14)]
plt.pie(max,labels=year,counterclock=False,startangle=90,colors=['r','b','g','c','y'])
plt.title("max sale in each year")
plt.show()

prod=['Product1','Product2','Product3','Product4','Product5']
plt.stackplot(prod,y10,y11,y12,y13,y14,labels=year)
plt.title("Product sale in each year")
plt.legend(loc='upper left')
plt.show()

prod=['Product1','Product2','Product3','Product4','Product5']
plt.pie(y10,labels=prod,counterclock=False,startangle=90,colors=['r','b','g','c','y'])
plt.title("Year 2010")
plt.show()

plt.pie(y11,labels=prod,counterclock=False,startangle=90,colors=['r','b','g','c','y'])
plt.title("Year 2011")
plt.show()

plt.pie(y12,labels=prod,counterclock=False,startangle=90,colors=['r','b','g','c','y'])
plt.title("Year 2012")
plt.show()

plt.pie(y13,labels=prod,counterclock=False,startangle=90,colors=['r','b','g','c','y'])
plt.title("Year 2013")
plt.show()

plt.pie(y14,labels=prod,counterclock=False,startangle=90,colors=['r','b','g','c','y'])
plt.title("Year 2014")
plt.show()