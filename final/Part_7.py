# Generators

# Write a function f with the following behavior: each time f is called it returns the next positive even
# integer. So, the first time it is called it returns 2, the next time 4 and so on.

num = 0


def f():
    global num
    num += 2
    return num


# print(f())
# print(f())
# print(f())


# Now do it without global variables

# def f_without_G(num):
#     value = 0
#     while value < num:
#         yield value
#         value += 2
#     return value


# even_num = f_without_G(11)
# for i in even_num:
#     print(i)

# Now do it counting down


# def countdown(num):
#     print("count down from", num)
#     while num > 0:
#         yield num
#         num -= 1


# going_down = countdown(15)
# for i in going_down:
#     print("T_minus", i)

# Write a generator that will yield the “next” prime number each time that it’s called


# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True


# def prime_generator():
#     value = 2
#     while True:
#         if is_prime(value):
#             yield value
#         value += 1


# pg = prime_generator()

# print(next(pg))
# print(next(pg))
# print(next(pg))
# print(next(pg))
# print(next(pg))


# Write a generator that will yield the “next” leap year each time that it’s called.

def is_leap_year(n):
    if n % 4 == 0 and (n % 100 != 0 or n % 400 == 0):
        return True
    else:
        return False


def leap_year_generator():
    year = 1995
    print("Starting year", year)
    while True:
        if is_leap_year(year):
            yield year
        year += 1


# l_p = leap_year_generator()
# print(next(l_p))
# print(next(l_p))
# print(next(l_p))
# print(next(l_p))

# Using a generator, create a dictionary such that d[i] is mapped to the ith prime number.


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def generator_for_dictionary():
    value = 0
    key = 0
    d = {}
    while True:
        if is_prime(value):
            key += 1
            d[key] = value
            yield d
        value += 1


g_f_d = generator_for_dictionary()
print(next(g_f_d))
print(next(g_f_d))
print(next(g_f_d))
print(next(g_f_d))
# Can you also do this with a dictionary comprehension?


def is_prime_y():
    n = 2
    while True:
        con = True
        for i in range(2, (n // 2) + 1):
            if n % i == 0:
                con = False
                break
        if con:
            yield n
        n += 1


dic_con_prime = is_prime_y()
d = {key: next(dic_con_prime) for key in range(1, 101)}
print(d)


# Write a generator get_oct() that will produce the next octal number each time it’s called. The value
# should be a string, so that when the octal number 20 is produced (this is the octal representation for
# the decimal 16) the generator will return ‘20’.
def get_oct():
    current_num = 1
    while True:
        yield str(oct(current_num))[2::]
        current_num += 1


decimal = 20
oct_t = get_oct()
list_of_number_in_oct = {i: next(oct_t) for i in range(1, decimal+1)}


print(list_of_number_in_oct)


# Write a generator that produces “serial numbers” according to the following rule: a serial number is a
# ten-character string where


# Write a generator that monitors a device that periodically sends either a 1 or a 0. The generator keeps
# track of the number of zeros between receiving a 1. They call that number the gap. Each time a value
# is received the generator yields the gap.

def generator(n_list):
    count = 0
    for i in n_list:
        if i == 1:
            yield count
            count = 0
        else:
            count += 1
    yield count


runs = [1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1]
# output= [0, 0, 1, 0, 3, 0, 0, 0, 1, 2, 0]
g = generator(runs)
new_list = [i for i in g]
print(new_list)


# Referring to the problem above. Imagine that the sequence of 1s and 0s represents the state of some
# security sensor, 1 if available, zero if not. If the gap between 0s exceeds some user defined n, the
# generator should return a warning and return. Write the modified generator.
