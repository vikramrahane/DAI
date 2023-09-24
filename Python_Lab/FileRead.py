import re
lst=[]
fh=open("mydata.txt")  # Default is 'r' mode read only mode
for line in fh:
    line=line.rstrip("\n")
    print(line)
    lst.append(line)
print(lst)
fh.close()

# copy one file into another file
fh=open("mydata.txt")
fh1=open("mycopy.txt","w")
for line in fh:
    fh1.write(line)
fh.close()
fh1.close()

fh=open("mydata.txt")
fh1=open("mycopy.txt","w")
for line in fh:
    if re.search("game", line):
        fh1.write(line)
fh.close()
fh1.close()

fh=open("mydata.txt")
fh1=open("mycopy.txt","w")
for line in fh:
    l=line.split(":")
    if l[2]=="game":
        fh1.write(line)
fh.close()
fh1.close()

with open("mydata.txt") as fh:  # file close with end of with statement
    with open("mycopy.txt","w") as fh1:
        for line in fh:
            if line!="\n":
                l=line.split(":")
                if l[2]=="game":
                    fh1.write(line)
                    print(line)

with open("mydata.txt") as fh:
    s=0
    for line in fh:
        l=line.split(":")
        s=s+int(l[4])
print("sum of salaries of all employees: ",s)

with open("data.txt") as fh:
    lst=fh.readlines()
    print(lst)
























