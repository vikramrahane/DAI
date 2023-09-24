def fact(n):
    if n>0:
        f=1
        for i in range(1,n+1):
            f=f*i
    else:
        print(f"{n} should be greater than 0")
    return f
def main():
    for i in range(1,21):
        print(f"{i} {fact(i)}")

main()
