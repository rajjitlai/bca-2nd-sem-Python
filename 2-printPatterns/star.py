# Python program to print the pattern
"""
                  *
            *     *     *
      *     *     *     *     *
"""

def printPattern():
      # rows = int(input("Enter the number of rows: "))   
      rows = 4
      k = 2 * rows - 2
      
      for i in range(0, rows):
            for j in range(0, k):
                  print(end=' ')
            k = k - 2
            for j in range(0, 2 * i - 1):
                  print("*", end=" ")
            print(" ")

printPattern()