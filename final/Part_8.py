# Decorators


# a. Prints that func has entered
# b. Calls func to do the work
# c. Prints that func has exited.
from random import randint
import time
import timeit
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ wrapper"""
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"finished Calling function {func.__name__}")
        return result
    return wrapper


@my_decorator
def add_numbers(x, y):
    """my func"""
    return x + y


# without calling out wrapper
print(add_numbers(2, 4))
print(add_numbers.__name__)
print(add_numbers.__doc__)  # the string from the add_numbers
print()

# with  calling out wrapper
add_numbers = my_decorator(add_numbers)
result = (add_numbers(2, 4))
print(result)
# ------------------------------------------Example-----------------------------------


def mult_num(x, y):
    """mult func"""
    return x * y

# from functools import wraps


def the_function(func):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        """The wrapper"""
        print("Before the function is called")
        result = func(*args, **kwargs)
        print("After the function is called")
        return result
    return my_wrapper


# mult_num = the_function(mult_num)
# my_result = mult_num(2, 2)
# print(my_result, mult_num.__name__)
# print(my_result, mult_num.__doc__)


# --------------------------------------Problems--------------------------------------------------------------

# Write a decorator that when applied to a function will keep track of how many times that
# function has been called. It will do this by keeping count of the calls to the decorated functions in
# a dictionary passed to the decorator.
call_dictionary = {}

# write the decorator:


def count_calls(call_dictionary):
    def decorator(func):
        @wraps(func)  # type: ignore
        def prob_wrapper(*args, **kwargs):
            # print(f"Calling function {func.__name__}")
            name = f"{func.__name__}"
            value = call_dictionary.get(func.__name__, 0)
            call_dictionary[func.__name__] = value + 1
            result = func(*args, **kwargs)
            # print(f"Closing function {func.__name__}")
            return result
        return prob_wrapper
    return decorator


@count_calls(call_dictionary)  # count_calls is the decorator
def add(x, y):
    return x+y


@count_calls(call_dictionary)
def multiply(x, y):
    return x*y


z = add(2, 3)
print(call_dictionary)
z = add(2, 3)
print(call_dictionary)
z = multiply(2, 3)
print(call_dictionary)
# When I run the above code, I get:
# {'add': 1}
# {'add': 2}
# {'add': 2, 'mult': 1}

# ------------------------------------------Example-----------------------------------

# Another example. A decorator to return the runtime of the decorated functions.


def my_function():
    time.sleep(2)  # simulate a 2 second delay
    return "Hello, world!"


start_time = time.time()
result = my_function()
end_time = time.time()

duration = end_time - start_time

# print(f"Result: {result}")
# print(f"Duration: {duration} seconds")

# Another useful function in the time library is timeit, which provides a simple way to time the
# execution of a function with higher precision:

# define my_function for two second and return "Hello, world"

# number = how many times should be executed
duration = timeit.timeit(my_function, number=1)
# print(f"Duration: {duration} seconds")

# The timeit module is specifically designed to measure the execution time of small code snippets
# with high accuracy. It provides a timeit() function that takes a Python statement as input and
# executes it a number of times to measure the average execution time.


# Example_1

def ex_function():
    for i in range(1000000):
        pass


# timeit can be used as a standalone function
time_taken = timeit.timeit(ex_function, number=100)
# print("Execution time:", f"{time_taken:.4f} seconds")


def add_function():
    sum = 0
    for i in range(1000000):
        sum += i
    return sum


# Time the execution of my_function 1000 times
t = timeit.timeit(add_function, number=1000)
# print(f"Execution time: {t:.6f} seconds")


# --------------------------------------Problems--------------------------------------------------------------

# Write a decorator time_it so that when it decorates a sort function, it sorts the list passed to the
# function and returns the runtime.


def decorator_time_it(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        sort_time = end_time - start_time
        return result, sort_time
    return wrapper

# The first sort: bubble sort. Write it and sort 1,000 random integers.


@decorator_time_it
def bubble_sort(arr):
    n = len(arr)
    for _ in range(n-1):
        isSwapping = False
        for i in range(n-1):
            if arr[i] > arr[i + 1]:
                temp_i = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp_i
                isSwapping = True
        if isSwapping == False:
            break
    return arr

# The second sort: selection sort. Write it and sort 1,000 random integers.


@decorator_time_it
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[min_index]
            arr[min_index] = arr[i]
            arr[i] = temp
    return arr


# my_array = [randint(1, 1000) for _ in range(5)]
# print(f"The random list: {my_array}")
# print(bubble_sort(my_array))
# print(selection_sort(my_array))


# print(
#     f"Duration for by {bubble_sort.__name__}: {bubble_sort_time:.6f} seconds")
# print(
#     f"Duration for by {selection_sort.__name__}: {selection_sort_time:.6f} seconds")


# print(f"result of bubble_sort {bubble_sort(arr)}")
# print(f"result of selection_sort {selection_sort(arr)}")


# Here is the code for merge sort. Time it and see how it compares to the above two sorts.
@decorator_time_it
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


bubble_sort = decorator_time_it(bubble_sort)
selection_sort = decorator_time_it(selection_sort)
merge_sort = decorator_time_it(merge_sort)

arr = [randint(0, 1000) for _ in range(10000)]
_, bubble_sort_time = bubble_sort(arr.copy())
_, selection_sort_time = selection_sort(arr.copy())
_, merge_sort_time = merge_sort(arr.copy())
name = ""
print(f"Bubble Sort time is: {bubble_sort_time}")
print(f"Selection Sort time is: {selection_sort_time}")
print(f"Merge Sort time is: {merge_sort_time}")
print()

if bubble_sort_time < selection_sort_time and bubble_sort_time < merge_sort_time:
    name = "Bubble Sort"
    diff = selection_sort_time - bubble_sort_time
    diff_final = merge_sort_time - bubble_sort_time
elif selection_sort_time < bubble_sort_time and selection_sort_time < merge_sort_time:
    name = "Selection Sort"
    diff = bubble_sort_time - selection_sort_time
    diff_final = merge_sort_time - selection_sort_time
else:
    name = "Merge Sort"
    diff = bubble_sort_time - merge_sort_time
    diff_final = selection_sort_time - merge_sort_time
print(name + ' is faster by '+str(diff)+' seconds.')
print(name + ' is faster by '+str(diff_final)+' seconds.')


# What happened. Now what?

# Takes a long time to execute. Indicates Merge Sort is faster.


# One possible reason why the merge sort might not be faster than
# bubble sort and selection sort in this specific implementation is that
# the input size is relatively small (only 1000 elements).

# Merge sort typically performs better than other sorts
# (such as bubble sort and selection sort) for large input sizes
# because its time complexity is O(n log n) in the worst case,
# while the time complexity of bubble sort and selection sort is O(n^2) in the worst case.
# However, for small input sizes, the overhead of the recursion and copying of sub-arrays
# that occur in the merge sort implementation may outweigh the benefits of its
# better worst-case time complexity, making it slower than other sorts.

# Another reason could be the fact that the merge sort implementation in this code is not optimized.
# For example, in the while loops that copy the remaining elements from L and R arrays
# to the main array, the code assigns a single value to the main array instead of using slicing
# to copy the entire remaining sublist.
# This can result in slower performance due to more individual assignments being performed.
# Additionally, the code creates new sub-arrays in every recursive call to merge_sort,
# which can be inefficient for large input sizes.

# Overall, the specific implementation of merge sort in this code
# may not be optimized for performance,
# and the input size is relatively small,
# which can make other sorting algorithms such as bubble sort and selection sort perform better.
# However, for larger input sizes, merge sort is generally expected to perform better
# due to its better time complexity.
