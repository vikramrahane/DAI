import re
with open("data.txt") as fh:
    for line in fh:
        m=re.search("game",line)
        if m!= None:
            print(m)