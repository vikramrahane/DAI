#a
print("Pattern a")
n=int(input("Enter Height"))
for i in range(n):
    print("*"*(i+1))
#b
print("Pattern b")
n=int(input("Enter Height"))
if n%2==0:
    print("Height should be Odd")
else:
    cnt=n//2
    for i in range(1,n+1,2):
        print(" "*cnt+"*"*i,sep="")
        cnt-=1
    cnt=1
    for j in range(n-2,0,-2):
        print(" "*cnt+"*"*j,sep="")
        cnt+=1
#c
print("Pattern c")
n=int(input("Enter Height"))
for i in range(n-1,-1,-1):
    print(" "*(n-i-1),end="")
    for j in range((2*i)+1):
        print("1",end="") if j%2==0 else print("0",end="")
    print()
#d
print("Pattern d")
n=int(input("Enter Height"))
for i in range(n):
    for j in range(1,i+2):
        print(j,end="")
    print()
