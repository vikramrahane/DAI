#******* Set *******
s=set("vikram rahane")
print(s)
s=set(['python','pearl','os','linux','Python'])
print(s)

s={12,45,78,18,(1,2),"data"}
print(s)

s.add(100)
print(s)
#s.add(['a','b','c'])  gives error list is mutable data
s.update(['a','b','c']) # it work because update add value one by one
print(s)

print(s.pop()) # delete data randomly
print(s)

s.remove(45)  #if not found throws exception
print(s)

s.discard(12)   #if not found then ignore
print(s)

s1={1,2,4,3}
s2={11,12,4,2}
print(s1,"\n",s2)
print("Union",s1.union(s2))
print("Union",s1.intersection(s2))
print("Union",s1.difference(s2))
print("Union",s2.difference(s1))
print("Union",s1.symmetric_difference(s2))
s3={2,4,7,8}
s1.difference_update(s2)
print(s1)
s3.symmetric_difference_update(s2)
print(s3)


s1={1,2,4,3}
s2={11,12,4,2}
print(s1,"\n",s2)
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))

s1={1,2,4,3}
s2={4,2}
print(s1,"\n",s2)
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))

s1={2,4}
s2={11,12,4,2}
print(s1,"\n",s2)
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))

s1={2,4}
s2={11,12}
print(s1,"\n",s2)
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))
