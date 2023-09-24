citytree={}
def addnewcity():
    city=input("Enter a City Name: ")
    treelst=[]
    
    ch='y'
    while ch=='y':
        tree=input("Enter a Tree Name: ")
        treelst.append(tree)
        ch=input("Do you want to ad more Trees?(y/n) ")
    citytree[city]=treelst
def displayall():
    for k,v in citytree.items():
        print(f"{k} : {v}")
def searchbycity(city):
    if city in citytree.keys():
        return citytree[city]
    else:
        return -1
def displaybytree(tree):
    print(f"Cities in which {tree} commonly found : ",)
    for k,v in citytree.items():
        if tree in v:
            print(k,end=", ")
def deletebycity(city):
    status=searchbycity(city)
    if status!=-1:
        ch=input(f"Do you really want to delete city {city}?(y/n) ")
        if ch=='y':
            citytree.pop(city)
            return 1
        else:
            return 2
    else:
        return 3
def modifybycity(city):
    status=searchbycity(city)
    if status!=-1:
        ch=input(f"Do you really want to Modify city {city}?(y/n) ")
        if ch=='y':
            treelst=[]            
            ch1='y'
            while ch1=='y':
                tree=input("Enter a Tree Name: ")
                treelst.append(tree)
                ch1=input("Do you want to ad more Trees?(y/n) ")
            citytree[city].extend(treelst)
            return 1
        else:
            return 2
    else:
        return 3
ch=0
while ch!=7:
    ch=int(input("""
    1.Add new city and trees commonly found in the city. 
    2.Display all cities and the list of trees for all cities. 
    3.Display list of trees of a particular city. 
    4.Display cities which have the given tree. 
    5.Delete city
    6.Modify tree list for given city
    7.Exit
    Choice: """))
    match ch:
        case 1:
            addnewcity()
        case 2:
            displayall()
        case 3:
            city=input("Enter a city name: ")
            status=searchbycity(city)
            if status!=-1:
                print(f"{city} : {status}")
            else:
                print("City Not Found")
        case 4:
            tree=input("Enter a Tree name: ")
            displaybytree(tree)
        case 5:
            city=input("Enter a city name: ")
            status=deletebycity(city)
            if status==1:
                print("City found and Deleted Successfully.")
            elif status==2:
                print("City found but not Deleted.")
            else:
                print("City Not Found")
        case 6:
            city=input("Enter a city name: ")
            status=modifybycity(city)
            if status==1:
                print("City found and Modified Successfully.")
            elif status==2:
                print("City found but not Modified.")
            else:
                print("City Not Found")
        case 7:
            pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        