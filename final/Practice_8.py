# Write a Python function called swap_values that takes two variables a and b as input
# and swaps their values using tuple unpacking.
# The function should return the updated values of a and b.
from itertools import permutations
import copy
import time
from functools import wraps
import pickle


def swap_values(a, b):
    a, b = b, a
    return a, b


print(swap_values(1, 2))


# Consider the following list: my_list = [1, 2, 3, 4, 5].
# Write a single line of code using iterable unpacking to assign the first three values
# of the list to variables a, b, and c respectively.
the_list = [1, 2, 3, 4, 5]
a, b, c = the_list[:3]
print(a, b, c)


# Write a Python function called average_scores that takes a list of tuples as input.
# Each tuple contains a student's name and their scores on three exams.
# The function should calculate the average score for each student
# and return a dictionary that maps each student's name to their average score.
# For example, if the input is
# [('Alice', 85, 90, 92), ('Bob', 78, 89, 91)], the output should be {'Alice': 89, 'Bob': 86}.
def average_scores(list_tuple):
    # (student_name, score_1 , score_2, score_3)
    dict_name_grade = {}
    for tuple_num in list_tuple:
        a, b, c = tuple_num[1:]
        average = (a+b+c) // 3
        dict_name_grade[tuple_num[0]] = average
    return dict_name_grade


working_list = [('Alice', 85, 90, 92), ('Bob', 78, 89, 91)]
print(average_scores(working_list))

# Consider the following tuple: my_tuple = (1, 2, 3, 4, 5).
# Write a single line of code using extended iterable unpacking to assign
# the first value to variable a and the remaining values to a list called b.
my_tuple = (1, 2, 3, 4, 5)
a, *b = my_tuple

print(a, b)

# Given the dictionary my_dict = {'name': 'John', 'age': 25, 'city': 'New York'},
# write a single line of code using dictionary unpacking to assign the value of 'name' to variable a,
# the value of 'age' to variable b, and the value of 'city' to variable c.
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
x, y, z = my_dict.keys()
print(x, y, z)

# Write a Python function called concatenate_lists that takes a variable number of lists as input
# and returns a single list that contains all the elements from the input lists.
# Use iterable unpacking to achieve this.


def concatenate_lists(*args):
    my_list = [element for lst in args for element in lst]
    return my_list


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

result = concatenate_lists(list1, list2, list3)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Consider the following nested list: list_nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Write a nested loop that iterates over the elements of the list
# and prints each element on a separate line.
list_nest = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def nested_print(list_nest):
    for x in list_nest:
        for j in x:
            print(j)


nested_print(list_nest)


# Write a Python function called unpack_string that takes a string as input
# and unpacks it into individual characters using iterable unpacking.
# The function should return a list of the unpacked characters.


def unpacking_string(s):
    return [i for i in s]


word = "hello"
print(unpacking_string(word))
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Write a Python function called even_square that takes a list of integers as input
# and returns a new list containing the squares of all the even numbers from the input list.
# Use list comprehension to generate the new list.


def even_square(list_int):
    return [num*num for num in list_int if num*num % 2 == 0]


my_list = (1, 2, 3, 4, 5, 6)
print(even_square(my_list))


# Write a Python function called merge_dicts that takes two dictionaries as input
# and returns a new dictionary that combines the key-value pairs from both dictionaries.
# If a key exists in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary.

def merge_dicts(dict_1, dict_2):
    for key, value in dict_2.items():
        if key in dict_1:
            dict_1[key] = value
        dict_1[key] = value
    return dict_1


dict1 = {
    'name': 'John',
    'age': 25,
    'city': 'New York',
    'occupation': 'Engineer'
}

dict2 = {
    'name': 'Alice',
    'age': 30,
    'country': 'Canada',
    'occupation': 'Teacher'
}

print(merge_dicts(dict1, dict2))


