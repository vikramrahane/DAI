with open("data.txt") as fh:
    l=fh.readlines()
    print(l)
    fh.seek(0)
    s=fh.read()[3:14]
    print(s)