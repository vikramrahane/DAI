from abc import ABC,abstractmethod
class Person:
    count=0  #static variable
    #constructor
    def __init__(self,etype="",pn="",mob=""):
        
        Person.count=Person.count+1
        self.__pid=etype+str(Person.count)
        self.__pname=pn
        self.__mobno=mob
    
    @staticmethod   # use decorator if not given it take val as self
    def myf(val): # static fn with parameter
        print("in myfunction",val,Person.count)
        
    def __str__(self):
        return f"ID: {self.__pid} NAme: {self.__pname}, Mobile: {self.__mobno},"
    #Setter to modify only pid
    def set_pid(self,x):
        self.__pid=x
    #IT retrive only pid
    def get_pid(self):
        return self.__pid
    #Setter to modify only pname
    def set_pname(self,x):
        self.__pname=x
    #IT retrive only pname
    def get_pname(self):
        return self.__pname
    #Setter to modify only Mobile No
    def set_mob(self,x):
        self.__mobno=x
    #IT retrive only mobile no
    def get_mob(self):
        return self.__mobno
    
class Employee(Person,ABC):
    def __init__(self,etype="",pname="",mob="",dt="",ds=""):
        super().__init__(etype,pname,mob)
        self.__dept=dt
        self.__desg=ds
    def __str__(self):
        return super().__str__()+f" dept: {self.__dept}, desg: {self.__desg},"
    
    @abstractmethod       ################
    def calculatesal(self):
        pass
    #Setter methods
    def set_dept(self,x):
        self.__dept=x
    def set_desg(self,x):
        self.__desg=x
        
    #getter methods
    def get_pname(self):
        return self.__dept
    def get_mob(self):
        return self.__desg

class SalariedEmp(Employee):
    def __init__(self,pname="",mob="",dt="",ds="",sal=1000):
        super().__init__("S",pname,mob,dt,ds)
        self.__sal=sal
        self.__bonus=0.10*sal
    def __str__(self):
        return super().__str__()+f" Salary: {self.__sal}, Bonus: {self.__bonus}"
    
    def calculatesal(self):
        return self.__sal+self.__sal*0.10+self.__sal*0.12+self.__bonus
    
    #Setter methods
    def set_sal(self,x):
        self.__sal=x
    def set_bonus(self,x):
        self.__bonus=x
        
    #getter methods
    def get_bonus(self):
        return self.__bonus
    def get_sal(self):
        return self.__sal
        
class ContractEmp(Employee):
    def __init__(self,pname="",mob="",dt="",ds="",charg=1000,hrs=0):
        super().__init__("C",pname,mob,dt,ds)
        self.__hrs=hrs
        self.__charges=charg
    def __str__(self):
        return super().__str__()+f" Charges: {self.__charges}, Hours: {self.__hrs}"
    
    def calculatesal(self):
        return int(self.__hrs)*int(self.__charges)
    
    #Setter methods
    def set_hrs(self,x):
        self.__hrs=x
    def set_charg(self,x):
        self.__charges=x
        
    #getter methods
    def get_hrs(self):
        return self.__hrs
    def get_charg(self):
        return self.__charges 
 
        
if __name__=="__main__":
    s=SalariedEmp("Vikram","232323","AI","Developer",100000)
    print(s.get_pid())
    print(f"Salaried Employee:\n {s}")
    print(s.calculatesal())
    c=ContractEmp("Prada","988989","AI","Tester",20,8)
    print(f"Contracted Employee: \n{c}")
    print(c.calculatesal())
    
    
'''
    s=Person("Pradu","23232")
    s1=Person("Vikram","98989898")
    print(s)
    print(s1)
    s.set_pid(3)
    print(s)
    print(s.get_pid())
    Person.myf(45)
    '''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    