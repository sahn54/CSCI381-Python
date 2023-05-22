
# Write a Python function called count_words that takes a string argument s
# and returns a dictionary mapping each word in s to the number of times it appears.
# You can assume that s contains only lowercase letters and spaces, with no punctuation.
# For example, if s is "the quick brown fox jumps over the lazy dog",
# the function should return {"the": 2, "quick": 1, "brown": 1, "fox": 1, "jumps": 1, "over": 1, "lazy": 1, "dog": 1}.
def count_word(s):
    count_word_list = [word for word in s.strip(" ").split()]
    count_word_dict = {}
    for word in count_word_list:
        if word in count_word_dict:
            count_word_dict[word] += 1
        else:
            count_word_dict[word] = 1
    return count_word_dict
    # returns dictionary mapping


new_word = "the quick brown fox jumps over the lazy dog"
print(count_word(new_word))

# Write a Python class called LinkedList that represents a linked list with the following methods:
# __init__, which creates an empty linked list;
# add, which adds a new node with the given value to the end of the linked list;
# remove, which removes the first node in the linked list with the given value;
# contains, which returns True if the linked list contains a node with the given value,
# and False otherwise.


class LinkedList:

    def __init__(self):
        self.linked_list = []

    def add(self, new_node):
        self.linked_list.append(new_node)

    def remove(self, node):
        for list_node in self.linked_list:
            if list_node == node:
                self.linked_list.remove(node)
                return
        print(f"Node{node} does not exist in linked list")

    def contains(self, node):
        return node in self.linked_list


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
print(ll.linked_list)  # [1, 2, 3]
print(ll.contains(2))  # True
print(ll.contains(4))  # False
ll.remove(2)
print(ll.linked_list)  # [1, 3]


# Write a Python function called transpose that takes a 2D list of integers
# and returns a new 2D list that represents the transpose of the input list.
# That is, if the input list is [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
# the function should return [[1, 4, 7], [2, 5, 8], [3, 6, 9]].

def transpose(two_d_list):
    new_two_d_list = []
    for i in range(len(two_d_list)):
        inner_two_d_list = []
        for j in range(len(two_d_list)):
            inner_two_d_list.append(two_d_list[j][i])
        new_two_d_list.append(inner_two_d_list)
    # return a list that returns elements by index
    return new_two_d_list


input_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(input_list))


def transpose_list_com(two_d_list):
    return [[two_d_list[j][i] for j in range(len(two_d_list))] for i in range(len(two_d_list))]


print(transpose_list_com(input_list))
# Write a Python function called largest_palindrome that takes a string argument s
# and returns the largest palindrome that appears in s.
# If there are multiple palindromes with the same length,
# the function should return the one that appears first in s.
# You can assume that s contains only lowercase letters and spaces, with no punctuation.
# For example, if s is "racecar madam kayak level", the function should return "racecar".


def largest_palindrome(s):
    list_of_words = [word for word in s.strip(' ').split()]
    # check if each word is a palindrome
    index = 0
    largest = ""
    for p in list_of_words:
        if p[index] == p[len(p) - index - 1]:
            if len(largest) < len(p):
                largest = p
        else:
            print(f"this string is not a palindrome")
    return largest


palindromes = "racecar madam kayak level"
print(largest_palindrome(palindromes))
# Write a Python function called median that takes a list of integers
# and returns the median value.
# If the list has an odd number of elements, the median is the middle element.
# If the list has an even number of elements, the median is the average of the two middle elements.
# For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9], the function should return 5.


def median(list_int):

    if len(list_int) % 2 != 0:
        mid_index = len(list_int) // 2
        return list_int[mid_index]
    else:
        # for even numbers of elements, we need to sort and then find the average
        sorted_list = sorted(list_int)
        # since it is even we want to locate the index number -1
        mid_index_1 = len(sorted_list) // 2 - 1
        mid_index_2 = len(sorted_list) // 2
        return (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / 2
        # make sure the () is placed which can change the output


    # return median value - int
user_input = [1, 2, 3, 4, 5, 6, 7, 8]
print(median(user_input))

# Write a Python function called duplicates that takes a list of integers
# and returns a list of all the integers that appear more than once
# in the input list. The output list should be in ascending order.
# For example, if the input list is [1, 2, 3, 2, 4, 3, 5, 6, 7, 7],
# the function should return [2, 3, 7].

# Exam 1:45pm
# no pickle


def duplicates(list_int):
    new_list = []
    new_dict = {}
    for i in list_int:
        if i in new_dict:
            new_dict[i] += 1
            new_list.append(i)
        new_dict[i] = 1
    return new_list


input_list = [1, 2, 3, 2, 4, 3, 5, 6, 7, 7]
print(duplicates(input_list))

# Write a Python function called quicksort that takes a list of integers
# and returns a new list that contains the same elements in ascending order,
# using the quicksort algorithm.
# You can assume that the input list is not empty.
# For example, if the input list is [3, 7, 1, 9, 2, 5, 8, 4, 6],
# the function should return [1, 2, 3, 4, 5, 6, 7, 8, 9].


def quicksort(list_int):
    pivot = list_int[0]
    n = list_int
    pass

# Write a Python function called `gcd that takes two positive integer arguments a and b
# and returns their greatest common divisor (GCD) using the Euclidean algorithm.
# For example, if a is 30 and b` is 18, the function should return 6.


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


print(gcd(30, 18))

# Write a Python function called binary_search that takes a sorted list of integers
# and a target integer, and returns the index of the target if it appears in the list,
# or -1 otherwise. You can assume that the input list is sorted in ascending order.
# For example, if the input list is [1, 2, 3, 4, 5, 6, 7, 8, 9] and the target is 5,
# the function should return 4.


def binary_search(sort_list, target_int):
    L = 0
    R = len(sort_list) - 1
    while L <= R:
        mid = (L+R) // 2
        if sort_list[mid] == target_int:
            return mid
        elif sort_list[mid] <= target_int:
            L += 1
        else:
            R += 1
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(my_list, 5))


# Write a Python function called fibonacci that takes a non-negative integer argument n
# and returns the nth Fibonacci number using recursion. The Fibonacci sequence is defined as follows:
# the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding numbers.
# For example, if n is 7, the function should return 13 (since the 7th Fibonacci number is 13)
# 0,1,1,2,3,5,8,13,21,...
def fibonacci(n):
    if n < 0:
        return f"{n} is a negative integer!"
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


f = fibonacci(4)
print(f)
# unpacking for elements is going to be similar to one to one values * will be return a list:
