import random

# my_list = []
# for i in range(10):
#     i = random.randint(1, 10)
#     my_list.append(i)
# print(my_list)

# PRINT THE LIST AND THE MAXIMUM INTEGER IN THE LIST
# my_list = []
# for i in range(10):
#     i = random.randint(1, 10)
#     my_list.append(i)
# print((my_list))
# print(f"my maximum integer is {max(my_list)}")


# my2_list = []
# counter = 0
# while counter < 10:
#     i = random.randint(1, 10)
#     my2_list.append(i)
#     if i > max:
#         i == max
#     counter += 1
# print((my2_list))
# print(f"my maximum integer is {max}")

def findMax():
    position = 0
    my3_list = []
    for i in range(10):
        num = random.randint(1, 10)
        my3_list.append(num)
        position = i
    print((my3_list))
    print(
        f"My maximum integer is {max(my3_list)} and the index is {my3_list.index(max(my3_list))}")
    print(
        f"my maximum integer is {max(my3_list)} and the index is {position}")


findMax()
