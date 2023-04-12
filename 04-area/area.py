# Program to find the area of triangle using Heron's Formula
import math

def triArea():
    # we get the input from the user
    side1 = float(input("Enter the length of side 1: "))
    side2 = float(input("Enter the length of side 2: "))
    side3 = float(input("Enter the length of side 3: "))

    # assert that the sum of any two sides is greater than the third side
    assert side1 + side2 > side3, "Invalid triangle sides"
    assert side2 + side3 > side1, "Invalid triangle sides"
    assert side1 + side3 > side2, "Invalid triangle sides"

    # calculate the semi-perimeter of the triangle
    s = (side1 + side2 + side3) / 2

    # calculate the area of the triangle using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print("Area of the triangle is: ", area)

triArea()