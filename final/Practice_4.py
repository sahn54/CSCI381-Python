# Write a Python function called uppercase_strings that takes a list of strings as input
# and returns a new list containing the uppercase versions of all the strings in the input list.
# Use list comprehension to generate the new list.
import time
import functools


def uppercase_strings(list_str):
    return [word.upper() for word in list_str]


ex1 = ["Hello", "king", "lion", 'rock']
print(uppercase_strings(ex1))


# Write a Python function called create_dict that takes two lists of equal length as input,
# one containing keys and the other containing values,
# and returns a dictionary with the keys and values from the input lists.
def create_dict(list_1, list_2):
    if len(list_1) != len(list_2):
        return "Not equal length"
    return {list_1[i]: list_2[i] for i in range(len(list_1))}


ex_2 = ["king", "Queen", "Mr", "Mrs", "Lord"]
ex_3 = ["Arthur", "Mary", 'Jack', "Smith", "Min"]

print(create_dict(ex_2, ex_3))

# Write a Python function called read_from_file that takes a file name as input
# and returns a list of strings representing the lines of the file.
# Use a with statement to ensure that the file is properly closed after reading.


def read_from_file(file):
    file_content = file.read()
    list_file = file_content.split()
    list_file_new = []
    for word in list_file[1::]:
        list_file_new.append(word.replace(',', ' '))
    return list_file_new


with open("Own_project/numbers.txt") as file:
    print(read_from_file(file))


# Write a Python function called shallow_copy that takes a list of lists as input
# and returns a new list of lists that is a shallow copy of the input.
# That is, modifying the elements of the new list may affect the elements of the original list.
def shallow_copy(list_of_list):
    new_list = list_of_list.copy()
    return new_list


ex_4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]

new_copy = shallow_copy(ex_4)
print(new_copy)
new_copy[1][0] = 9
print(new_copy)
print(ex_4)

# Write a Python generator function called fibonacci that generates the Fibonacci sequence indefinitely.
# The generator should start with the first two numbers in the sequence, 0 and 1,
# and each subsequent value should be the sum of the two preceding values.


def fibonacci():
    value = 1
    previous = 0
    result = 0
    yield result
    while True:
        if result < 3:
            result = value + previous
            previous = result
            yield result
        result = value + previous
        yield result
        value = result


f = fibonacci()
print(next(f))
print(next(f))

# Write a Python function called timer that takes a function as input
# and returns a new function that behaves the same as the input function,
# but also prints the time taken for the function to execute.
# Use a decorator to implement this functionality.


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        return result, duration
    return wrapper


@timer
def add(x, y):
    return x+y


@timer
def divide_int(x, y):
    if y != 0:
        return x//y
    else:
        y += 1
        return x//y


f = divide_int(9, 2)

print(f)


# Write a Python function called split_name that takes a string in the format "last name, first name"
# as input and returns a tuple containing the first and last names as separate elements.
def split_name(name):

    splitted_name = tuple(name.replace(',', '').split())
    return splitted_name[::-1]


print(split_name("last, first"))


# Write a Python function called join_strings that takes a list of strings
# and a separator string as input and returns a single string containing all the input strings
# joined together with the separator.
# Use the join method of strings to implement this function.


def join_strings(string_list, separator):
    return separator.join(string_list)


# Example usage
input_list = ["Hello", "World", "Python"]
separator_str = "-"

result = join_strings(input_list, separator_str)
print(result)


# Write a Python function called password that request and validate a password from your user.
# A valid password will be any two digit integer, both digits of which are even.
# give the user chances to enter a correct password.
# At each incorrect attempt, print "Invalid password, Try again"
# If the password enter is correct print " Correct! You may access the system" Exit the program
# If the password entered is incorrect print "Too many invalid attempts. Please try again later."


def password():

    attempt = 3

    while attempt > 0:
        user_ans = int(input("Enter: "))
        even = 0
        list_num = [int(i) for i in str(user_ans)]
        for i in list_num:
            if i % 2 == 0:
                even += 1
            if even >= 2:
                return "Correct! You may access the system"
        print("Invalid password, Try again!")
        attempt -= 1
    return "Too many invalid attempts. Please try again later."


print(password())


def reverse_num(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev


print(reverse_num(123))
