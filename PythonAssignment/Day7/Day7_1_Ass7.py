Dict = { 
 'Physics': 82, 
 'Math': 65, 
 'history': 99
} 
max=0
maxk=-1
for k,v in Dict.items():
    if v>max:
        max=v
        maxk=k
print(f"Key of Maximum value : {maxk}")