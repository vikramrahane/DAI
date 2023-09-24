set1={10,20,30,40,50}
set2={30,40,50,60,70}
print("Set1: ",set1,"\n","set2: ",set2)
print("Intersection : ",set1.intersection(set2)) #Set1&set2
print("Union : ",set1.union(set2)) #set1|set2
print("Difference : ",set1.difference(set2))  #set1-set2
print("Symmetric Difference: ",set1.symmetric_difference(set2)) #set1^set2
set1.difference_update(set2)
print("Difference Update: ",set1)
set1={10,20,30,40,50}
set2={30,40,50,60,70}
print("Set1: ",set1,"\n","set2: ",set2)
set1.symmetric_difference_update(set2)
print("Symmetric difference Update",set1)
