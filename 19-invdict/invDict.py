# Python function that takes a dictionary of word:meaning pairs as an input from the user and creates an inverted dictionary of the form meaning:list-of-words

def invert_dict(input_dict):
          inverted_dict = {}
          for word, meaning in input_dict.items():
                    if meaning not in inverted_dict:
                              inverted_dict[meaning] = [word]
                    else:
                              inverted_dict[meaning].append(word)

          return inverted_dict

input_dict = {}
num_pairs = int(input("Enter the number of word:meaning pairs: "))
for i in range(num_pairs):
          word = input("Enter a word: ")
          meaning = input("Enter the meaning: ")
          input_dict[word] = meaning

inverted_dict = invert_dict(input_dict)
for meaning, words in inverted_dict.items():
    print(meaning, ":", words)
