m=int(input("How many days in month: "))
w=int(input("begining day of month: "))
print("Mo\tTu\tWd\tTh\tFr\tSa\tSu")
print(f"\t"*w,end="")
x=w
for i in range(1,m+1):
    if x!=6:
        print(i,end="\t")
        x+=1        
    else:
        print(i)
        x=0
