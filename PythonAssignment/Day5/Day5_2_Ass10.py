list1 = [5, 10, 15, 20, 25, 50, 20]
for i in range(list1.count(20)):
    list1.pop(list1.index(20))
    
#list1=[x for x in list1 if x!=20]
print(list1)