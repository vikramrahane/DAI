ch=int(input("Enter a No"))
match ch:
    case 1:
        print("Case 1 ")
    case 2:
        print("case 2")
    case _:
        print("Wrong Choice")

c=input("Enter a color")
match c:
    case 'red'|'yellow':
        print("Select red or yellow")
    case 'green':
        print("Green Green Green")
