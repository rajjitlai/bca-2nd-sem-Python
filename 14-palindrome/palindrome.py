# Python function that checks if the user input is palindrome or not

userInput = input("Enter a number: ")

def palindrome():
          check = userInput[::-1]
          
          if userInput == check:
                    print(f"The number {userInput} is palindrome")
          else:
                    print(f"The number {userInput} is not palindrome")

palindrome()
          