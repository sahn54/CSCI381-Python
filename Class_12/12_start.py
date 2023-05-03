# Pickle
# The pickle function is a powerful tool that can be used to save and restore Python objects. It can be used to
# save objects to a file, send objects over a network, or store objects in a database.
# pickle is used to serialize and deserialize Python objects. Serialization is the process of converting an
# object into a sequence of bytes, while deserialization is the process of converting a sequence of bytes back
# into an object.

# --------------------------


# Serialization - is the process of converting an
# object into a sequence of bytes

# Deserialization

# Write a program that reads a text file and creates a simplified version of in inverted index.
invertedDict = dict()
line_list = []
with open("Class_12/speech.txt") as file:
    for line in file:
        line_num = 1
        line_word = line.strip("\n")
        print(f"Line {line_num}: {line}")
        line_list.append(line_word)


t_List = [4, 4, 4, 6, 6, 8, 8, 8, 8]


def squish(x):
    # x is a list
    new_list = [(i, x.count(i)) for i in sorted(set(x))]
    return new_list


# print(squish(t_List))

# Your program will create a dictionary, invertedDict, whose key is the word in the file and whose value is a
# list of integers representing the line numbers in the file where word is found.

# What if the word is found k times on some line?
# Then the line number will appear k times in the list.
# For example, say the word “cat” appears 3 times on line 4, 2 times on line 6, and 4 time on line 8, then
# the dictionary entry for cat will be:
# invertedDict[“cat”] ->[4,4,4,6,6,8,8,8,8].
