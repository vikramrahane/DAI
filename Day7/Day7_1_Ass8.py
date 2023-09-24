Dict = { 
 'emp1': {'name': 'Jhon', 'salary': 7500}, 
 'emp2': {'name': 'Emma', 'salary': 8000}, 
 'emp3': {'name': 'Brad', 'salary': 6500} 
}
def modifysalary(en,nsal):
    modk=-1
    for k,v in Dict.items():
        for k1,v1 in v.items():
            if v1==en:
                modk=k
                break
    if modk!=-1:
        if nsal>Dict[modk]['salary']:
            Dict[modk]['salary']=nsal
            return 1
        else:
            return 2  
    else:
        return 3
    
en=input("Enter Name of Employee: ")
nsal=int(input("Enter Salary: "))
status=modifysalary(en,nsal)
if status==1:
    print("Found and modify Successfully.")
elif status==2:
    print("Found but New Salary<old salary")
else:
    print("Not Found")
print(Dict)