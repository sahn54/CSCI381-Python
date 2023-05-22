# Pickle
# The pickle function is a powerful tool that can be used to save and restore Python objects. It can be used to
# save objects to a file, send objects over a network, or store objects in a database.
# pickle is used to serialize and deserialize Python objects. Serialization is the process of converting an
# object into a sequence of bytes, while deserialization is the process of converting a sequence of bytes back
# into an object.

# --------------------------


# Serialization - is the process of converting an object into a sequence of bytes

# Deserialization - is the process of converting a sequence of bytes back into an object.

import pickle

list_of_numbers = [1, 2, 3, 4, 5]

# pickling - saving into sequence to bytes
with open("numbers.pkl", 'wb') as file:
    pickle.dump(list_of_numbers, file)

# unpickling - restoring back to object

with open("numbers.pkl", "rb") as file:
    restored_numbers = pickle.load(file)

print(restored_numbers)


# ------------------------------------------Example-----------------------------------------------


def signature(w):
    w1 = list(w)
    w1.sort()
    w1 = ''.join(w1)
    return w1


# create or load?
mode = input("Create or Load C or L: ")
print()
if mode.upper() == 'C':
    # create a "Scrabble Dictionary"
    d = {}
    print('Creating dictionary ... please wait.')
    f = open('C:/python32/six letter words.txt', 'r')
    print()
    sl = f.read()
    z = sl.split(' ')
    print()
    for w in z:
        sig = signature(w)
        if sig not in d:
            d[sig] = []
            d[sig].append(w)
        else:
            d[sig].append(w)
    f.close()
else:
    print('Unpickling dictionary ... please wait.')
    f = open('slwords', 'rb')
    d = pickle.load(f)  # this “unpickles”
    word = input("Please enter word: ")
    print()
    while word != 'done':
        if len(word) != 6:
            print("word not 6 chars")
        else:
            word = word.upper()
            word = signature(word)
            if word in d:
                print(d[word])
            else:
                print(word, ' not found.')
            word = input("Please enter word: ")
            print()
    f = open('slwords', 'wb')
    print('Pickling ... please wait.')
    pickle.dump(d, f)  # this pickles
    f.close()
