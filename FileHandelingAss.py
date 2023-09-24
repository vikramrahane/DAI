with open("data.txt") as fh:
    d={}
    for line in fh:
        line=line.rstrip("\n")
        l=line.split(":")
        if l[4] in d.keys():
            d[l[4]]=d[l[4]]+int(l[3])
        else:
            d[l[4]]=int(l[3])
print(d)