# Write a Python function called max_word_length that takes a string as input
# and returns the length of the longest word in the string.
# Use a list comprehension to generate a list of the lengths of all the words in the string.
import timeit
from functools import wraps
import copy


def max_word_length(s):
    return [len(word.strip(',')) for word in s.strip(',').split()]
# just add max in to the list comprehension


string_line = "Hello this is me, Mario!"
print(max_word_length(string_line))

# Write a Python function called dict_comprehension that takes a list of strings as input
# and returns a dictionary where the keys are the strings and the values are the lengths of the strings.
# Use a dictionary comprehension to generate the dictionary.


def dict_comprehension(list_str):
    return {word: len(word) for word in list_str}


my_list = ["Mary", "James", "John", "Judah", "Matthew"]
print(dict_comprehension(my_list))
# Write a Python function called file_filter that takes a file name and a string as input,
# and returns a list of the lines in the file that contain the given string.
# Use a with statement to ensure that the file is properly closed after reading.


def file_filter(file_name, str_input):
    with open(file_name) as file:
        my_list_2 = []
        for line in file:
            if str_input in line:
                my_list_2.append(line)
        return my_list_2


print(file_filter("final/Topics.txt", "and"))


# Write a Python function called deep_copy that takes a list of lists as input
# and returns a new list of lists that is a deep copy of the input.
# That is, modifying the elements of the new list will not affect the elements of the original list.


def deep_copy(list_of_list):
    copied_list = copy.deepcopy(list_of_list)
    copied_list[1][0] = "Hello"
    return copied_list


list_2D = [["lion", "monkey", 'cat', 'dog'], [
    'house', 'ship', 'car'], ['LA', 'NY', 'MO']]

print(deep_copy(list_2D))
print(list_2D)

# Write a Python generator function called triangle_numbers that generates
# the sequence of triangle numbers, starting with 1 and continuing indefinitely.
# A triangle number is the sum of all positive integers up to a given number.
# For example, the first few values generated should be 1, 3, 6, 10, 15, ...


def triangle_numbers(num):
    value = 1
    adding_value = 2
    while num > 0:
        yield value
        value += adding_value
        adding_value += 1
        num -= 1


t_n = triangle_numbers(10)
for i in t_n:
    print(i)

# Write a Python function called log that takes a message as input
# and writes it to a file called log.txt, along with a timestamp.
# Use a decorator to implement this functionality.


def decorator_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Program starts: {func.__name__} ")
        starting_time = timeit.timeit()
        print(f"Program processing: {func.__name__} ")
        result = func(*args, **kwargs)
        ending_time = timeit.timeit()
        timestamp = ending_time - starting_time
        print(f"Program ends: {func.__name__} ")
        return result, timestamp
    return wrapper


@decorator_log
def log(file_name, input_message):
    with open(file_name, 'w') as log_file:
        log_file.write(input_message)
    return input_message


my_log = log("final/log.txt", "Adding text")
print(my_log)


# Write a Python function called unpack_tuple that takes a tuple of arbitrary length as input
# and returns a new tuple where the first and last elements of the input tuple are swapped.
# If the input tuple has length 1, the function should return the input tuple unchanged.
# If the input tuple has length 0, the function should return an empty tuple.
# For example, if the input tuple is (1, 2, 3, 4, 5), the output should be (5, 2, 3, 4, 1).
def unpack_tuple(check_tuple):
    if len(check_tuple) < 1:
        return ()
    elif len(check_tuple) == 1:
        return check_tuple
    else:
        swap_list = [i for i in list(check_tuple)[::-1]]
        return tuple(swap_list)


my_tuple = (1, 2, 3, 4, 5)
print(unpack_tuple(my_tuple))

# def unpack_tuple(check_tuple):
#     if len(check_tuple) < 1:
#         return ()
#     elif len(check_tuple) == 1:
#         return check_tuple
#     else:
#         first, *middle, last = check_tuple
#         return (last, *middle, first)

# my_tuple = (1, 2, 3, 4, 5)
# print(unpack_tuple(my_tuple))


# Write a Python function called word_freq that takes a string as input
# and returns a dictionary that maps each word in the string to the number of times it appears.
# You should ignore case and punctuation, and treat all whitespace as equivalent.
# Use a regular expression to split the string into words.


def word_freq(str_input):
    my_dict = {word.strip('.').lower(): str_input.count(word.strip(".").lower())+1
               for word in str_input.split()}
    return my_dict


my_str_input = "Joe waited for the train. The train was late. Mary and Samantha took the bus."
print(word_freq(my_str_input))
