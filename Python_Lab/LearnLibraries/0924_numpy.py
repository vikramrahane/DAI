import numpy as np

a=np.array([1,2,3,4.6,7])
print(a)
print("Array Type ",type(a))
print("Data Type ",a.dtype)  # It gives data type of ndarray
print("Dimensions ",a.ndim)
print("Shape ",a.shape) # shows no of items in array

a=np.array([[1,2,3,4],[5,6,7,8]])
print(a)
print("Array Type ",type(a))
print("Data Type ",a.dtype)  # It gives data type of ndarray
print("Dimensions ",a.ndim)
print("Shape ",a.shape)  # shows no of (rows,column)

a=np.array(['viki','prada','ajay','rana','sam'])
print(a)
print("Array Type ",type(a))
print("Data Type ",a.dtype)  # It gives data type of ndarray
print("Dimensions ",a.ndim)
print("Shape ",a.shape) # shows no of items in array
#utf - unified text format

a=np.array([[[1,2,3],[4,5,6]],[[9,8,7],[6,5,4]]])
print(a)
print("Array Type ",type(a))
print("Data Type ",a.dtype)
print("Dimension ",a.ndim)
print("Shape ",a.shape)

a=np.array([[[[1,2],[3,4]],[[5,6],[7,8]]],[[[9,8],[7,6]],[[5,4],[3,2]]]])
print(a)
print("Array Type ",type(a))
print("Data Type ",a.dtype)
print("Dimension ",a.ndim)
print("Shape ",a.shape)

a=np.array([[[[[1,2],[3,4]],[[6,7],[8,9]]],[[[1,2],[3,4]],[[1,2],[3,4]]]],[[[[1,2],[3,4]],[[1,2],[3,4]]],[[[1,2],[3,4]],[[1,2],[3,4]]]]])
print(a)
print("Array Type ",type(a))
print("Data Type ",a.dtype)
print("Dimension ",a.ndim)
print("Shape ",a.shape)

b=np.arange(12)
print(b)

b=np.arange(1,32,2).reshape(4, 4)
print(b)
print(b[:,1:3]) # ':' -> it means all (rows/columns)
print(b[1:3,0:3])  # 1 & 2 Row, 0,1 & 2 Column
c=b[1:3,:]
print(c,type(c))

b=np.arange(1,32,2).reshape(4, 4,order='f')  # f-> fortran Order Vertically (Default is c oredr)
print(b)

a=np.zeros((2,2),dtype='int32') # bydefault dtype is float
print(a)

a=np.ones((2,2),int)  # bydefault dtype is float
print(a)

a=np.empty((2,2),str)
print(a)

a=np.full((3,3),56)
print(a)

b=np.ones((3,3))
c=a+b                 # addition of two array's with same shape
print(c)

c=c+3                 # addition of array with scaalr value
print(c)

c=a*b                 # element wise Multiplication
print(f"a: \n{a}\nb:\n{b}\nc:\n{c}")

c=np.matmul(a,b)  # Mathematical Multiplication Matrix
print(c)
print(a.dot(b))     # Mathematical Multiplication Matrix

a=np.identity(3)# Identity square Matrix
print(a)
b=np.eye(4,5)      # Identity Matrix
print(b)

b=np.eye(4,5,k=1)      # Identity Matrix diagonal shift upper side by 1
print(b)

b=np.eye(4,5,k=2)      # Identity Matrix diagonal shift upper side by 2
print(b)

###### Filter Array ##########

a=np.array([[11,12,13],[45,67,15],[16,17,18]])
print(a[a%6==0])
print(a[a>15]) # It gives values who satisfy the condition
print(a>15)  # It returns Boolean value MAtrix according to condition

# to search the value
print(np.where(a%2==0))
print(list(np.where(a%2==0)[0].data))
print(np.where(a%5==0))

# sum of all values
print(np.sum(a)) # return one no sum of all no
print(np.sum(a,axis=1)) # return sum of all no row wise
print(np.sum(a,axis=0)) # return sum of all no column wise

print(np.mean(a))
print(np.median(a))

x=np.array([10,20,30])
y=np.array([1,2,3])
z=np.array([11,21,31])

b=np.vstack((x,y,z))
print(b)
b=np.hstack((x,y,z))
print(b)

print(b)
np.flip(b)          #reverse both rows and column
np.flip(b,axis=1)   #reverse only columns
np.flip(b,axis=0)   #reverse only rows


x=np.linspace(10, 30,8)
print(x)

x=np.linspace(10, 30,4,endpoint=False) # 30 excluded
print(x)
























