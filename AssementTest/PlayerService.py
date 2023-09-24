from Player import *
playerinfo={}
def addnewplayer(tname):
    pname=input("Enter Player Name: ")
    special=input("Enter Player's Specialization: ")
    charges=input("Enter Player's charges: ")
    obj=Player(pname,special,charges,tname)
    playerinfo[obj.get_pid()]=obj
    
def addnewteam(tname):
    choice='y'
    while choice=='y':
        addnewplayer(tname)
        choice=input("Do you want to add more player?(y/n) ")
   
def deletebyteam(tname):
    lst=[]
    for k,v in playerinfo.items():
        if v.get_tname()==tname:
            lst.append(k)
    if len(lst)>0:
        choice=input(f"Do you really want to delete the Team {tname}?(y/n) ")
        if choice=='y':
            for k in lst:
                playerinfo.pop(k)  
            return 1
        else:
            return 2         
    else:
        return 3

def displayall():
    for v in playerinfo.values():
        print(v)
def searchbyid(pid):
    v=playerinfo.get(pid,-1)
    return v
    
def modifybyid(pid,charg):
    v=searchbyid(pid)
    if v!=-1:
        choice=input(f"Do you really want to Modify charges of the Player {pid} to {charg}?(y/n) ")
        if choice=='y':
            v.set_charges(charg)
            return 1
        else:
            return 2
    else:
        return 3
def totalcharges():
    totalcharge={}
    for v in playerinfo.values():
        tname=v.get_tname()
        charge=v.get_charges()
        if tname in totalcharge.keys():
            totalcharge[tname]=totalcharge[tname]+float(charge)
        else:
            totalcharge[tname]=float(charge)
    return totalcharge
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    