# Review:
# print() has parameters:
# Value: object to the printed. * indicates that there may be more than one object
# Sep: objects are separated by sep. Default value: ' '
# end: is printed at last
# file: must be  be an object with write(string) method. If omitted, sys.stdout will be used which prints objects on the screen.
# flush: if True, the stream is forcibly flushed.
# Default value: False


# x = 1
# y = 2
# z = x+y
# print(x, y, z)


# In C++
# 1. code segments
# 2. run time stack - automatics variables
# ex: int a;
# 3. Heap

# a = new
# pointer int*

# Python
# everything is an object
# the variables does not holds the values like c++
# Frames is in the run time stack
# Object is in the heap

# type() shows what type of data is the object
# x+y -> x._add_y

# List
# x = [1,2,3]
# len(x)

# expression - somthing that can be evlauate , it has a value and somtimes has a side effect
# the side effect for x = 5 is that x is has a new value.
# the value is  x - as a side effect

# Extended assignment
# Page 32: frames are sharing object in python, so there is thing called reference count.
# when reference count is 0 then the garbage collection will return the objects.

# unpacking or Assignment to tuples
# frames points to their own obejcts x,y,z = 1,2,3

# Augmented Assignment : += , -= etc

# walrus assignment
# print(a:=9)
# a = 9


# look on eval()
# look on repr()
# look on fstring


# print('Hello \nMy name is Sung')

# name
# name = input("Please enter your name: ")
# print('Hello ' + name + ' !')


first = input("Please enter the first number: ")
second = input("Please enter the second number: ")
result = int(first) + int(second)
print("The sum of " + first + " and " + second + " is " + str(result))
result = int(first) - int(second)
print("The difference of " + first + " and " + second + " is " + str(result))
result = int(first) * int(second)
print("The product of " + first + " and " + second + " is " + str(result))
result = int(first) // int(second)
print("The integer division of " + first +
      " and " + second + " is " + str(result))
result = int(first) / int(second)
print("The float division of " + first +
      " and " + second + " is " + str(result))
result = int(first) % int(second)
print("The remainder of " + first + " and " + second + " is " + str(result))
