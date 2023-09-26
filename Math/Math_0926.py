from sympy import limit,sqrt,pprint,diff,solve
from sympy.abc import x,y,z

e=x**4-2*x**2+3
d1=diff(e,x)
sol=solve(d1,x)
print(sol)
d2=diff(d1)
print(d2.subs([(x,sol[0])]))
print(d2.subs([(x,sol[1])]))
print(d2.subs([(x,sol[2])]))

e=(x*y)/(x**2+y)
pprint(e)
d1=diff(e,x)
pprint(d1)


e=sqrt((2*x**2)+(3*y**2)-4)
pprint(e)
d1=diff(e,x)
pprint(d1)
d2=diff(e,y)
pprint(d2)
