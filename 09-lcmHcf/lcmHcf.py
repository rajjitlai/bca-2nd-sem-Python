# Python function that takes two numbers as input parameters and returns their least common multiple and highest common factor

userInput1 = int(input("Enter the first number: "))
userInput2 = int(input("Enter the second number: "))

def lcmHcf():
    big = max(userInput1, userInput2)
    small = min(userInput1, userInput2)
    
    while small != 0:
        temp = small
        small = big % small
        big = temp
    hcf = big
    
    lcm = (userInput1 * userInput2) // hcf
    
    print(f"The lcm of {userInput1} and {userInput2} is: ", lcm)
    print(f"The hcf of {userInput1} and {userInput2} is: ", hcf)
    
lcmHcf()
