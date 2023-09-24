'''User defined Functions which return tuple'''
def del_lst(lst,val):
    cnt=0
    while val in lst:
        cnt+=1
        lst.remove(val)
    if cnt==0:
        return val,-1
    else:
        return val,cnt
    
l=[6,71,4,9,6,2,23,6]
print(del_lst(l,66))
val,occur=del_lst(l,66)   # Unpacking of tuple
print(val,occur)

def search(lst,val):
    if val in lst:
        return val,lst.index(val)
    else:
        return val,-1

print(search(l,23))
val,pos=search(l,23)
print(f"value={val} and its position is {pos}")
