import numpy as np
lst1=[]
lst2=[]
lst3=[]
lst4=[]
for i in range(20):
    n=int(input("Enter a No: "))
    if i<5:
        lst1.append(n)
    elif i<10:
        lst2.append(n)
    elif i<15:
        lst3.append(n)
    else:
        lst4.append(n)
array1=np.array([lst1,lst2])
array2=np.array([lst3,lst4])
print("\nArray1 : \n",array1)
print("\nArray2 : \n",array2)
print("\nAddition: \n",array1+array2)
print("\nSubtraction: \n",array1-array2)
print("\nMultiplication: \n",array1*array2)
print("\nExponential: \n",array1**2)