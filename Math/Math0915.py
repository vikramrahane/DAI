from numpy import linalg as la
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
a=np.array([[3,5],[2,3]])
print(f"inverse of a = \n {la.inv(a)}")

b=np.array([[1,1,0],[1,1,1],[0,2,1]])
print(f"inverse of b= \n {la.inv(b)}")

d=np.array([[1,1,2],[2,3,6],[3,6,10]]) #x+y+2z=4 2x+3y+6z=10 3x+6y+10z=17
s=np.array([4,10,17])
print(f"[x,y,z]={la.solve(d,s)}")

print(f"Rank of a={la.matrix_rank(a)}")

x=np.array([[2,2],[4,4]])
print(f"Rank of x={la.matrix_rank(x)}")

plt.xlim(0,5)
plt.ylim(0,5)

plt.arrow(0,0,3,2,head_width=0.3,head_length=0.3,color='purple')
plt.arrow(0,0,2,3,head_width=0.3,head_length=0.3,color='purple')


#********** Linear Equation solution
a=np.array([[2,1],[3,-5]]) #2x+y=7 3x-5y=4
b=np.array([7,4])
print(f"{np.matmul(la.inv(a),b)}") #inverseof(a) multiply with b
print(f"{la.solve(a,b)}")


# Find factors of equation ax2+bx+c=0
c=[1,-7,8]
print(f"roots=\n{np.roots(c)}")

#*****Eigen Value and Eigen Vector
a=np.array([[4,2],[2,3]])
print(la.eig(a))

a=np.array([[3,-4],[2,-6]])
print(la.eig(a))


print("3D Matrix Eigen Value and Eigen Vector")

A=np.array([[5,-10,-5],[2,14,2],[-4,-8,6]])
print(la.eig(A))

#*********singular Value Decomposition
            #*******
a=np.array([[3,2],[-4,-6]])
v1=a[0]
v2=a[1]

u1=v1/la.norm(v1)
w2=v2-np.dot(u1,v2)*u1
u2=w2/la.norm(w2)

o_n_a=np.array([u1,u2])
print(f"orthogonalized\n{o_n_a}")

def ortho_norm(x):
    v1=x[0]
    v2=x[1]

    u1=v1/la.norm(v1)
    w2=v2-np.dot(u1,v2)*u1
    u2=w2/la.norm(w2)

    o_n_a=np.array([u1,u2])
    return o_n_a
print(f"orthogonalized\n{ortho_norm(a)}")


def ortho_norm_3D(x):
    v1=x[0]
    v2=x[1]
    v3=x[2]

    u1=v1/la.norm(v1)

    w2=v2-np.dot(u1,v2)*u1
    u2=w2/la.norm(w2)

    w3=v3-np.dot(u1,v3)*u1-np.dot(u2,v3)*u2
    u3=w3/la.norm(w3)

    o_n_a=np.array([u1,u2,u3])
    return o_n_a

a=np.array([[1,1,0],[1,1,1],[0,2,1]])
print(f"orthogonalized\n{ortho_norm_3D(a)}")
s=ortho_norm_3D(a)
print(np.dot(s[:,1],s[:,2]))



















