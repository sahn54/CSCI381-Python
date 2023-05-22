# practice writing decorators

# decorator with merge-sort will give you a problem

# only decorator should be used for function call rather than the function itself.
# which resolves the problem with merge-sort


# Final Exam: Introduction to Decorators in Python

# Please answer the following questions by writing the code. Ensure that your code is correct and follows the principles of decorators as discussed in the course material.
# ---------------------------------------------------------------Decorator-----------------------------------------------------------------------------------------
# Question 1:
# Write a decorator function called "timer" that measures the execution time of a function
# and prints the time taken in seconds. Apply this decorator to the following function:
import logging
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        return result, duration
    return wrapper


@timer
def calculate_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


f = calculate_factorial(4)
print(f)

# Question 2:
# Write a decorator function called "uppercase_result" that converts the output of a function
# to uppercase. Apply this decorator to the following function:


def uppercase_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


@uppercase_result
def concatenate_strings(a, b):
    return a + b


g = concatenate_strings("Hello ", "World")
print(g)


# Question 3:
# Create a decorator function called "logger" that logs the inputs and outputs of a function.
# The logger should print the input arguments and the return value of the function.
# Apply this decorator to the following function:


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Input: {args}")
        logging.info(f"Output: {result}")
        return result
    return wrapper


@logger
def multiply_numbers(a, b):
    return a * b


logging.basicConfig(level=logging.INFO)
h = multiply_numbers(3, 6)

print(h)

# -------------------------------------Generator-------------------------------------------------
# Question 4:
# Write a generator function called "fibonacci_sequence" that generates the Fibonacci sequence.
# The generator should yield each Fibonacci number in the sequence.
# Generate the first 10 Fibonacci numbers using this generator.
# 0,1,1,2,3,5,8,11


def fibonacci_sequence(n):
    previous = 0
    current_digit = 1
    for num in range(n):
        if num == 0:
            yield previous
            previous += current_digit
        elif num == 1 or num == 2:
            yield previous
        else:
            current_digit, previous = previous + current_digit, current_digit
            yield current_digit


fib = fibonacci_sequence(10)
for _ in range(10):
    print(next(fib))


# Question 5:
# Create a generator function called "countdown" that generates a countdown sequence
# from a given number to 1.
# The generator should yield each number in the sequence.
# Generate a countdown sequence starting from 5.


# def count_down(n):
#     count = n
#     for _ in range(n):
#         yield count
#         count -= 1


# cd = count_down(5)
# for i in cd:
#     print(i)
def count_down(n):
    while n > 0:
        yield n
        n -= 1


for i in count_down(5):
    print('T-minus', i)

# Question 6:
# Write a generator function called "read_file_lines" that takes a file path as input
# and yields each line of the file.
# Use this generator to read and print all the lines of a file named "data.txt".


def read_file_lines(file_name):
    with open(file_name) as f:
        for line in f.readlines():
            yield line


reading = read_file_lines("final/Topics.txt")

print(next(reading))
print(next(reading))


# Note: Ensure that your code is well-formatted and follows proper Python syntax and indentation.
