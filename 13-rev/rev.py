# Python function that takes a string as an input from the user and displays its reverse. 

def revString():
          userInput = input("Enter a string: ")
          
          revStr = userInput[::-1]
          
          print("The reversed string is ", revStr)
          
revString()