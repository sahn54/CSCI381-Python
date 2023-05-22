# Write a Python function called even_numbers that takes a list of integers
# as input and returns a new list containing only the even numbers
# from the input list. Use list comprehension to generate the new list.
import pickle as p
from functools import wraps
import time
import copy


def even_numbers(list_int):

    new_list = [number for number in list_int if number % 2 == 0]
    return new_list


k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(k))


# Write a Python function called reverse_dict that takes a dictionary as input
# and returns a new dictionary with the keys and values swapped.
# For example, if the input dictionary is {"a": 1, "b": 2, "c": 3}, the output should be {1: "a", 2: "b", 3: "c}".
def reverse_dict(dict_input):
    new_dict = {dict_input[key]:  key for key in dict_input}
    return new_dict


dict_k = {"a": 1, "b": 2, "c": 3}
print(reverse_dict(dict_k))

# Write a Python function called write_to_file that takes a list of strings and a file name as input
# and writes each string to a new line in the specified file.
# Use a with statement to ensure that the file is properly closed after writing.


def write_to_file(list_str, file):
    for word in list_str:
        file.write(str(word))
        file.write(" ")


# use k as our list:
with open("final/file_1.txt", "w") as file:
    write_to_file(k, file)

# Write a Python function called deep_copy that takes a list of lists as input
# and returns a new list of lists that is a deep copy of the input.
# That is, modifying the elements of the new list should not affect the elements of the original list.


def deep_copy(list_of_lists):
    new_list_of_lists = copy.deepcopy(list_of_lists)
    new_list_of_lists[0][0] = 5
    return f"Original list: {list_of_lists}\nModified list: {new_list_of_lists}"


og_list = [[1, 2, 3, 4], 5, 6, 7]
print(deep_copy(og_list))


# Write a Python generator function called factorials that generates the factorial sequence,
# starting with 1! and continuing indefinitely.
# For example, the first few values generated should be 1, 2, 6, 24, 120, ...
def factorials():
    value = 1
    result = 1
    while True:
        result *= value
        value += 1
        yield result


my_factorial = factorials()
for i in range(20):
    print(next(my_factorial))

# Write a Python function called timer that takes a function as input
# and returns a new function that behaves the same as the input function,
# but also prints the time taken for the function to execute.
# Use a decorator to implement this functionality.


def timer(func):
    @wraps(func)  # type: ignore
    def wrapper(*args, **kwargs):
        print(f"Opening function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Ending function: {func.__name__} ")
        return result
    return wrapper


@timer
def add(a, b):
    return a + b


add = timer(add)
start_time = time.time()
result = add(4, 5)
end_time = time.time()

duration = end_time - start_time

print(f"Result: {result}")
print(f"Duration: {duration}")


# REVIST
# Write a Python program that reads a dictionary from a file,
# where each line of the file contains a key-value pair separated by a colon.
# The program should then prompt the user for a key and
# output the corresponding value if it exists in the dictionary.
# Use the pickle module to load the dictionary from the file.

with open("final/file_1.txt") as read_file:
    string_file = read_file.read()
    my_list = string_file.strip(' ').split()
    print(my_list)
    dict_num = {i: my_list[i] for i in range(len(my_list))}

p.dump(dict_num, open("final/file_2.txt", "wb"))

new_dict = p.load(open("final/file_2.txt", "rb"))

print(new_dict)


# def double_1(numlist):
#     n = [f"Twice {i} is {i * 2}." for i in numlist]
#     return "\n".join(n)


# m = double_1([3, 7, 4])
# print(m)


# def printWords(wordlist):
#     return " ".join(wordlist)


# print(printWords(['he', 'is', 'his', 'hero']))


# def problem_14(num_list, lowVal, highVal):
#     return [print(num, sep="", end=" ")
#             for num in num_list if lowVal <= num <= highVal]


# def problem_15(num_list, lowVal, highVal):
#     return [num for num in num_list if lowVal <= num <= highVal]


# problem_14([2, 5, 1, 7, 4], 2, 6)
# print()
# print(problem_15([2, 5, 1, 7, 4], 2, 6))
# print()  # get rid of %


# More file exercises and generators
# Unpacking
