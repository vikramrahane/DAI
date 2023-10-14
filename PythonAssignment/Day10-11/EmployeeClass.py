class Employee:
   
    def __init__(self,eid=1,ename="",sal=0,mob=""):        
        self.__eid=eid
        self.__ename=ename
        self.__sal=sal
        self.__mob=mob       
        
    def __str__(self):
        return f"ID: {self.__eid}, Name: {self.__ename}, M1: {self.__sal}, M2: {self.__mob}"
    
   
    #Setter methods
    def set_eid(self,x):
        self.__eid=x
    def set_ename(self,x):
        self.__ename=x
    def set_sal(self,x):
        self.__sal=x
    def set_mob(self,x):
        self.__mob=x
            
    #getter methods
    def get_mob(self):
        return self.__mob
    def get_sal(self):
        return self.__sal
    def get_eid(self):
        return self.__eid
    def get_ename(self):
        return self.__ename