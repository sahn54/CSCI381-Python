my_list = []
with open("Class_11/words.txt")as file:
    # new_file = file.read()  # gets everything into a string
    # print(new_file)

    # new_file = file.readlines()  # gets everything in to a list
    # list_words = "".join(new_file).splitlines()
    for line in file:
        word = line.strip()
        signature = "".join(sorted(word))  # sorted changes strings to an list
        my_list.append((signature, word))

# we need to sort my_list again
sorted_words = sorted(my_list, key=lambda x: x[0])


# now we put all of the sorted words into a dictionary where the signature is the key and word is the value
my_dict = {}
for letter, word in sorted_words:
    # my_scrabble_list is for all list that has the same letters for each key example: NOT: [NOT, TON] , if the word does not match give a blank
    my_scrabble_list = my_dict.get(letter, [])
    my_scrabble_list.append(word)
    my_dict[letter] = my_scrabble_list

to_continue = True
while to_continue:
    user_input = input("Enter a letter:").upper()
    if user_input == "GG":
        to_continue = False
        continue

    sorted_user_letters = "".join(sorted(user_input))

    user_word_list = my_dict.get(sorted_user_letters, "not words are found")

    print(user_word_list)
