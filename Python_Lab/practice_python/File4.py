with open("data.txt") as fh1,open("write_data.txt","w") as fh2:
    for l in fh1:
        fh2.write(l)