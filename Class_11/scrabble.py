# TASK 1: Create the file
word_list = []
with open("Class_11/words.txt") as file:
    for line in file:
        word = line.strip()
        # TASK 2: Create a list of tuples (signature,word), where for each word in word list its “signature” is the “word”
        # sorted by its letters. So, for example, if we were dealing with four letter words, the signature of “STOP” is
        # “OPST”. Notice that this is also the signature of POTS and TOPS
        signature = "".join(sorted(word))
        word_list.append((signature, word))
# TASK 3: Sort the list of tuples created in step 2 by the signature.
sorted_words = sorted(word_list, key=lambda x: x[0])

# TASK 4: Go through the list created in step 3 and create a Python dictionary where for each entry, the key is the
# signature and the associated value is a list of all words with the same signature.

# so we want a dictionary where the key is the letters in alphabetical order
# and the value is a list of all words that can be formed with those letters
# example: the key OPTS should have [STOP, POTS, TOPS, etc]

word_dict = dict()
for letters, word in sorted_words:
    # if the list exists, return it. if not, return an empty list that we can work with
    word_list = word_dict.get(letters, [])
    word_list.append(word)
    word_dict[letters] = word_list

# make sure it works
# for letters in word_dict:
#   if len(word_dict[letters]) > 3:
#     print(letters)
#     print(word_dict[letters])

# TASK 5: Finally, in a loop, ask the user for the six letters that they want to look up, and your program will return
# all valid six-letter Scrabble words matching the request.

user_letters = input("Enter your letters: ")

# no guarantee that the letters are sorted from the user!
# we get the strings -> sorted into a list -> join them back to a string again.
sorted_user_letters = "".join(sorted(user_letters.upper()))

# word_dict[sorted_user_letters] will give key error if the key doesn't exist
# get on the other hand will have a default word.
user_word_list = word_dict.get(sorted_user_letters, "no words available")

print(user_word_list)
