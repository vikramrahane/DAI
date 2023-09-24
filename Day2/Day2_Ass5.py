a=0
cnt=0
n=int(input("Enter a No: "))
while n!=0:
    d=n%10
    cnt+=1
    a=a+d
    n=n//10
print(f"Count of Digit is {cnt} and sum of all digits is {a}")
