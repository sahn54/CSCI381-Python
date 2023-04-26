# directories
portfolio = [
    ('ACME', 50, 92.34),
    ('IBM', 75, 102.25),
    ('PHP', 40, 74.50),
    ('IBM', 50, 124.75)
]  # list

# how you could count the total number of shares for each stock name in earlier data:
# Note IBM has two tuples


total_num = dict()
for name, amount, price in portfolio:
    total_num[name] = total_num.get(name,  0) + amount
print(total_num)


# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# x = thisdict.keys()

# print(x)

results = {n: n ** 2 for n in range(10)}
print(results)


k = int(input("Enter a number: "))
# create a list and put it in the dictionary


nth_prime = {n: k for n in range(1, k, 2) if k > 1 if k % 2 != 0}
print(nth_prime)


def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Now, you can call this function with any number of keyword arguments:
my_func(apple=3, banana=5, orange=2)


def z(a, *b, **c):  # recall the order
    print(type(a), type(b), type(c))  # int(12), tuple(3,4,5) ,dic(k=87,l=19)
    print(a, b[1], c, sep='\n')  # 12 , 4 , {'k', 'l'}
    print(len(c), list(c.items()))  # 2, [k:87,l:19]
    g = list(c.items())  # g = [k:87,l:19]
    c[g[0]] = 156  # type: ignore # type error
    print(c.items())  # {'k': 87, 'l':19}
    print(type(c.items()))  # dict
    d = [i for i in c.keys()]  # [k ,l]
    print(c[d[0]])  # 87
    print()  # space
    z = list(c)
    print(c[list(c)[0]])
    print()
    for i in iter(c):
        print(i)


z(12, 3, 4, 5, k=87, l=19)

# generators
# classes
# exceptions


# Write a function, signature(n) that and returns a string with same letters in lexicographic order.
# For example, signature(stop) ➔ opst

def signature(n):
    text = ""
    temp_list = sorted([i for i in n])
    for k in temp_list:
        text += k
    return text


print(signature("stop"))
