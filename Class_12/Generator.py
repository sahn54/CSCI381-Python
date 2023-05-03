# In Python, a generator is a function that returns an iterator that produces a sequence of values when iterated over.

# Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
# def generator_name(arg):
#     # statements
#     yield something


# def my_generator(n):

#     # initialize counter
#     value = 0

#     # loop until counter is less than n
#     while value < n:

#         # produce the current value of the counter
#         yield value

#         # increment the counter
#         value += 1

# # iterate over the generator object produced by my_generator
# for value in my_generator(3):

#     # print each value produced by generator
#     print(value)


# Write a function f with the following behavior: each time f is called it returns the next positive even
# integer. So, the first time it is called it returns 2, the next time 4 and so on.
# def f():
#     global x
#     x += 2
#     return x


# def without_f(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 2


# gen_num = without_f(10)
# for num in gen_num:
#     print(num)

# When a generator function is called, it returns a generator object that can be iterated over, just like
# a list, but it generates values only when requested.


# you go to the yield where you left off.


# Write a generator that will yield the “next” prime number each time that it’s called.

def is_prime(number):
    if number < 2:  # Numbers less than 2 are not prime
        return False

    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True


def next_prime_1(num):
    return (value for value in range(num + 1, 2*num + 1) if is_prime(value))


gen_prime = next_prime_1(0)
for num in gen_prime:
    print(num)
    if num >= 30:
        break


# Write a generator that will yield the "next" leap year each time that it's called

def check_leap_year(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))


def next_year(years):
    current_year = 4
    while current_year < years:
        if check_leap_year(current_year):
            yield current_year
        current_year += 4


c = next_year(10)
for i in c:
    print(i)

# Using a generator, create a dictionary such that d[i] is mapped to the ith prime number.


def next_prime_2():
    value = 2
    while True:
        if is_prime(value):
            yield value
        value += 1


my_dictionary = {}
gene = next_prime_2()
for num in range(100):
    my_dictionary[num] = next(gene)
print(my_dictionary)

# Can you also do this with a dictionary comprehension?
# {1:2, 2:3, 3:5... } Key the number from 1 to n and value is the prime number
gene_2 = next_prime_2()
my_dictionary_c = {num: next(gene) for num in range(100)}

print(my_dictionary_c)


# def is_prime(num):
#     return [x for x in range(2, num) if all(x % y != 0 for y in range(2, x))]


# def dict_prime():
#     value = 2
#     while True:
#         while not is_prime(value):
#             value += 1
#         yield value
#         value += 1


# n = dict_prime()
# prime = {x: next(n) for x in n}
# print(prime)


# Problem:
# Write a generator get_oct() that will produce the next octal number each time it’s called. The value
# should be a string, so that when the octal number 20 is produced (this is the octal representation for
# the decimal 16) the generator will return ‘20’.

def get_oct():
    value = 0
    while True:
        yield oct(value)[2::]
        value += 1


oct_num = get_oct()

# num_dict = dict()
# for n in range(100+1):
#     num_dict[n] = next(oct_num)
# print(num_dict)

num_dict_1 = {n: next(oct_num) for n in range(100)}
print(num_dict_1)


def even_numbers1():
    num = 0
    yield num
    num += 2


try:
    even = even_numbers1()
    for w in range(10):
        print(next(even))
except StopIteration:
    print("There is Stop Iteration, require a yield")
# Stop Iteration - ask Chat GPT
