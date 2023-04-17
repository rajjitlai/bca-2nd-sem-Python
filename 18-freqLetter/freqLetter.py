# Python function that takes a sentence as input from the user and calculates the frequency of each letter and use a variable of dictionary type to maintain the count


def freqLetter():
          userInput = input("Enter a sentence: ")
          frequency = {}
          for letter in userInput:
                    if letter.isalpha():
                              letter = letter.lower()
                              frequency[letter] = frequency.get(letter, 0) + 1
          print(frequency)
          
freqLetter()
