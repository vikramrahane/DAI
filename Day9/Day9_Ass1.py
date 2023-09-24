class Student:
    cnt=0
    def __init__(self,sname="",m1=0,m2=0,m3=0):
        Student.cnt=Student.cnt+1
        self.__sid=Student.cnt
        self.__sname=sname
        self.__m1=m1
        self.__m2=m2
        self.__m3=m3
        
    def __str__(self):
        return f"ID: {self.__sid}, Name: {self.__sname}, M1: {self.__m1}, M2: {self.__m2}, M3: {self.__m3}"
    
    #Setter methods
    def set_sid(self,x):
        self.__sid=x
    def set_sname(self,x):
        self.__sname=x
    def set_m1(self,x):
        self.__m1=x
    def set_m2(self,x):
        self.__m2=x
    def set_m3(self,x):
        self.__m3=x
        
    #getter methods
    def get_sid(self):
        return self.__sid
    def get_sname(self):
        return self.__sname
    def get_m1(self):
        return self.__m1
    def get_m2(self):
        return self.__m2
    def get_m3(self):
        return self.__m3
        
s1=Student("Vikram",99,98,99)
print(s1)
s2=Student("Pradhyumn",40,41,42)
print(s2)