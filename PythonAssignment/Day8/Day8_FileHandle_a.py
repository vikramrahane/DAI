import re
with open("productdata.txt") as fh:
    with open("myproduct.txt",'w') as fh1:
        for line in fh:
            line.rstrip('\n')
            m=re.match("^12.*0$", line)
            if m!=None:
                fh1.write(line)
            else:
                print(line)
