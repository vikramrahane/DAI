def prime(n):
    for i in range(2,n):
        if n%i==0:
            return -1
            break
    else:
        return 1
a=int(input("Enter a 1st No:"))
b=int(input("Enter a 2nd No:"))
x=a
y=b
hcf=1
while x!=1 or y!=1:
    for i in range(2,a if a<b else b):
        if prime(i):
            if x%i==0 and y%i==0:
                hcf=hcf*i
                x=x/i
                y=y/i
            elif x%i==0:
                x=x/i
            elif y%i==0:
                y=y/i
            else:
                pass
print(f"HCF of {a} and {b} is {hcf}")
