class Player:
    cnt=0
    def __init__(self,pname="",special="",charg=1000,tname=""):
        Player.cnt=Player.cnt+1
        self.__pid=Player.cnt
        self.__pname=pname
        self.__special=special
        self.__charges=charg
        self.__tname=tname
        
    def __str__(self):
        return f"ID: {self.__pid} Name: {self.__pname} Specialization: {self.__special} Charges: {self.__charges} Team Name: {self.__tname}"

    #Setter Methods
    def set_pid(self,pid):
        self.__pid=pid
    def set_pname(self,pname):
        self.__pname=pname
    def set_special(self,special):
        self.__special=special
    def set_charges(self,charges):
        self.__charges=charges
    def set_tname(self,tname):
        self.__tname=tname    
        
    #Getter Methods
    def get_pid(self):
        return self.__pid
    def get_pname(self):
        return self.__pname
    def get_special(self):
        return self.__special
    def get_charges(self):
        return self.__charges
    def get_tname(self):
        return self.__tname