# Write a Python function called write_to_file that takes a list of strings
# and a file name as input and writes each string to a new line in the specified file.
# Use a with statement to ensure that the file is properly closed after writing.
def write_to_file(list_str, file_name):
    with open(file_name, 'w') as file:
        for word in list_str:
            file.write(f"{word} \n")


fruit_list = ["apple", "banana", "cherry", "date", "elderberry"]

write_to_file(fruit_list, "final/fruits.txt")


# Write a Python function called deep_copy that takes a nested list as input
# and returns a new nested list that is a deep copy of the input.
# That is, modifying the elements of the new list should not affect the elements of the original list.


def deep_copy(nest_list):
    copied_list = copy.deepcopy(nest_list)
    copied_list.append([45, 66, 33])
    copied_list[0][2] = 999
    return copied_list


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list)
print(deep_copy(nested_list))

# Write a Python generator function called fibonacci that generates the Fibonacci sequence,
# starting with 0 and 1, and continuing indefinitely. Use a generator to implement this sequence.


def fibonacci():
    current = 0
    previous = 0
    yield current
    current += 1
    while True:
        yield current
        current, previous = current + previous, current


f = fibonacci()
for _ in range(10):
    print(next(f))

# Write a Python function called timer that takes a function as input
# and returns a new function that behaves the same as the input function,
# but also prints the time taken for the function to execute.
# Use a decorator to implement this functionality.


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        duration = end - start
        print(f"The result is {result} and the duration is {duration}")
        return result
    return wrapper


@timer
def greet(name):
    """A function that greets a person by name."""
    print(f"Hello, {name}! How are you today?")


# Example usage
greet("Alice")


# Write a Python program that uses the pickle module to serialize a dictionary
# and save it to a file called data.pickle.
# Then, write another program that loads the dictionary from the file and prints its contents.
def dumps_file(pickle_file, ex_dict):

    serialization = pickle.dumps(ex_dict)

    with open(pickle_file, 'wb') as picked_out:
        picked_out.write(serialization)

    return "Dictionary have been successfully saved!"


def load_file(pickle_file):
    with open(pickle_file, 'rb') as picked_in:
        deserialization = pickle.load(picked_in)
    return deserialization


person_dict = {"name": "John", "age": 30, "city": "New York"}


print(dumps_file(pickle_file="final/data.pickle", ex_dict=person_dict))
print(load_file(pickle_file="final/data.pickle"))


# Write a Python function called unpack_args that takes a variable number of arguments
# and prints each argument on a separate line. Use *args to handle the variable number of arguments.
def unpack_args(*args):
    for num in args:
        print(num, end="")
    print()


unpack_args(1, 2, 3, 4, 5, 6, 7)

# Write a Python function called unpack_kwargs that takes a variable number of keyword arguments
# and prints each key-value pair on a separate line.
# Use **kwargs to handle the variable number of keyword arguments.


def unpack_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


unpack_kwargs(k=1, l=2, i=2, ko=23, no=9)


# Write a Python function called permutations that takes a list as input
# and returns a list of all possible permutations of the elements in the input list.
# Each permutation should be represented as a tuple.


def permutations_lists(input_list):
    perm = permutations(input_list)
    for i in perm:
        print(i)


input_lst = [1, 2, 3, 4, 5]
permutations_lists(input_lst)


# Write a Python function called queens that solves the Eight Queens problem.
# The function should take an integer n as input, representing the size of the chessboard,
# and return a list of lists representing valid configurations of n queens on the board.
# Each configuration should be represented as a list of n integers,
# where each integer represents the column number of the queen in that row.
def diagonal_threat(q):
    for col in range(7, 0, -1):
        for i in range(col):
            if col-i == abs(q[col]-q[i]):
                return True
    return False


def queens(n):

    ready_queens = list(permutations(range(n)))
    count = 0
    solution = []
    for queen in ready_queens:
        if diagonal_threat(queen):
            continue
        count += 1
        solution.append(queen)
        print(f"solution number {count}: {queen}")


queens(8)
