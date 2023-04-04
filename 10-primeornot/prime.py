# Python function that takes a number as an input and determine whether it is prime or not.
import math

def is_prime(n):
    if n < 2:
        print(n, "is not a prime number")
    elif n == 2:
        print(n, "is a prime number")
    elif n % 2 == 0:
        print(n, "is not a prime number")
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                print(n, "is not a prime number")
                break
        else:
            print(n, "is a prime number")

userInput = int(input("Enter a number: "))            
is_prime(userInput)
