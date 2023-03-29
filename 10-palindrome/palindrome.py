# Python function that takes a number as an input and determine whether it is prime or not

userInput = input("Enter a number: ")

def palindrome():
          check = userInput[::-1]
          
          if userInput == check:
                    print(f"The number {userInput} is palindrome")
          else:
                    print(f"The number {userInput} is not palindrome")

palindrome()
          