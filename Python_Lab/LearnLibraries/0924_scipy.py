from scipy.special import cbrt,comb,perm 
from scipy import linalg
import numpy as np
x=cbrt([27,64])
print(x)

print(perm(6,2))
print(comb(6,2))

n=np.array([[10,20],[30,40]])
print(linalg.det(n))

eig_val,eig_vector=linalg.eig(n)
print(eig_val)
print(eig_vector)

from scipy import stats
n=np.array([[22,23,14,22,56],[12,67,45,56,23]])
print(n)
modval=stats.mode(n,axis=1)
print(modval)

from scipy import integrate

f=lambda x:x**2
#single integration with a=0 & b=1
integ=integrate.quad(f, 0, 1)  # 1st value in integration 2nd value is estimeeted error in integration
print(integ)