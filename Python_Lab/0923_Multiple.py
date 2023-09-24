class A:
    def __init__(self,a1=0,a2=0,**kwarg):
        print("In A Constructor.",kwarg)
        super().__init__(**kwarg)
        self.__a1=a1
        self.__a2=a2
        
    def __str__(self):
        return f" a1: {self.__a1} a2: {self.__a2}"
    
class B:
    def __init__(self,b1=0,**kwarg):
        print("In B Constructor.",kwarg)
        super().__init__(**kwarg)
        self.__b1=b1
        
    def __str__(self):
        return super().__str__()+f" b1: {self.__b1}"
    
class C(B,A):
    def __init__(self,c1=0,c2=0,**kwarg):
        print("In C Constructor.",kwarg)
        super().__init__(**kwarg)
        self.__c1=c1
        self.__c2=c2
        
    def __str__(self):
        return super().__str__()+f" c1: {self.__c1} c2: {self.__c2}"
    
c=C(a1=8,a2=67,b1=90,c1=45,c2=66)
print(c)
print(C.mro())