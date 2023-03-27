# Program to find the fibonacci sequence 

user_input = int(input("Enter a number: "))
def fibonacci(n):
    a, b = 0, 1

    print(a, b, end=" ")

    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c

print(f"The fibonacci series of {user_input} is: ")
fibonacci(user_input)

