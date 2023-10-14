s1="America"
s2="Japan"
def mix_str(x,y):
    return x[0]+y[0]+x[len(s1)//2]+y[len(s2)//2]+x[-1]+y[-1]
print(mix_str(s1,s2))
