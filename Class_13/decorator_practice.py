import functools
calldict = {}  # calldict is the dictionary


def countcalls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = f"{func.__name__}"
        value = calldict.get(name, 0)
        calldict[name] = value + 1
        result = func(*args, **kwargs)

        return result
    return wrapper


# @countcalls  # countcalls is the decorator
# def add(x, y):
#     return x+y


# @countcalls
# def mult(x, y):
#     return x*y


@countcalls(calldict)  # countcalls is the decorator
def add(x, y):
    return x+y


@countcalls(calldict)
def mult(x, y):
    return x*y


z = add(2, 3)
print(calldict)
z = add(2, 3)
print(calldict)
z = mult(2, 3)
print(calldict)
