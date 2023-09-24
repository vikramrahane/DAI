import math
n=int(input("Enter a No of terms: "))
x=int(input("Enter the value of x: "))
s=0
for i in range(n):
    c=(x**i)/math.factorial(i)
    print(f"+{c:.{2}f}",end="")
    s=s+c
print(f"\nsum of series of terms {n} and x={x} : {s}")
