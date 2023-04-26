# mystring = "Hello World"

# str.count(sub[, start[, end]])
# print(mystring.count('e'))
# print(mystring.find('e'))
# print(mystring.join('k'))
# print(mystring.replace('e', 'k'))
# print(mystring.split('e'))


# str.count(sub[, start[, end]])

# str.find(sub[, start[, end]])

# str.join(iterable)

# str.replace(old, new[, count])

# str.split([sep[, maxsplit]])


# Write a function that reverses a string. Remember, a string is not mutable! Do it two ways.
def reverse_string(str):
    newString = ""
    for i in range(len(str)):
        newString = str[i] + newString
    print(newString)


def reverse_list_toList(thelist):
    newlist = []
    theString = ""
    for i in thelist:
        newlist.append(i)
        newlist.reverse()
    for j in newlist:
        theString += j
    print(theString)


def reverse_list_toString(thelist):
    # Create a new list with the same elements as the input list
    newlist = thelist[:]
    # Reverse the elements in the new list
    newlist.reverse()
    # Join the elements in the new list into a string
    theString = ''.join(newlist)
    # Print the resulting string
    print(theString)


# Example usage
mylist = ['h', 'e', 'l', 'l', 'o']
mylist_2 = ['w', 'o', 'r', 'l', 'd']
reverse_list_toString(mylist)  # Output: "olleh"


reverse_string("mystring")
reverse_list_toList(['a', 'b', 'c'])
reverse_list_toString(mylist_2)


# Write a function one_upper(s) which returns True if exactly one character in string s is capitalized, and
# False otherwise. You can assume that the string s contains only alphabetic characters and no blanks. You
# might want to consider other string functions from the documentation.

def one_upper(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
        else:
            return False


print(one_upper("Queens College"))
