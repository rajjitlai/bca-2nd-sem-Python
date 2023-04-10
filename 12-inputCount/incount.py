# Python function that takes two strings as an input from the user and counts the number of matching characters in the given pair of strings.

def counter():
          userInput1 = input("Enter first string: ")
          userInput2 = input("Enter second string: ")
          count = 0
          for char in userInput1:
                    if char in userInput2:
                              count += 1
          return count

print("The number of matching characters is: ", counter())