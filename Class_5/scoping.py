# LEGB
# sum = 0
# for i in range(5):
#     sum += i
# print(sum)

# sum is a built-in that accepts any appropriate iterable
# print(sum([10, 20, 30]))

# TypeError: 'int' object is not callable

# Why do we get this weird error? - Python defines Locals first
# Because in addition to the sum function defined in built-ins, we have now defined a global variable named
# sum. And because globals come before built-ins in Python’s search path, Python discovers that sum is an
# integer and refuses to invoke it.


# def foo(x):
#     def bar(y):
#         return x * y
#     return bar


# f = foo(10)
# print(f(20))
#  when foo(10) -> x becomes 10 , bar is returned
# f is now a function, when defining f it is technically bar()


# First, Python looks for x locally, in the local function bar.
# Next, Python looks for x in the enclosing function foo.
# If x were not in foo, then Python would continue looking at the global level.
# And if x were not a global variable, then Python would look in the built-ins namespace.


# In Python 3, though, we have the nonlocal keyword. This keyword tells
# Python: “Any assignment we do to this variable should go to the outer function, not to a (new) local
# variable”;


def foo():
    call_counter = 0

    def bar(y):
        nonlocal call_counter
        call_counter += 1
        return f'y = {y}, call_counter = {call_counter}'
    return bar


b = foo()
for i in range(10, 100, 10):
    print(b(i))

# foo returns bar


# Default parameter values are evaluated once when the function is first defined, not each time the
# function is called. This often leads to surprising behavior if mutable objects are used as a default since
# they will retain the change and the original default won’t be the “default” anymore:
def f(x, items=[]):
    items.append(x)
    return items


f(1)  # returns [1]
f(2)  # returns [1, 2]
f(3)  # returns [1, 2, 3]

# The takeaway: Never use a mutable value, such as a list or dictionary, as a parameter’s default value. You
# shouldn’t do so because default values are stored and reused across calls to the function. This means that if you
# modify the default value in one call, that modification will be visible in the next call.

# So, as a general practice, to avoid such surprises, only use immutable objects for default argument
# values—numbers, strings, Booleans, None, and so on.
