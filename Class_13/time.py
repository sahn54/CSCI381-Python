import random
import time
import timeit


def my_function():
    time.sleep(2)  # simulate a 2 second delay
    return "Hello, world!"


start_time = time.time()
result = my_function()
end_time = time.time()
duration = end_time - start_time
print(f"Result: {result}")
print(f"Duration: {duration} seconds")
# When I run this code I get:
# Result: Hello, world!
# Duration: 2.0110862255096436 seconds


def swap(a, b):
    return b, a

# The first sort: bubble sort. Write it and sort 1,000 random integers.


def bubble_sort(arr):
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            arr.append(swap(arr[i], arr[i+1]))


# The second sort: selection sort. Write it and sort 1,000 random integers.


# Write a decorator time_it so that when it decorates a sort function, it sorts the list passed to the
# function and returns the runtime.

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished calling function {func.__name__}")
        return result
    return wrapper


# ---------------------------------------------------------------------------------------------------------

# Here is the code for merge sort. Time it and see how it compares to the above two sorts.


# @time_it
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
