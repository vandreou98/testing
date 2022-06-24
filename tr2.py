def triangle(n):

    for i in range(0, n):
        print(" "*(n-i-1) + "*"*(2*i+1))


n = input("enter the number of rows: ")

while not n.isnumeric():
    print("Wrong type. The number must be integer")
    n = input("enter the number of rows: ")

triangle(int(n))
