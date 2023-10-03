class student_management:
    #Constructor
    def __init__(self,name=""):
        self.__name=name
    # when to print object
    def __str__(self):
        return f"Student Name: {self.__name}"
    
    #setter method
    def set_name(self,name):
        self.__name=name
    
    #getter method
    def get_name(self):
        return self.__name   
        