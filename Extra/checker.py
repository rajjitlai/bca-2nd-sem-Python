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
# string = input("Enter a string: ")

# for ch in string:
#     if ch >= 'a' and ch <= 'z':
#         print(ch, "is a Lowercase character")
#     elif ch >= 'A' and ch <= 'Z':
#         print(ch, "is an Uppercase character")
#     elif ch >= '0' and ch <= '9':
#         print(ch, "is a Digit")
#     elif ch == ' ':
#         print(ch, "is a Whitespace character")
#     else:
#         print(ch, "is a Special character")

#  added the count function
string = input("Enter a string: ")

count_alpha = 0
count_num = 0
count_vowels = 0
count_consonants = 0
count_space = 0

for ch in string:
    if ch >= 'a' and ch <= 'z':
        count_alpha += 1
        if ch in ['a', 'e', 'i', 'o', 'u']:
            count_vowels += 1
        else:
            count_consonants += 1
        print(ch, "is a Lowercase character")
    elif ch >= 'A' and ch <= 'Z':
        count_alpha += 1
        if ch in ['A', 'E', 'I', 'O', 'U']:
            count_vowels += 1
        else:
            count_consonants += 1
        print(ch, "is an Uppercase character")
    elif ch >= '0' and ch <= '9':
        count_num += 1
        print(ch, "is a Digit")
    elif ch == ' ':
        count_space += 1
        print(ch, "is a Whitespace character")
    else:
        print(ch, "is a Special character")
        
print("Number of alphabets:", count_alpha)
print("Number of digits:", count_num)
print("Number of vowels:", count_vowels)
print("Number of consonants:", count_consonants)
print("Number of whitespace characters:", count_space)


