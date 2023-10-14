str1=input("Enter a String: ")
str2=input("Enter a String to search: ")
pos=str1.find(str2)
cnt=1
while pos!=-1:
    print(f"{str2} - {pos}")
    pos=str1.find(str2,pos+1)
    cnt+=1
print("Count: ",cnt)
