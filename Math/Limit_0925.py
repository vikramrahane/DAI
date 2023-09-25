import numpy as np
from sympy import limit,sqrt,pprint
from sympy.abc import x
expr=sqrt(x+1)
res=limit(expr,x,0)
pprint(expr)
print(res)

expr=((4*x)-(5*x*x))/(x-1)
res=limit(expr,x,0)
pprint(expr)
print("at x=0 ",res)

expr=(sqrt((x+8))-3)/(x-1)
res=limit(expr,x,1)
pprint(expr)
print("at x=1 ",res)

from sympy import diff
e=x**2
r=diff(e,x)
print("Deriative of ")
pprint(e)
print("with respect to x is: ")
pprint(r)

e=sqrt(100-(x*x))
r=diff(e,x)
print("Deriative of ")
pprint(e)
print("with respect to x is: ")
pprint(r)

e=sqrt(169-(x*x))
r=diff(e,x)
print("Deriative of ")
pprint(e)
print("with respect to x is: ")
pprint(r)

e=80-(4.9*x*x)
r=diff(e,x)
print("Deriative of ")
pprint(e)
print("with respect to x is ")
pprint(r)

e=x*x-(1/x)
r=diff(e,x)
print("Deriative of ")
pprint(e)
print("with respect to x is ")
pprint(r)

### Product of two functions ####
u=x**3
v=x**3-5*x+10
f=u*v
r=diff(f,x)
print("Derivative of ")
pprint(f)
print("with respect to x is: ")
pprint(r)

### division of two functions ####
u=x**3
v=x**3-5*x+10
f=u/v
r=diff(f,x)
print("Derivative of ")
pprint(f)
print("with respect to x is: ")
pprint(r)

### division of two functions ####
u=x**2+5*x-3
v=x**5-6*x**3+3*x**2-7*x+1
f=u/v
r=diff(f,x)
print("Derivative of ")
pprint(f)
print("with respect to x is: ")
pprint(r)


v=sqrt((169/x)-x)
r=diff(v,x)
print("Derivative of ")
pprint(v)
print("with respect to x is: ")
pprint(r)

v=(x+8)**5
r=diff(v,x)
print("Derivative of ")
pprint(v)
print("with respect to x is: ")
pprint(r)







































