import numpy as np
set1={10,20,30,40,50}
set2={30,40,50,60,70}
sum=0
for s in set1:
    sum=sum+s
avg=sum/len(set1)
set1.update(filter(lambda x:x>avg,set2))
print(set1)