# Program to check for Alphabet, Digits, Special character, Whitespace

# ch = input("Enter a string: ")

# if ch>='a' and ch<='z':
#           print("Lower case")
# elif ch >='A' and ch<='Z':
#           print("Uppercase")
# elif ch >='0' and ch<='9':
#           print("Digits")
# elif ch==' ':
#           print("White Space")
# else:
#           print("Special Character")

#  This is the correct code
string = input("Enter a string: ")

for ch in string:
    if ch >= 'a' and ch <= 'z':
        print(ch, "is a Lowercase character")
    elif ch >= 'A' and ch <= 'Z':
        print(ch, "is an Uppercase character")
    elif ch >= '0' and ch <= '9':
        print(ch, "is a Digit")
    elif ch == ' ':
        print(ch, "is a Whitespace character")
    else:
        print(ch, "is a Special character")
