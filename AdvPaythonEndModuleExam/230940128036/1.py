# Function take 2 list from user and operations to be performed
def list_operations():
    list_1=[]
    list_2=[]
    # 1st list(list of strings) taken from user
    print("Enter values for list_1:\n")
    ch='y'
    while ch=='y':        
        if len(list_1)<4:
            val=input("Enter element: ")
            list_1.append(val)
        else:
            print("You can enter only 4 elements.")
            break
        ch=input("Do you want to add more element?(y/n) ")
   
    
    # 2nd list(list of no's) taken from user
    print("Enter values for list_2:\n")
    ch='y'
    while ch=='y':        
        if len(list_2)<4:
            val=int(input("Enter a No: "))
            list_2.append(val)
        else:
            print("You can enter only 4 No's.")
            break
        ch=input("Do you want to add more element?(y/n) ")
    
    # operations for lists
    while ch!=4:
        ch=int(input("""
        1. Create Dictionary
        2. Add element in list 1
        3. Delete element from list 2
        4. Exit
        Choice: """))
        match ch:
            case 1:
                d={}
                for tpl in zip(list_1,list_2):
                    d[tpl[0]]=tpl[1]
                print(d)
                             
            case 2:
                val=input("Enter element: ")
                list_1.append(val)
                print(list_1)
            case 3:
                print(f"List_2: {list_2}")
                try:
                    val=int(input("Enter no to be deleted: "))
                    list_2.remove(val)
                    print(list_2)
                except:
                    print("No not Found. ")
            case 4:
                print("Thank You")
    

list_operations() # function call














