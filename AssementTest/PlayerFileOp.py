import re
with open("player.txt") as fh:
    for line in fh:
        line=line.rstrip("\n")
        m=re.match("2.*g$", line)
        if m!=None:
            print(line)
    