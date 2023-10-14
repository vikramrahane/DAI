d={}
with open("productdata.txt") as fh:
    for line in fh:
        line.rstrip('\n')
        lst=line.split(':')
        if lst[3] in d.keys():
            d[lst[3]]=d[lst[3]]+int(lst[4])
        else:
            d[lst[3]]=int(lst[4])
print(d)
        