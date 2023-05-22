# import random

# example_list = [1,2,3,4,5,6,7,8,9,10]

# def log_function_call(func):
#  def wrapper(*args, **kwargs):
#   # WHAT IS HAPPENING BEFORE THE FUNCTION IS CALLEd
#   print(f"Calling function {func.__name__}")

#   #CALLING THE ACTUAL FUNCTION
#   result = func(*args, **kwargs)

#   #AFTER THE FUNCTION IS CALLED IF THERE IS OTHER WORK YOU WANT TO DO
#   print(f"Finished calling function {func.__name__}")

#   return result
#  return wrapper


# @log_function_call
# def add_numbers(x, y):
#  return x + y

# @log_function_call
# def minus_numbers(x, y):
#  return x - y
# -------------------------------------------------------------------------------------------------------
import time
import functools
import string
from functools import wraps
import random
example_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # WHAT IS HAPPENING BEFORE THE FUNCTION IS CALLED
        print(f"Calling function {func.__name__}")

        # CALLING THE ACTUAL FUNCTION
        result = func(*args, **kwargs)

        # AFTER THE FUNCTION IS CALLED IF THERE IS OTHER WORK YOU WANT TO DO
        print(
            f"Finished calling function {func.__name__}. Now bring down the size of the list")
        while len(example_list) > 12:  # keep the list 11 elements
            example_list.pop(0)

        return result
    return wrapper


@list_function_call
def add_to_list():
    '''
    Here is information about the function
    '''
    for x in range(5):
        example_list.append(random.randint(0, 20))
    return


# print(add_to_list.__name__)
print(add_to_list.__doc__)

add_to_list()
# add_to_list()
# add_to_list()
# add_to_list()
# add_to_list()
print(example_list)

# result = add_numbers(2, 3)
# print(result)
# result = minus_numbers(2, 3)
# print(result)

# ------------------------------------------------dictionary comprehension with decorator--------------------------------------------------------


call_dict = {}  # call_dict is the dictionary


def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        value = call_dict.get(func.__name__, 0)
        call_dict[func.__name__] = value + 1
        result = func(*args, **kwargs)
        print(f"Finished calling function {func.__name__}")
        return result
    return wrapper


@count_calls  # count_calls is the decorator
def add(x, y):
    return x+y


@count_calls
def multi_num(x, y):
    return x*y


# ------------------------------------------------------------------Recursion with Decorator-----------------------------
# HOW TO USE WRAPPERS EFFECTIVELY EVEN WITH RECURSION
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        return result, duration
    return wrapper


def merge_sort(list_n):
    if len(list_n) > 1:
        mid = len(list_n) // 2
        L = list_n[:mid]
        R = list_n[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                list_n[k] = L[i]
                i += 1
            else:
                list_n[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list_n[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list_n[k] = R[j]
            j += 1
            k += 1


@time_it
def merge_sort_call(list_to_sort):
    merge_sort(list_to_sort)
    return list_to_sort


my_list = [random.randint(1, 40) for _ in range(12)]
print(my_list)
print(merge_sort_call(my_list))

# ----------------------------------------------------------------dictionary comprehension ------------------------
# from math import sqrt


# def is_prime(num):
#   if num <= 2:
#     return True
#   x = 2
#   while x < (sqrt(num) + 1):
#     if num % x == 0:
#       return False
#     x += 1
#   return True


# def next_prime():
#  current_prime = 2
#  while (True):
#    while not is_prime(current_prime):
#      current_prime += 1
#    yield current_prime
#    current_prime += 1


# n = next_prime()
# prime_dict = {x : next(n) for x in range(1,100)}
# print(prime_dict)


# example_list = [x for x in range(100) if x % 2 == 0]
# example_dict = {str(x) : x for x in range(100) if x % 2 == 0}
# print(example_dict)

# This example below maps the numbers to their cubes that are not divisible by 4. up to 100


# map a number to

# make a dictionary that has as keys number of letters
# of items with that number of letters
# ONLY IF
# CONDITION 1: the name starts with an A
# or
# CONDITION 2: the length is divisible by two
# list_of_items = ["apple", "bike", "batoner", "ape", "adam"]
# item_dictionary = {len(x) : x for x in list_of_items if (x[0] == "a" and len(x) % 2 != 0) or (x[0] != "a" and len(x) % 2 == 0)}
# print(item_dictionary)

# ----------------------------------------------------------------Files--------------------------------------------------------------------------------------

# # file example
# # readline and read, stripline and strip,
# with open('/Users/jacobweissman/Desktop/381p/381p_inverted.txt') as file:
#   next_line = "nonsense"
#   while len(next_line) > 0:
#     next_line = file.readline()
#     print(next_line)
#   # contents = file.readlines()
#   # print(contents)


# open the file, get the contents into a list of tuples
# word_list = []
# with open("/Users/jacobweissman/Desktop/381p/381p_inverted.txt") as file:
#     line_number = 0
#     index_dict = {}
#     for line in file:
#         line_number += 1
#         table = str.maketrans('', '', string.punctuation)
#         current_line = line.lower().translate(table).split()
#         for word in current_line:
#             if word in index_dict:
#                 index_dict[word].append(line_number)
#             else:
#                 index_dict[word] = [line_number]
# for word, index_list in index_dict.items():
#     print(word + ": ")
#     print(index_list)
