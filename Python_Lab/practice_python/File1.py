id=[]
name=[]
ds=[]
sal=[]
dp=[]
with open("data.txt") as fh:
    for line in fh:
        l=[]
        line=line.rstrip('\n')
        l=line.split(':')
        id.append(l[0])
        name.append(l[1])
        dp.append(l[2])
        ds.append(l[3])
        sal.append(l[4])
    print(id)
    print(name)
    print(ds)
    print(dp)
    print(sal)
    