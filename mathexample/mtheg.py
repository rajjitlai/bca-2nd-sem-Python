# Python program to illustrate the various functions of the “Math” module

import math

# Calculate the square root of a number
num = 25
sqrt = math.sqrt(num)
print("Square root of", num, "is", sqrt)

# Calculate the factorial of a number
num = 5
fact = math.factorial(num)
print("Factorial of", num, "is", fact)

# Convert degrees to radians
deg = 45
rad = math.radians(deg)
print(deg, "degrees is equal to", rad, "radians")

# Calculate the sine of an angle in radians
angle = math.pi/4
sin = math.sin(angle)
print("Sine of", angle, "radians is", sin)

# Calculate the cosine of an angle in radians
cos = math.cos(angle)
print("Cosine of", angle, "radians is", cos)

# Calculate the logarithm base 10 of a number
num = 1000
log10 = math.log10(num)
print("Logarithm base 10 of", num, "is", log10)
