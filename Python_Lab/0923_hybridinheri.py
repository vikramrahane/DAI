class A:
    def __init__(self,a1=0,a2=0):
        print("In A Constructor.",a1,a2)
        self.__a1=a1
        self.__a2=a2
        
    def __str__(self):
        return f" a1: {self.__a1} a2: {self.__a2}"

class B(A):
    def __init__(self,b1=0,**kwargs):
        print("In B Constructor.",kwargs)
        super().__init__(**kwargs)
        self.__b1=b1        
        
    def __str__(self):
        return super().__str__()+f" b1: {self.__b1}"
    
class C(A):
    def __init__(self,c1=0,c2=0,**kwargs):
        print("In C Constructor.",kwargs)
        super().__init__(**kwargs)
        self.__c1=c1
        self.__c2=c2        
        
    def __str__(self):
        return super().__str__()+f" c1: {self.__c1} c2: {self.__c2}"
    
class D(B,C):
    def __init__(self,d1=0,d2=0,**kwargs):
        print("In D Constructor.",kwargs)
        super().__init__(**kwargs)
        self.__d1=d1
        self.__d2=d2        
        
    def __str__(self):
        return super().__str__()+f" d1: {self.__d1} d2: {self.__d2}"

d=D(a1=12,a2=22,b1=23,c1=24,c2=25,d1=26,d2=27)
print(d)
print(D.mro())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    