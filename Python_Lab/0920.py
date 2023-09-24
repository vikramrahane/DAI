import re
s="Something is there somewhere"
m=re.search("t.*?e",s,re.I|re.M)
if m!= None:
    print(m.group())
    print(m.span())
else:
    print("Not Found")
    
m=re.match("s.*?e",s,re.I|re.M)
if m!= None:
    print(m.group())
    print(m.span())
else:
    print("Not Found")

s="Something is there somewhere"
m=re.search("\bis\b",s,re.I|re.M)
if m!= None:
    print(m.group())
    print(m.span())
else:
    print("Not Found")
    
s1="*************hgjfdkghjkdfh"
m=re.search("\*.*",s1,re.I|re.M)  # '.' Single any character, Use \

if m!= None:
    print(m.group())
    print(m.span())
else:
    print("Not Found")
    
s="Something is there somewhere"
lstm=re.finditer("s.*?e",s,re.I|re.M) # It return iterator list of strings found with position
if lstm!= None:
    for m in lstm:
        print("*** Occurance***")
        print(m.group())
        print(m.span())
else:
    print("Not Found")
    
s="Something is there somewhere"
lst=re.findall("s.*?e",s,re.I|re.M)   # It return only list of strings found
if lst!= None:
        print(lst)
else:
    print("Not Found")   
    
s="Something is there somewhere"
s1=re.sub("s.*?e","any",s,flags=re.I|re.M) # It replaces given string by pattern
print(s1)
    
s="Something is there somewhere" 
s1=re.sub("s.*?e","any",s,count=2,flags=re.I|re.M) # count=1st 2 occurances only
print(s1)  
    
myreg=re.compile("s.*?e",re.I|re.M) # set a object of regular expression
m=myreg.search(s)
if m!=None:
    print(m.group())
    print(m.span())
else:
    print("not found")

s1=myreg.sub("any",s)
print(s1)   

s1=myreg.sub("any",s,2)
print(s1)  
    

s="Something is there somewhere"
lstm=re.finditer("s.*?e|.re",s,re.I|re.M) # It return iterator list of strings found with position
if lstm!= None:
    for m in lstm:
        print("*** Occurance***")
        print(m.group())
        print(m.span())
else:
    print("Not Found")
    
    
    
    
    
    
    
    
    
    
    
    
    
    