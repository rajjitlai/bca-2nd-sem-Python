# Python program to find the sum of the series 1 + x2 /2! + x4 /4! + x6 /6! + … xn /n!

n = int(input("Enter the term: "))
x = int(input("Enter value of x: "))
k = 2
sum = 1

for i in range(2, n+1, 2):
          fact = 1
          for j in range(1, i+1):
                    fact *= j
          sum += ((x**i)/fact)

print("Sum = ", sum)


