#Print name n times using recursion
def print_name(n):
    if n<1:
        return
    print(n,". Prithviraj")
    print_name(n-1)
    pass


n = int(input("Enter number: "))
print_name(n)

