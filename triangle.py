def triangle(n):

    for i in range(0, n):
        for j in range(0, n-i-1):
            print(" ", end="")

        for j in range(0, 2*i+1):
            print("*", end="")
        print()


n = input("enter the number of rows: ")

while not n.isnumeric():
    print("Wrong type. The number must be integer")
    n = input("enter the number of rows: ")

triangle(int(n))
