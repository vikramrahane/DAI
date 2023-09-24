d={"DBDA":(100,60),"DAI":(200,50)}
print("length:",len(d))

#to add a new key value pair
d["DAC"]=(230,240)
print("length: ",len(d))
print(d)

d1={(1,2):"xxxx",(3,4):"tttt"}
print(d1[(1,2)])

#to add a new key value pair if key exist then value will be override
d["DAC"]=(200,240)
print("length: ",len(d))
print(d)

#To check whether key exists or not. If default value not given it return 
#None if key not found otherwise return default value
v=d.get("DBDA1")  # v=d.get(
if v==None:
    print("Not Found")
else:
    print("key found and value is: ",v)
print(d)
   #To check whether key exists or not. If key not found then it add new key,value pair
d1={"DBDA":(100,60),"DAI":(200,50)}
v=d1.setdefault("DBDA1",-1)  # v=d.get(
if v==-1:
    print("Not Found so added")
else:
    print("key found and value is: ",v)
print(d1)

#to navigate through keys and values
d={"DBDA":(100,60),"DAI":(200,50),"DAC":(200,240)}
for k in d.keys():
    print(f"{k}--->{d[k]}")
    
for k,v in d.items():
    print(f"{k}---->{v}")
    
for i in d.items():
    print(i)
    
# show items in which capacity > 50
 #1st Sol
for k,v in d.items():
    if v[1]>100:
        print(f"{k}---->{v}")
    #2nd Sol    
for k in d.keys():
    if d[k][1]>100:
        print(f"{k}--->{d[k]}")

print(d.values())

# pop() if not found and default value not given it throws Exception
v=d.pop("DAC",-1)
if v==-1:
    print("Not Found")
else:
    print("Deleted")
print(v,d)

data={"DBDA":(100,60),"DAI":(200,50),"DAC":(200,240)}
data.popitem() # delete last pair
print(data)

d1={"a":10,"b":40}
d2={"a":25,"c":80}

d1.update(d2) #value of key 'a' is voverride
print(d1)

d1={"a":10,"b":40}
d2={"a":25,"c":80}
d3={**d1,**d2}
print(d3)

l=[11,12,13]
d=dict.fromkeys(l)
print(d)

d=dict.fromkeys(l,100)
print(d)

d=dict.fromkeys("vikram")
print(d)

d1={1:23,'a':'djfv'}
print(d1)

















