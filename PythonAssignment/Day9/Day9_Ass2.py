import sys
from StudentService import *
ch='y'
while ch=='y':
    choice=int(input("""
    1. Display All Student
    2. Search by id
    3. Search by name
    4. calculate GPA of a student
    5. Add New Student
    6. Exit 
    Choice :"""))
    match choice:
        case 1:
            displayall()            
        case 2:
            i=int(input("Enter Student ID: "))
            stud=searchbyid(i)
            if stud!=-1:
                print(stud)
            else:
                print("Student not Found")
        case 3:
            i=input("Enter Student name: ")
            stud=searchbyname(i)
            if stud!=-1:
                print(stud)
            else:
                print("Student not Found")
        case 4:
            i=int(input("Enter Student ID: "))
            stud=calgpa(i)
            if stud!=-1:
                print(f"gpa of student {i} :{stud}")
            else:
                print("Student not Found")
        case 5:
            addnewstud()
        case 6:
            sys.exit(0)
        case _:
            print("Wrong Choice")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        