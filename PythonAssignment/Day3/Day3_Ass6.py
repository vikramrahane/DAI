s = "Welcome to USA. usa awesome, isn't it?"
pos=s.lower().rfind("USA".lower())
while pos!=-1:
    print(pos)
    pos=s.lower().rfind("USA".lower(),0,pos)

s = "Welcome to USA. usa awesome, isn't it?"
pos=s.casefold().rfind("USA".casefold())
while pos!=-1:
    print(pos)
    pos=s.casefold().rfind("USA".casefold(),0,pos)
