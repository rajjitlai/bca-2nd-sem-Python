# Program to print Floyd's Triangle
rows = int(input("Enter the number of rows: "))

num = 1
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1
