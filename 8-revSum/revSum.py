#  Python function that takes a number with two or more digits as an input and finds its reverse and computes the sum of its digits

user_input = int(input("Enter a number with two or more digits: "))

def revSum():
          rev = str(user_input)[::-1]
          sum = 0
          for n in rev:
                    sum += int(n)
                    # sum = sum + in(n)
                    
          print("The reversed number is: ", rev)
          print("The sum of the reversed number is: ", sum)

revSum()