import sys
set1=set()
ch='y'
while ch=='y':
    val=input("Enter a Name: ")
    set1.add(val)
    ch=input("Do you want to add more(y/n)? ")
while True:
    ch=int(input("""1. delete element if exists otherwise do not show any errr
    2. add a elemet
    3. create one more set
    4. union of 2 sets
    5. intersection of 2 sets
    6. difference of 2 sets 
    7. convert set into frozenset
    8. Display
    9. exit
    Choice: """))
    match ch:
        case 1:
            val=input("Enter a name for delete: ")
            if val in set1:
                status=input(f"Do you really want to delete {val}?(y/n) ")
                if status=='y':
                    set1.discard(val)
                    print("Found & deleted successfully")
                else:
                    print("Found but not deleted")
            else:
                print("Not Found")
            
        case 2:
            val=input("Enter a name: ")
            if val in set1:
                print("Exists")
            else:
                set1.add(val)
        case 3:
            set2={''}
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            pass
        case 8:
            print(set1)
        case 9:
            sys.exit(0)
        case others:
            print("Wrong choiced",ch)