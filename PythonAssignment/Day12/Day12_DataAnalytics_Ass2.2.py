import numpy as np
dealor1=np.array([[12,23,34,45,56,67],[23,34,45,56,67,78],
                  [11,22,33,44,55,66],[13,24,35,46,57,68],
                  [12,23,34,44,55,66],[46,57,68,23,34,45],
                  [12,23,33,44,57,68],[12,34,13,44,68,78],
                  [111,222,333,444,555,666],[123,456,789,147,258,369]])
dealor2=np.array([[12,23,34,45,56,67],[23,34,45,56,67,78],
                  [111,222,333,444,555,666],[123,456,789,147,258,369],
                  [11,22,33,44,55,66],[13,24,35,46,57,68],
                  [12,23,33,44,57,68],[12,34,13,44,68,78],
                  [12,23,34,44,55,66],[46,57,68,23,34,45]
                  ])
print("YEarwise Data of Dealor 1:\n",dealor1)
print("YEarwise Data of Dealor 2:\n",dealor2)
print("\nyearwise sales of each item by both the dealers:\n",dealor1+dealor2)
print("\n yearwise sales of all items for dealer1:\n ",np.sum(dealor1,axis=1))
print("\n yearwise sales of all items for dealer2:\n ",np.sum(dealor2,axis=1))

year=int(input("enter a year(2001-2010): "))
print(f"\n sales of a year {year} for dealer1:\n ",np.sum(dealor1[year-2001]))
print(f"\n sales of a year {year} for dealer2:\n ",np.sum(dealor2[year-2001]))

print("\n sales of TV for dealer1:\n ",np.sum(dealor1[:,0]))
print("\n sales of freeze for dealer1:\n ",np.sum(dealor1[:,1]))
print("\n sales of TV for dealer2:\n ",np.sum(dealor2[:,0]))
print("\n sales of freeze for dealer2:\n ",np.sum(dealor2[:,1]))
