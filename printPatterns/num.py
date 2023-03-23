# Python program to print the pattern
"""
          1
          2 3 2
          3 4 5 4 3
          4 5 6 7 6 5 4
          5 6 7 8 9 8 7 6 5
"""

# function definition
def patternPrint(n):
          for i in range(1, n + 1):
                    for j in range(1, i + 1):
                              print(i + j - 1, end=" ")
                    for k in range(i - 1, 0, -1):
                              print(i + k - 1, end=" ")
                    print("")

# function call
patternPrint(5)
