from class_student_management import *

student_list=[]
    
ch=1       
while ch!=5:
    ch=int(input("""
    1. Add New Student
    2. Update Student Name
    3. Delete Student Name
    4. Display Student List
    5. Exit
    Choice: """))
    match ch:
        case 1:
            try:
                stud_obj=student_management() # create student_management class object
                val=input("Enter Student Name: ")  
                for l in student_list:
                    if l.get_name()==val:
                        raise(val)
                stud_obj.set_name(val)        #call class method          
                student_list.append(stud_obj) # add student object into list
                print("Student added Successfully")               
                    
            except:
                print(f"Student Name {val} already exists.")  #if student name already exists in the List
        case 2:
            try:
                old_name=input("Enter Old Name: ")
                new_name=input("Enter New Name: ")
                for l in student_list:
                    if l.get_name()==old_name:
                        l.set_name(new_name)
                        
            except Exception as e:
                print(e)
        case 3:
            try:
                name=input("Enter Student Name: ")
                for l in student_list:
                    if l.get_name()==name:
                        student_list.remove(l)
                        print("Deleted Successfully")
            except Exception as e:
                print(e)
        case 4:
            try:
                print("Studen List: ")
                for l in student_list:
                    print(l.get_name(),end=", ")
                        
            except Exception as e:
                print(e)
        case 5:
            print("Thank You")                    