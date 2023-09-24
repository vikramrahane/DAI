x=5
y=22
print(x,bin(x))
print(y,bin(y))

n=x<<5
n1=n|y
print(n1,bin(n1))

y1=n1&int(0b11111)
print(y1,bin(y1))

x1=n1>>5
print(x1,bin(x1))
