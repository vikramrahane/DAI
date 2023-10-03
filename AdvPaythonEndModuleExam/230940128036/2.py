cricketer_profile={}
# Dictionary elements taken from user
name=input("Enter the name: ")
age=int(input("Enter the age: "))

# list of favourite players taken from user
favourite_player=[]
ch='y'
while ch=='y':        
    fav=input("Enter the Favourite Player: ")
    favourite_player.append(fav)
    ch=input("Do you want to add more Favourite Player?(y/n) ")
    
# list of countries played taken from user
countries=[]
ch='y'
while ch=='y':        
    c=input("Enter the Country Name: ")
    countries.append(c)
    ch=input("Do you want to add more Countries?(y/n) ")

cricketer_profile['name']=name
cricketer_profile['age']=age
cricketer_profile['favourite_player']=favourite_player
cricketer_profile['countries_played']=countries
print("\ncricketer_profile= \n{")

for k,v in cricketer_profile.items():
    print(f"{k}:{v}")
print("}")