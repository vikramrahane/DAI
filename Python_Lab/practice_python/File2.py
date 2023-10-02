#Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".  
with open("data.txt") as fh:
    cnt=0
    l=0
    w=0
    for line in fh:
        l=l+len(line)
        lst=[]
        lst=line.split(":")
        w=w+len(lst)
        if line.startswith('2'):
            pass
        else:
            cnt+=1
        for x in line:
            print(x+"#",end="")
    print(cnt)
    print("Total Characters= ",l)
    print("Total words= ",w)
    
