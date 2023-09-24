d={'a':45,'b':78}
def div(a,b):
    return a/b
try:
    a=int(input("Enter a No: "))
    b=int(input("Enter a No: "))
    c=div(a,b)
    #print(d['v'])  It throws Key Error Exception
except ValueError as ex:
    print("Wrong Value. ",ex)
except KeyError as ex:
    print("Key not Found. ",ex)
except Exception as e:
    print("Something Wrong",e)    
finally:
    print("This is final statement.")    