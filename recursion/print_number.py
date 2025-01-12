def print_number(n, count):
    if count>n:
        return
    print(count)
    print_number(n, count-1)
    pass

n = int(input("Enter number"))
count = 1
print_number(n, count)