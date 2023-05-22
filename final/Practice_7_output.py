# Find out the output:
# def example(a, *b, **c):
#     print(type(a), type(b), type(c))
#     print(a, b[2], c, sep='\n')
#     print(len(c), list(c.items()))
#     g = list(c.items())
#     c[g[1]] = 'Hello'
#     print(c.items())
#     print(type(c.items()))
#     d = [i for i in c.keys()]
#     print(c[d[1]])
#     print()
#     z = list(c)
#     print(c[list(c)[2]])
#     print()
#     for i in iter(c):
#         print(i)


# example('abc', 1, 2, 3, x=10, y=20, z=30)


# def example_2(a, *b, **c):
#     print(type(a), type(b), type(c))
#     print(a, b[1], c, sep='\n')
#     print(len(c), list(c.items()))
#     g = list(c.items())
#     c[g[0]] = 32
#     print(c.items())
#     print(type(c.items()))
#     d = [i for i in c.keys()]
#     print(c[d[0]])
#     print()
#     z = list(c)
#     print(c[list(c)[0]])
#     print()
#     for i in iter(c):
#         print(i)


# example_2(5, 1, 2, 3, x=10, y=20)

def example_3(a, *b, **c):
    print(type(a), type(b), type(c))  # 1
    print(a, b[0], c, sep='\n')  # 2
    print(len(c), list(c.items()))  # 3
    g = list(c.items())
    c[g[0]] = "New Value"  # type: ignore
    print(c.items())  # 4
    print(type(c.items()))  # 5
    d = [i for i in c.keys()]
    print(c[d[0]])  # 6
    print()  # 7
    z = list(c)
    print(c[list(c)[0]])  # 8
    print()  # 9
    for i in iter(c):
        print(i)  # 10


example_3(True, "Hello", 1, 2, x=10, y=20, z=30, w=40)


# def example_4(a, *b, **c):
#     print(type(a), type(b), type(c))
#     print(a, b[0], c, sep='\n')
#     print(len(c), list(c.items()))
#     g = list(c.items())
#     c[g[0]] = [1, 2, 3]
#     print(c.items())
#     print(type(c.items()))
#     d = [i for i in c.keys()]
#     print(c[d[0]])
#     print()
#     z = list(c)
#     print(c[list(c)[0]])
#     print()
#     for i in iter(c):
#         print(i)


# example_4('xyz', 1, 'abc', 2, x=10, y=20)


# def example(*args, **kwargs):
#     print(f"Arguments: {args}")  # = (1, 2, 3)
#     print(f"Keyword Arguments: {kwargs}")  # {x='hello', y='world'}
#     print(f"Total Arguments: {len(args) + len(kwargs)}")  # = 5
#     print()


# example(1, 2, 3, x='hello', y='world')


# def example(*args, **kwargs):
#     print(f"Arguments: {args}")
#     print(f"Keyword Arguments: {kwargs}")
#     print(f"Total Arguments: {len(args) + len(kwargs)}")
#     print()

# example('a', 'b', 'c', x=1, y=2, z=3)


# def example_5(a, *b, **c):
#     print(type(a), type(b), type(c))
#     print(a)
#     print(b[0])
#     print(c)
#     print(len(c), list(c.items()))
#     g = list(c.items())
#     c[g[0]] = "New Value"  # type: ignore
#     print(c.items())
#     print(type(c.items()))
#     d = [i for i in c.keys()]
#     print(c[d[0]])
#     print()
#     z = list(c)
#     print(c[list(c)[0]])
#     print()
#     for i in iter(c):
#         print(i)


# example_5("Hello", 1, 2, x=10, y=20, z=30)


# def example_6(a, *b, **c):
#     print(type(a), type(b), type(c))
#     print(a)
#     print(b[0])
#     print(c)
#     print(len(c), list(c.items()))
#     g = list(c.items())
#     c[g[0]] = [1, 2, 3]  # type: ignore
#     print(c.items())
#     print(type(c.items()))
#     d = [i for i in c.keys()]
#     print(c[d[0]])
#     print()
#     z = list(c)
#     print(c[list(c)[0]])
#     print()
#     for i in iter(c):
#         print(i)

# example_6('xyz', 1, 'abc', 2, x=10, y=20)
