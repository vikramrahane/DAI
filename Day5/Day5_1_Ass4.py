cities=[]
loc=[]
c=input("Enter City Name: ")
cities.append(c)
while True:
    ch=input("Do you want to continue(y): ")
    if ch=='y':
        c=input("Enter City Name: ")
        cities.append(c)
    else:
        break
c=input("Enter Location Name: ")
loc.append(c)
while True:
    ch=input("Do you want to continue(y): ")
    if ch=='y':
        c=input("Enter Location Name: ")
        loc.append(c)
    else:
        break
for c,l in zip(cities,loc):
    print(f"{c} --> {l}")
