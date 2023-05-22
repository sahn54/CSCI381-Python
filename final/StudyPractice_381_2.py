# the idea of a geneartor is to save space
# when we want to iterate through a lot of values,
# instead of generating the whole list of all values, storing the list, and iterating through the list
# we can use a generator which knows start, stop, step

# range(start, stop, step)


# yield perfect squares: write a function that yields the next perfect square
# reminder: perfect squares are 1,4,9,16,25,36,etc

# def perfect_square_generator():
#   starting_num = 1
#   while(True):
#     yield starting_num ** 2
#     starting_num += 1


# get_perfect_squares = perfect_square_generator()
# get_perfect_squares_two = perfect_square_generator()
# print(next(get_perfect_squares))
# print(next(get_perfect_squares))
# print(next(get_perfect_squares))
# print(next(get_perfect_squares_two))


# def z(a,*b,**c): # recall the order
#   # b only gets the parameters that were not already "collected" by other variables
#   # in this case, a already took care of 12
#   # all that's left for b is 3,4,5
#   # when we get element 1, it's gonna be value of 4

#   # print(type(a),type(b),type(c))
#   # print(a,b[1],c,sep='\n')
#   # print(len(c),list(c.items()))
#   g=list(c.items())
#   c[g[0]]=156

#   #g : [('k', 87), ('l', 19)]

#   #g[0] = ('k', 87)
#   #c[('k', 87)] = 156

#   # print(c.items())
#   # print (type(c.items()))
#   # d=[i for i in c.keys()]
#   # # print(c[d[0]])
#   # # print()
#   # z=list(c)
#   # print(z)
# print(c[list(c)[0]])
#   # print()
#   # for i in iter(c):
#   #   print(i)


# z(12,3,4,5,k=87,l=19)


# j = {"first" : 1, "second" : 2}
# for key, value in j.items():
#   print(key)
#   print(value)


# def return_sum(*a):
#   total_sum = 0
#   for x in a:
#     total_sum += x
#   return total_sum

# print(return_sum(1,2,3,4,5))


# generator yield question


# what does it mean that tuples are immutable

# the key for a dictionary must be immutable because to find the value
# in a dictionary requires performing a mathematical function on the key
# you have to be able to count on the fact that the function executed on the key
# will always get you back the same value, which is an index to go look for the value


# a, *body, c, d = range(5)

# print(body)

# a, b, *rest = range(3)
# a, b, *rest = range(2)

# def fun(a, b, c, d, *rest):
#   return a, b, c, d, rest

# print(fun(*[1, 2], 3, *range(4, 7)))

# j = {*range(4), 4, *(5,6,7)}
# print(j)


# ----------------------------------------------------My notes----------------------------------------------
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


# def prime_generator(n):
#     value = 0
#     while n > 0:
#         if is_prime(value):
#             yield value
#             n -= 1
#         value += 1


# f = prime_generator(10)
# for _ in range(10):
#     print(next(f))

# def generator_dict_prime():
#     index = 0
#     value = 0
#     dict_prime = {}
    # while True:
    #     if is_prime(value):
    #         dict_prime[index] = value
    #         yield dict_prime
    #         index += 1
    #     value += 1
#     while True:
#       yield {index : value for index in range(10) if is_prime(value)}
#       index += 1

# g = generator_dict_prime()
# for i in range(10):
#     print(next(g))


# "serial numbers"
def get_oct():
    value = 0
    counter = 0
    while True:
        yield {counter: value}
        counter += 1
        value = oct(counter)[2::]


g_o = get_oct()
for _ in range(20):
    print(next(g_o))
