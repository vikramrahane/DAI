a=0
p=1
cnt=0
while True:
    n=int(input("Enter a No: "))
    cnt+=1
    a=a+n
    p=p*n
    s=input("Do you wwant to quit(q):")
    if s=='q':
        break
print(f"Average value is {a/cnt} and Product of all no's is {p}")
