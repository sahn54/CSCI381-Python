# Write a function is_even(x) which returns True if x is even and False otherwise.
import random


def is_even(x):
    if x % 2 == 0:
        return True
    return False

# Write a function is_prime(x) which returns True if x is a prime number and False otherwise.


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


# Write a program to ask the user for two integers, first and last. Write a program to print out all the
# primes between first and last (inclusive), five values per line.
# def checking_primes_between():
#     input_1 = int(input("Enter first : "))
#     input_2 = int(input("Enter last:"))
#     prime_count = 0
#     if input_2 < input_1:
#         return "Prime input_2 should bigger than input_1!"
#     for i in range(input_1, input_2+1):
#         is_prime = True
#         for j in range(2, int(i**0.5)+1):
#             if i % j == 0:
#                 is_prime = False
#                 break
#         if is_prime and i > 1:
#             print(i, end=" ")
#             prime_count += 1
#             if prime_count == 5:
#                 print()
#                 prime_count = 0


# checking_primes_between()


# Write a function sum_of_digits(n) which returns the sum of the digits of n.
# def sum_of_digits(n):
#     str_num = str(n)
#     final_num = 0
#     for num in str_num:
#         final_num += int(num)
#     return final_num

def sum_of_digits(n):
    return sum(int(num) for num in str(n))  # type: ignore


# print(sum_of_digits(123))


# Write a function my_bin(n) which converts an integer number to a binary string representation of n.
# But Leave out the leading ‘0b’ returned by the built in function bin.

def my_bin(n):
    bin_n = ""
    while n > 0:
        digit = n % 2
        n //= 2
        bin_n += str(digit)
    return bin_n[::-1]


# print(my_bin(4))
# -----------------------------------------LISTS ------------------------------------------------------------
# Write a program that creates a list with the integers 1 – 10. Using a for loop add up all the elements of
# the list and print the sum.


def sum_list():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sum(num for num in new_list)


print(sum_list())


# Write a program that creates a list with the integers 1 – 10. Using a for loop, add up all the elements of
# the list that are even and print the sum.
def sum_even_list():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sum(num for num in new_list if num % 2 == 0)


print(sum_even_list())
# Write a program that creates a list with the integers 1 – 10. Using a for loop add up all the elements of
# the list that are odd and print the sum


def sum_odd_list():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sum(num for num in new_list if num % 2 != 0)


print(sum_odd_list())

# Write a program that creates a list with the integers 1 – 10. Using a for loop add up all the elements of
# the list that are in even positions ( 0 is even) and print the sum.


def sum_even_pos_list():
    new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return sum(new_list[i] for i in range(len(new_list)) if i % 2 == 0)


print(sum_even_pos_list())

# Write a program to fill a list of size 10 with random integers in the range 1 – 10 and print it out.


def random_list():
    new_list = []
    for _ in range(11):
        new_list.append(random.randint(1, 10))
    return new_list


print(random_list())

# Modify the program above so that we print the list as well as the maximum integer in the list. Do this
# two ways.


def random_list_max_1():
    new_list = []
    for _ in range(11):
        new_list.append(random.randint(1, 10))
    return new_list, max(new_list)


print(random_list_max_1())


# Modify the program above so that it also prints the position in the list where the maximum element was
# found.

def random_list_max_2():
    new_list = []
    max_value = 0
    for _ in range(11):
        num = random.randint(1, 10)
        new_list.append(num)
        if max_value < num:
            max_value = num
    return new_list, max_value


print(random_list_max_2())
# ------------------------------Sorting----------------------------------


def select_sort(list_n):
    for i in range(len(list_n)-1):
        min = list_n[i]
        pos = i
        for j in range(i, len(list_n)):
            if list_n[j] < min:
                min = list_n[j]
                pos = j
        list_n[i], list_n[pos] = list_n[pos], list_n[i]
    return list_n


non_sorted = [random.randint(1, 50) for _ in range(10)]
print(non_sorted)
print(select_sort(non_sorted))


def bubble_sort(list_n):
    for i in range(len(list_n)):
        sorted = True
        for j in range(len(list_n)-i-1):
            if list_n[j] > list_n[j+1]:
                list_n[j], list_n[j+1] = list_n[j+1], list_n[j]
                sorted = False
        if sorted == True:
            return list_n


non_sorted_2 = [random.randint(1, 50) for _ in range(10)]

print(non_sorted_2)
print(bubble_sort(non_sorted_2))


# Given a list, print the elements of that list in reverse order. Do this in two ways.
list_to_sort = [random.randint(1, 50) for _ in range(10)]

# one way to sort:


# using select_sort
def select_sort_reverse(list_n):
    for i in range(len(list_n)-1):
        min = list_n[i]
        pos = i
        for j in range(i, len(list_n)):  # range for j will be from i to len(list_n)
            if list_n[j] < min:
                min = list_n[j]
                pos = j
        list_n[i], list_n[pos] = list_n[pos], list_n[i]
    return list_n[::-1]


print()
print(list_to_sort)
print(select_sort_reverse(list_to_sort))
list_to_sort.sort(reverse=True)
print(list_to_sort)
print(sorted(list_to_sort, reverse=True))


# ------------------------Lambdas--------------------------------
# Problem: Write a lambda function that takes two arguments, x and y, and returns their sum.
# Question: Write a lambda function that calculates the sum of two numbers.
lambda_1 = (lambda x, y: x + y)
print(lambda_1(2, 3))

# Problem: Write a lambda function that takes a string s and returns the length of the string.
# Question: Write a lambda function that calculates the length of a given string.
lambda_2 = (lambda s: len(s))
print(lambda_2("HelloWorld"))

# Problem: Write a lambda function that takes a list nums and returns the square of each number in the list.
# Question: Write a lambda function that squares each number in a given list.

list_k = [34, 54, 23, 123, 54, 2, 3, 54, 98]
lambda_3 = list(map(lambda x: x**2, list_k))

print(lambda_3)

# Problem: Write a lambda function that takes a dictionary student and returns the value associated with the key 'grade'.
# Question: Write a lambda function that extracts the grade value from a student dictionary.
student = {'name': 'John', 'age': 20, 'grade': 'A'}


def lambda_4(student): return student['grade']


print(lambda_4(student))

# Problem: Write a lambda function that takes a list names and returns a new list containing only the names that start with the letter 'A'.
# Question: Write a lambda function that filters names starting with 'A' from a given list.
names = ["Alice", "Bob", "Charlie", "Daisy", "Ethan"]

lambda_5 = list(filter(lambda x: x[0] == 'A', names))
print(lambda_5)

# Problem: Write a lambda function that takes two integers, a and b, and returns the maximum of the two numbers.
# Question: Write a lambda function that finds the maximum of two given numbers.

# Problem: Write a lambda function that takes a list numbers and returns a new list with only the even numbers.
# Question: Write a lambda function that filters even numbers from a given list.

# Problem: Write a lambda function that takes a list words and returns a new list with the words sorted in alphabetical order.
# Question: Write a lambda function that sorts a given list of words alphabetically.

# Problem: Write a lambda function that takes a list grades and returns the average of the grades.
# Question: Write a lambda function that calculates the average of a list of grades.

# Problem: Write a lambda function that takes a list strings and returns a new list with the strings converted to uppercase.
# Question: Write a lambda function that converts a given list of strings to uppercase.
