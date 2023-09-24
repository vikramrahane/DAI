from numpy import linalg as la
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
a=np.array([3,4,-1])
b=np.array([1,1,-2])

print(a+b)
u=np.array([2,-7,1])
print(3*u)
#print((2*a)+(3*b)-(5*u))

a=np.array([2,-3,6])
b=np.array([8,2,-3])

print(np.sum(a*b)) #dot/inner product of two vectors
print(np.dot(a,b)) #dot/inner product of two vectors

a=np.array([6,-4,-3])
print("l2 norm of a",np.sqrt(np.sum(a*a)))
print(la.norm(a))

u=np.array([6,-4,-3])
print("l1 norm of u",la.norm(u,1)) #sum of mod of all elements in a vector

u=np.array([2,-3,6])
v=np.array([8,2,-3])
print(np.dot(u,v)/(la.norm(u)*la.norm(v))) # cosine similarity

u=np.array([1,3,2])
v=np.array([2,7,10])
print(np.dot(u,v)/(la.norm(u)*la.norm(v))) # cosine similarity
print("cos(u,v)=",cosine_similarity([u,v])) # cosine similarity

i1=np.array([-0.89,0.2,0.8])
i2=np.array([0.2,0.4,0.5])
i3=np.array([0.3,-0.9,0.3])
i4=np.array([0.4,0.23,0.4])
i5=np.array([0.34,0.3,-0.1])
print("cos(u,v)=",cosine_similarity([i1,i2,i3,i4,i5])) # cosine similarity

## Matrices: 2D array (with respect to numpy there is no matrix but 2D array)
a=np.array([[1,2,-3],[0,-4,1]])
b=np.array([[3,2,1],[0,1,0]])
print("a+b:\n",a+b)
print(a.shape)  #gives no of rows and columns
print(b.ndim)  #gives dimention(1D/2D/3D)
print(b.size)  #gives no of elements in the array

print(a-b)
print(a*b)  # Hadamard Product
print(np.multiply(a,b))  # Hadamard Product


##### Matrix Multiplication ###########
a=np.array([[1,3],[2,-1]])
b=np.array([[2,0,-4],[3,-2,6]])
print(a.shape)
print(b.shape)
print("\nAB=",a@b)
print("\nAB=",np.matmul(a,b))


b=np.array([[2,1],[4,0]])
print("\n2b^2-4b+3\n",(2*(b@b))-(4*b)+(3*np.eye(2)))
print("\nb^2-4b+12\n",((b@b))-(4*b)+(12*np.eye(2)))


print(la.det(b))   # Determinant of Matrix



















