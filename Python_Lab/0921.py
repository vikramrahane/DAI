class student:
    #constructor
    def __init__(self,i=0,pn="",mob=""):
        print("In student constructor. ")
        self.__pid=i
        self.__pname=pn
        self.__mobno=mob
    def __str__(self):
        return f"ID: {self.__pid} NAme: {self.__pname} Mobile: {self.__mobno}"
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
if __name__=="__main__":
    s=student(1,"Pradu","23232")
    s1=student(2,"Vikram","98989898")
    print(s)
    print(s1)
    s.set_pid(3)
    print(s)
    print(s.get_pid())