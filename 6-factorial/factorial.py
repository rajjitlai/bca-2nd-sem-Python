# Program to find the factorial of a given number

user_input = int(input("Enter a number: "))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {user_input} is ", fact)

factorial(user_input)
