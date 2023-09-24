import numpy as np
from numpy import linalg as la
from sklearn.decomposition import PCA

a=np.array([[2,0,8,6,0],[1,6,0,1,7],[5,0,7,4,0],[7,0,8,5,0],[0,10,0,0,7]])
print(a.shape)
U,S,VT=la.svd(a)
print("U",U)
print(U.shape)
print("S",S)
print(VT.shape)
print("VT",VT)

################ Variance ############
x=np.array([2,5,7,8])
y=np.array([9,7,5,2])
data=np.stack((x,y),axis=0)


np.cov(data,ddof=0)  #ddof uses informula instead of 'N' it take 'N-ddof'
print("Variance Covariance MAtrix : ",np.cov(data ,ddof=0))

x=np.array([2,5,7,8])
y=np.array([3,10,18,24])
data=np.stack((x,y),axis=0)


np.cov(data,ddof=0)  #ddof uses informula instead of 'N' it take 'N-ddof'
print("Variance Covariance MAtrix : ",np.cov(data,ddof=0))

import pandas as pd
milk=pd.read_csv("milk.csv",index_col=0)

print("Variance Covariance MAtrix : \n",milk.cov(ddof=0))

sigma=milk.cov(ddof=0)
eigen_val,eigen_vectors=la.eig(sigma)

print("eigen_values:\n",eigen_val)
print("eigen_vectors:\n",eigen_vectors)

pca_score=np.matmul(milk,eigen_vectors) 
print(pca_score.var(ddof=0)) # For verification that it is descendant order and same as Eigen values
print("eigen_values:\n",eigen_val)



print(pca_score.cov())
























