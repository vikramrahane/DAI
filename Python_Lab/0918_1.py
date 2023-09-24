def f1(a=1,b=2,c=3,*tp,**kwargs):
    print(a,b,c)
    print(tp)
    print(kwargs,"\n\n")
f1()
print()
f1(11,22,333,44,55,66,x=56,y=12,z=90)

def f1(a=1,b=2,c=3,*tp,**kwargs):
    print(a,b,c)
    print(tp)
    print(kwargs,"\n\n")
    s=a+b+c
    for d in tp:
        s=s+d
    for k in kwargs.values():
        s=s+k
    return s
print("Sum: ",f1(11,22,333,44,55,66,x=56,y=12,z=90))
print("Sum: ",f1())