# Python program to find the sum of the series 1-x2/2!+x4/4!-x6/6!+...+xn/n!

n = int(input("Enter the term: "))
x = int(input("Enter value of x: "))
k = 2
sum = 1
sign = 1
m = 2

for i in range(1, x+1):
          fact = 1
          for j in range(1, m + 1):
                    fact = fact * j
                    sign = -sign
                    sum += sum + ((x**k)/fact)*sign
                    k += 2
                    m += 2
print ("Sum = ", sum)