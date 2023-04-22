# Python function that takes a sentence as input from the user and calculates the frequency of each letter and use a variable of dictionary type to maintain the count

"""
def freqLetter():
          userInput = input("Enter a sentence: ")
          frequency = {}
          for letter in userInput:
                    if letter.isalpha():
                              letter = letter.lower()
                              frequency[letter] = frequency.get(letter, 0) + 1
          print(frequency)
          
freqLetter()
"""

# From the code taught in the class
my_sentence = []
sentence = input("Enter a sentence: ")
freq = {}
my_sentence = sentence.split()
print("The words in the sentence are: ", my_sentence)
for word in my_sentence:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

check_word = input("Enter a word to check its frequency in the sentence: ")
if check_word in freq:
    print(check_word, "has a frequency of", freq[check_word], "in the given sentence")
else:
    print(check_word, "not found in the sentence")

