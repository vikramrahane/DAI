lst=[10,20,30,10]
lst.append("Hello")
print(len(lst))
lst.extend("Testing")
print(len(lst))
print(lst)
print(lst.count(10))
#lst.reverse()
lst.pop()
print(lst)
lst.pop(2)
print(lst)
lst.remove('t')
print(lst)
if 100 in lst:
    lst.remove(100)
else:
    print("not found")
del(lst[3])
print(lst)
lst.remove(10)
print(lst)
print(lst.index('i'))
if 'gh' in lst:
    print(lst.index('gh'))
else:
    print("not found")

l=[8,2,7,1,0,4,7,13,2,7,87,2]
l.sort()#ascending
print(l)
l.sort(reverse=True)#desending
print(l)

s=["jhhl","detgf","dsf","affaf"]
s.sort()
print(s)
s.reverse()
print(s)
print("**********shallowcopy*******")
c=[12,23,34]
c1=c
c.append(100)
print(c)
print(c1)

c=[12,23,34]
c1=c.copy()
c.append(100)
print(c)
print(c1)

print("**********Deep copy(is necessary if there is nested list)(Mutable data type inside mutable data type)*******")

import copy
l=[1,2,3,[9,8,7]]
l1=copy.deepcopy(l)
l[3].append(100)
l.append('Hello')
print(l)
print(l1,"\n")

l=[1,2,3,[9,8,7]]
print(l)
l2=l.copy() #shallow copy
l[3].append(50)
l.append('Hello')
print(l)
print(l2,"\n")

l=[1,2,3,[[11,12],9,8,7]]
l1=copy.deepcopy(l)
l[3][0].append(100)
print(l)
print(l1)


print("******* ZIp Fn *********")
#To read data simoultaniously from multiple lists
l1=[12,1,14]
l2=["Pune",'delhi','Mumbai']
print(zip(l1,l2))
for i in zip(l1,l2):
    print(i[0],"----->",i[1])

for x,y in zip(l1,l2):
    print(f"{x}---->{y}")


for pos,val in enumerate(l1):
    print(pos,"---->",val,"\n")

l1=[12,1,14,2,9,4]
for i in sorted(l1):
    print(i,end=" ")
print(l1,"\n")

l1=[12,1,14,2,9,4]
for i in sorted(l1,reverse=True):
    print(i,end=" ")
print(l1,"\n")

l1=[12,1,14,2,9,4]
for i in reversed(l1):
    print(i,end=" ")
print(l1,"\n")





























