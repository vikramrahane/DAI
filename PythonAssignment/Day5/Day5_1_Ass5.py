lst=[1,3,5,1]
'''ind=0
cnt_lst=0
l1=[]
while cnt_lst!=len(lst): 
    if ind in lst:
        l1.append(lst.index(ind))
        cnt_lst+=1
    else:
        l1.append(-1)
    ind+=1
print(l1)'''
print(lst)
l=[-1 for i in range(max(lst)+1)]
for i in enumerate(lst):
    l[i[1]]=i[0]
print(l)
