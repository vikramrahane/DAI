import sys
lst=[7,14,556,3,25,1,41,66]
while True:
    print("""\n
1. Accept Data
2. Delete data by value
3. Delete data by position
4. Sort
5. Reverse
6. Sort without change in original
7. Reverse without change in original
8. Display Data
9. Exit""")
    ch=int(input("Enter a choice: "))
    if ch==1:
        while True:
            print("\na. at last position\nb. at given position\nc.Back")
            ch1=input("Enter a choice: ")
            if ch1=='a':
                x=int(input("Enter a No: "))
                lst.append(x)
            elif ch1=='b':
                x=int(input("Enter a No: "))
                pos=int(input("Enter a position: "))
                lst.insert(pos,x)
            elif ch1=='c':
                break
            else:
                print("Wrong Choice")
    elif ch==2:
        x=int(input("Enter a value to remove: "))
        if x in lst:
            lst.remove(x)
            print(f"Element {x} Deleted.")
        else:
            print(f"{x} not Found")
    elif ch==3:
        while True:
            print("a. at last position\nb. at given position\nc.Back")
            ch1=input("Enter a choice: ")
            if ch1=='a':
                lst.pop()
                print("Last Element Deleted.")
            elif ch1=='b':
                pos=int(input("Enter a position: "))
                lst.pop(pos)
                print(f"Element Deleted from position {pos}.")
            elif ch1=='c':
                break
            else:
                print("Wrong Choice")
    elif ch==4:
        while True:
            print("a.Sort by Ascending\nb. Sort by Descnding \nc.Back")
            ch1=input("Enter a choice: ")
            if ch1=='a':
                lst.sort()
                print(lst)
            elif ch1=='b':
                lst.sort(reverse=True)
                print(lst)
            elif ch1=='c':
                break
            else:
                print("Wrong Choice")
    elif ch==5:
        lst.reverse()
        print(lst)
    elif ch==6:
        print("Sorted List: ",sorted(lst))
        print("Original List: ",lst)
    elif ch==7:
        rlst=[]
        for i in reversed(lst):
            rlst.append(i)
            
        print("Reversed List: ",rlst)
        print("Original List: ",lst)
    elif ch==8:
        while True:
            print("a. Normal\nb. Numbered\nc.Back")
            ch1=input("Enter a choice: ")
            if ch1=='a':
                print(lst)
            elif ch1=='b':
                for i in range(len(lst)):
                    print(f"{i} {lst[i]}")
            elif ch1=='c':
                break
            else:
                print("Wrong Choice")
    elif ch==9:
        sys.exit()
    else:
        print("Wrong Choice")
