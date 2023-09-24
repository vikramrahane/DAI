print()
s="cat a cat a cat a cat a cat a cat a cat a cat a cat a"
print("occurance From Left to right")

pos=s.find("cat")
while pos!=-1:
    print(pos)
    pos=s.find("cat",pos+1)
print(f"Count of cat {s.count('cat')}")

print("occurance From right to Left")

pos=s.rfind("cat")
while pos!=-1:
    print(pos)
    pos=s.rfind("cat",0,pos)
print(f"Count of cat {s.count('cat')}")

print(s.replace("cat","Dog",3))
print('IX'.isnumeric())


print("*"*20)
s1="Thi is , test"
print('uppercase',s1.upper())
print('lowercase',s1.lower())
print("startswith",s1.startswith("Thi"))
print("split",s1.split(" "))
print("split",s1.split(","))
print("endswith",s1.endswith("est"))
s2="asdadsdsx this is string adxadxs"
print("strip:",s2.strip('adxs'))

l=["sdsd","6767","mmm"]
print(":".join(l))
print("1234".isdecimal())
print("Isdf".isalpha())
print("This is new is this".replace("is","xxxxx",1))

print("*"*20)
a=12
b=a
c=12
print(id(a),id(b),id(c))
d=int(input("Enter a No"))
print(id(a),id(b),id(c),id(d))
a=10
print(id(a),id(b),id(c))

print("*"*20)
s="YOYO"
t=s
x="AWAW"
y=input("Enter a string")
print(id(s),id(t),id(x),id(y))

print("List")
lst=[1,4,2,3,5,6]
lst1=['python','perl','test']
lst2=[12,12 ,34,12,'xxxx','bbb',34,56,[34,56,78],24]
print(lst2[8][1])
print(lst[3])

print("length ",len(lst1))
lst[3]=45
print(lst)

for i in lst1:
    for j in i:
        print(j)

st="This is data"
for i in st:
    print(i)














