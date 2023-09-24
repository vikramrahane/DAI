list1 = ["M", "na", "i", "Raj"] 
list2 = ["y", "me", "s", "esh"] 
l=[list1[i]+list2[i] for i in range(len(list1))]
'''
l=[]
for i in range(len(list1)):
    l.append(list1[i]+list2[i])
'''
print(l)