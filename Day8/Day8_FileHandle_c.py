import re
categ=input("Enter a Category: ")
with open("productdata.txt") as fh:
    for line in fh:
        m=re.search(categ, line)
        if m!=None:
            print(line)