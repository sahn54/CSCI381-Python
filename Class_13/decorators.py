# Learn about decorators
# This is the decorator function


def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished calling function {func.__name__}")
        return result
    return wrapper


# This says that the log_function_call function will “decorate” the add function


@log_function_call
def add_numbers(x, y):
    return x + y


# Now you call add_number(2, 3)
result = add_numbers(2, 3)
print(result)


# Another way to write it
add_numbers = log_function_call(add_numbers(2, 3))
result = add_numbers(2, 3)
print(result)


# problems here
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """ wrapper"""
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper


@my_decorator
def my_function(x, y):
    """ my func"""
    return x+y


z = my_function(2, 3)
print(z, my_function.__name__)
print(z, my_function.__doc__)
