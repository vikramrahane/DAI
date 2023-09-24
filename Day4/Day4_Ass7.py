def sum(x):
    if x==1:
        return 1
    else:
        return x+sum(x-1)
def main():
    print(sum(10))
main()
