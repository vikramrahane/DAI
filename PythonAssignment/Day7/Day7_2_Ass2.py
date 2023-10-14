people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
print("No of Students: ",len(people))
people['Lisa']='Red'
print("Changed Lisa’s favourite colour to Red\n",people)
people.pop('Jenny')
print("Removed 'Jenny' and her favourite colour \n",people)

people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
for i in sorted(list(people.keys())):
    print(i,":",people[i])