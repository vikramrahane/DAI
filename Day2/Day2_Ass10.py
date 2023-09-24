n=int(input("Enter a No of terms: "))
x=int(input("Enter the value of x: "))
s=0
for i in range(n):
    c=((-1)**i)*(x**((2*i)+1))
    print(f"{c} ",end="")
    s=s+c
print(f"\nsum of series of terms {n} and x={x} : {s}")
