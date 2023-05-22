# 1. Write a Python function called factorial that takes an integer argument n and returns the factorial of n.
# A factorial (n!) of a number is the product of all positive integers from 1 to that number.
# For example, the factorial of 5 is 54321 = 120.

def factorial(number):
    result = 1
    for i in range(1, number+1):
        result *= i
    return result


print(factorial(5))


# 2. Write a Python function called reverse_words that takes a string argument str and returns a new string with the words in reverse order.
# For example, if s is "hello world", the function should return "world hello".

def reverse_words(str_1):
    # if there is a space, the next string after the space is a next element.
    # split()[::-1] splits a string into a list
    # reverse()
    # attempt 1:    #I am trying to have the word saved as an element
    s = str_1.split()[::-1]
    print(s)
    my_list = []
    for i in s:
        my_list.append(i)

    word = " ".join(my_list)
    return word
    # new_str = str[::-1]
    # return new_str


print(reverse_words("hello world"))

# 3. Write a Python class called Rectangle that represents a rectangle with a given width and height.
# The class should have two methods: area,
# which returns the area of the rectangle,
# and perimeter, which returns the perimeter of the rectangle.


class rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        self.perimeter_val = (self.width * 2) + (self.height * 2)

    def area(self):
        self.area_val = self.width * self.height


# width = int(input("Enter a width: "))
# height = int(input("Enter a height: "))
# my_rectangle = rectangle(width=width, height=height)
# my_rectangle.perimeter()
# my_rectangle.area()
# print(my_rectangle.perimeter_val)
# print(my_rectangle.area_val)


# 4. Write a Python function called flatten that takes a list of lists
# and returns a flattened version of the list.
# For example, if the input list is [[1, 2, 3], [4, 5], [6, 7, 8, 9]],
# the function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].
# Lisp - append the lists
def flatten(in_list):
    # change the list to a string and then convert it to a list again
    new_list = []
    for i in in_list:  # [1, 2, 3] [4, 5] [6, 7, 8, 9]
        for j in i:
            new_list.append(j)
    return new_list


my_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(flatten(my_list))

# 5. Write a Python function called fibonacci that takes an integer argument n
# and returns the nth Fibonacci number.
# The Fibonacci sequence is a sequence of numbers in which each number is
# the sum of the two preceding ones.
# The first two numbers in the sequence are 0 and 1,
# so the sequence starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

# fibonacci numbers from 1 to 100


def fibonacci(n):
    # We will use a dictionary to solve the problem
    # n calls the key
    main_sum = 0
    fibonacci_dict = {}
    # will return the value based on the n
    # values are going to be the main_sum for each sequence
    fibonacci_dict[1] = main_sum
    fibonacci_dict[2] = main_sum + 1
    for i in range(3, 101):
        main_sum = fibonacci_dict[i-1] + fibonacci_dict[i-2]
        fibonacci_dict[i] = main_sum
    return fibonacci_dict[n+1]  # since by default n indicates from 0 to n


# nth_num = int(input("Enter a number: "))
# print(fibonacci(nth_num))


# 6. Write a Python function called unique_words that takes a string argument s
# and returns a list of unique words in s, in alphabetical order.
# For example, if s is "hello world, hello universe",
# the function should return ["hello", "universe", "world"].
def unique_words(input_str):
    # we use a dictionary or a set , i pick a set
    my_set = set()
    new_list = []
    # clean up the words by taking out commas symbols and
    input_str = input_str.strip(",")
    # split each word into a list
    current_list = input_str.split()
    for i in current_list:
        if i not in my_set:
            my_set.add(i.strip(","))
            new_list.append(i.strip(","))

    # return a list
    return new_list


print(unique_words("hello world, hello universe"))


def unique_words_list_com(input_str):
    my_set = set()
    current_list = input_str.split()
    return [word.strip(",") for word in current_list if word.strip(",") not in my_set and (my_set.add(word) or True)]


print(unique_words_list_com("hello world, hello universe"))


# Write a Python function called binary_search that takes a sorted list of integers
# and a target integer, (two parameters)
# and returns the index of the target integer in the list if it is present,
# or -1 if it is not present.
# For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9]
# and the target integer is 6, the function should return 5.
def binary_search(sorted_list, target_int):
    # list of integers that is sorted.
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target_int:
            return mid
        elif sorted_list[mid] < target_int:
            left = mid+1
        else:
            right = mid - 1
    return -1


my_sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_sorted_list, 6))  # 5
print(binary_search(my_sorted_list, 16))  # -1


# Write a Python function called merge_sorted that takes two sorted lists of integers
# and returns a new sorted list that contains all the elements
# from both input lists,in ascending order.
# For example, if the input lists are [1, 3, 5, 7, 9] and [2, 4, 6, 8],
# the function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].


def merge_sorted(sort_list_1, sort_list_2):  # two sort lists
    # check if either list is empty
    if len(sort_list_1) == 0:
        return sort_list_2
    elif len(sort_list_2) == 0:
        return sort_list_1

    # recursive divide-and-conquer approach
    if sort_list_1[0] < sort_list_2[0]:
        return [sort_list_1[0]] + merge_sorted(sort_list_1[1:], sort_list_2)
    else:
        return [sort_list_2[0]] + merge_sorted(sort_list_1, sort_list_2[1:])


my_sorted_list_1 = [2, 4, 6, 8]
my_sorted_list_2 = [1, 3, 5, 7, 9]
print(merge_sorted(my_sorted_list_1, my_sorted_list_2))


# Write a Python function called is_palindrome that takes a string argument s and returns True
# if s is a palindrome (a word or phrase that reads the same backward as forward),
# and False otherwise. For example, if s is "racecar", the function should return True.


def is_palindrome(str_p):
    # str_p is a string
    size_r = len(str_p)
    for i in range(len(str_p)):
        if str_p[i] != str_p[size_r-1]:
            return False
        size_r -= 1

    return True


ex_string = "racecar"
print(is_palindrome(ex_string))

# Write a Python function called most_common_word that takes a string argument s and returns the most common word in s.
# If there are multiple words with the same frequency, the function should return the word that appears first in s.
# You can assume that s contains only lowercase letters and spaces, with no punctuation.
# For example, if s is "the quick brown fox jumps over the lazy dog", the function should return "the".


def most_common_word(input_str):
    list_input = input_str.strip(" ").split()  # really important
    # use a dictionary to solve this problem
    word_count_dict = {}
    word_count = set()
    for word in list_input:
        word = word.lower()
        if word not in word_count:
            word_count.add(word)
            word_count_dict[word] = 1
        else:
            word_count_dict[word] += 1
    max_value = max(word_count_dict, key=word_count_dict.get)  # type: ignore

    return max_value


new_sentence = "hello my my my my the quick brown fox jumps over the lazy dog"
print(f"Most used word in this string is: {most_common_word(new_sentence)}")


# list and dictionary comprehension
