n=int(input("Entera a No: "))
def fact(n,start):
    if n==start:
        return start
    else:
        return n*fact(n-1,start)
print(f"Factorial of {n} is {fact(n,1)}")

def add(n):
    if n==1:
        return 1
    else:
        return n+add(n-1)
print(f"sum of no 1 to {n} is {add(n)}")

print("\n**** Tuple ****")
def f1(a,b):
    a=a+10
    b=b+20
    c=a+b
    return a,b,c
data=f1(3,4)
print(data)
x,y,z=f1(10,20)
print(f"x={x} y={y} z={z}")

# This is Tuple of size 1
a=12,  # a=(12,)
print("%d " %(34,))

def addition(a=3,b=6,*x):  # *x for expansion of tuple
    s=a+b
    for n in x:
        s=s+n
    return s
print("addition: ",addition(34,87,1,2,5,11))
a=(12)
print(type(a))
a=(12,)
print(type(a))

