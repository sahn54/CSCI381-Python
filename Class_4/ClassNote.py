# Class notes (page 72)
# Learn more about for loops

# the loop is iterable
a = range(5)  # a = 0, 1, 2, 3, 4
b = range(1, 8)  # b = 1, 2, 3, 4, 5, 6, 7
c = range(0, 14, 3)  # c = 0, 3, 6, 9, 12
d = range(8, 1, -1)  # d = 8, 7, 6, 5, 4, 3, 2

# The object created by range() computes the values it represents on demand when lookups are
# requested. Thus, it’s efficient to use even with a large range of numbers.
# The for statement is not limited to sequences of integers. It can be used to iterate over many
# kinds of objects including strings, lists, dictionaries, and files. Here’s an example:
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(f'2 to the {n} power is {2**n}')

# In this example, the variable n will be assigned successive items from the list [1, 2, 3, 4, ..., 9] on
# each iteration.

message = 'Hello World'
# Print out the individual characters in message
for c in message:
    print(c)


names = ['Dave', 'Mark', 'Ann', 'Phil']
# Print out the members of a list
for name in names:
    print(name)

# Hash Map = Dictionary
