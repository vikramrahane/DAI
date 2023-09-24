s="cat a cat a cat a cat a cat a cat a cat a cat a cat "
print("occurance From Left to right")
pos=-1
while True:
    pos=s.find("cat",pos+1)
    if pos!=-1:
        print(pos)
    else:
        break

print("occurance From right to Left")
pos=0
while pos!=-1:
    pos=s.rfind("cat",0,pos-1)
    print(pos) if pos!=-1 else print()
    
