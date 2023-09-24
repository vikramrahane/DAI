def f():
    global cnt
    cnt+=1
    print(f"Count of fn call is : {cnt}")
    
cnt=0
for i in range(5):
    f()


def f1(a,b=4,c=5):
    z=b+c
    z=a+z
    return z
ans=f1(c=9,a=3,b=0)   # Keyword arguments
print(f"fn return : {ans}")
def f2():
    print(cnt)
cnt=10
def f3():
    x=34
    print(x)
x=10
print(x)
f3()
print(x)
print("********nested fn*******")
def ff1():
    x=34
    print(x)
    def ff2():
        global x
        x=45
        print(x)
    print(x)
    ff2()
    print(x)

x=10
print(x)
ff1()
print(x)

print("********nested fn for nonlocal*******")
def ff1():
    x=34
    print(x)
    def ff2():
        nonlocal x
        x=45
        print(x)
    print(x)
    ff2()
    print(x)

x=10
print(x)
ff1()
print(x)

print("*********** bit operation **************")
x=9
print(x,bin(x))
y=11
print(y,bin(y))

newnum=x<<4
newx=newnum|y
print("*********************")
s="dfghk khkjh khkj "
print(s[0::-1])
print(s[-15:9:1])
print(s[::2])
print(s[1::2])
print(s[3:10])
print(s[-5:0:-1])


s="a cat a cat a cat a cat a cat a cat a cat a cat "
print("occurance From Left to right")
pos=0
while pos!=-1:
    pos=s.find("cat",pos+1)
    print(pos) if pos!=-1 else print()

print("occurance From right to Left")
pos=0
while pos!=-1:
    pos=s.rfind("cat",0,pos-1)
    print(pos) if pos!=-1 else print()
    
print("2nd logic")
s="cat a cat a cat a cat a cat a cat a cat a cat a cat "
print("occurance From Left to right")
pos=-1
while True:
    pos=s.find("cat",pos+1)
    if pos!=-1:
        print(pos)
    else:
        break

print("occurance From right to Left")

pos=-1
while True:
    pos=s.rfind("cat",0,pos-1)
    if pos!=-1:
        print(pos)
    else:
        break























