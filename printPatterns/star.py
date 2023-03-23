# Python program to print the pattern
"""
          *
          * * *
          * * * * *
          * * *
          *
"""

# function definition
def patternPrint(n):
              for i in range(n):
                    if i < n //2 + 1:
                              for j in range(i*2 + 1):
                                        print("*", end=" ")
                    else:
                              for j in range((n - i)*2 - 1):
                                        print("*", end=" ")
                    print("")

# function call
patternPrint(5)



# alternate
"""
print("*")
print("* * *")
print("* * * * *")
print("* * *")
print("*")
"""