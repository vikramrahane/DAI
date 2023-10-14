class Friend:
    cnt=0
    def __init__(self,fname="",lastname="",hobbies=[],mobno="",email="",bdate="",address="" ):
        Friend.cnt=Friend.cnt+1
        self.__fid=Friend.cnt
        self.__fname=fname
        self.__lname=lastname
        self.__hobbies=hobbies
        self.__mobno=mobno
        self.__email=email
        self.__bdate=bdate
        self.__address=address
        
    def __str__(self):
        return f"fid:{self.__fid} Fname:{self.__fname} lastname={self.__lname} hobbies:{self.__hobbies} Mobile NO:{self.__mobno} email:{self.__email} bdate:{self.__bdate} address:{self.__address}"
    
    #Setter methods
    def set_id(self,x):
        self.__fid=x
    def set_fname(self,x):
        self.__fname=x
    def set_lname(self,x):
        self.__lname=x
    def set_hobby(self,lst):
        self.__hobbies=lst
    def set_mobno(self,x):
        self.__mobno=x
    def set_email(self,x):
        self.__email=x
    def set_bdate(self,x):
        self.__bdate=x
    def set_address(self,x):
        self.__address=x
        
    def get_id(self):
        return self.__fid
    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_hobby(self):
        return self.__hobbies
    def get_mobno(self):
        return self.__mobno
    def get_email(self):
        return self.__email
    def get_bdate(self):
        return self.__bdate
    def get_address(self):
        return self.__address