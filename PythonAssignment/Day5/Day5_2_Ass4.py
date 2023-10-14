list1 = ["Hello ", "Welcome "] 
list2 = ["Students", "Sir"] 
l=[i+j for i in list1 for j in list2]
'''for i in list1:
    for j in list2:
        l.append(i+j)'''
print(l)