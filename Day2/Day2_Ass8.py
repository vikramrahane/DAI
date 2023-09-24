n=int(input("Enter a No of terms: "))
a=9
s=9
print(f"{a}",end="")
for i in range(n-1):
    a=(a*10)+9
    s=s+a
    print(f"+{a}",end="")
print(f"\n sum of Series for {n} terms : {s}")

