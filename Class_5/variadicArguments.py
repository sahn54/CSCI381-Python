# 3.Variadic Arguments
# A function can accept a variable number of arguments if an asterisk (*) is used as a prefix on the last
# parameter name. For example:
# *args - positional arguments ***Tuple like a list that is not i
# **kwargs - keyword argument
def product(first, *args):
    result = first
    for x in args:  # note args is an iterable. Its type is <class 'tuple'>.
        result = result * x
    return result


product(10, 20)  # -> 200
product(2, 3, 4, 5)  # -> 120

# In this case, all of the extra arguments are placed into the args variable as a tuple. You can then work with
# the arguments using the standard sequence operations—iteration, slicing, unpacking, and so on.
