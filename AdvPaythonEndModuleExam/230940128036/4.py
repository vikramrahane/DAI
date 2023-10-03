try:
    with open("quot.txt") as fh:
        for line in fh:
            print(line)
except FileNotFoundError as e:
    print("File Not Found ",e)
except Exception as e:
    print(e)