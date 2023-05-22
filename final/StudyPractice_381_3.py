# # generator problem

# # a student ID is a CAPITAL letter, followed by four digits (none of which can be over a 7), followed by a letter
# # write a program using generator functions which can provide student ID's
# # example: D3021F

def gen_letter():
    letter = ord('A')
    while True:
        yield chr(letter)
        letter += 1
        if letter > ord('Z'):
            letter = ord('A')


def gen_numbers():
    current_num = 0
    while True:
        oct_num = int(oct(current_num)[2:])
        if '8' not in str(oct_num):
            yield f"{oct_num:04}"
            current_num += 1
            if (oct_num == 7777):
                current_num = 0


g_n = gen_numbers()
g_l = gen_letter()
g_l_2 = gen_letter()
for _ in range(4095):
    number_1 = next(g_n)
    for _ in range(8):
        letter_2 = next(g_l_2)
        for _ in range(26):
            letter_1 = next(g_l)
            print(letter_1 + str(number_1) + letter_2)

# def generate_number_ids():
#   current_num = 0
#   while (True):
#     octal_number = int(oct(current_num)[2:])
#     yield (f"{octal_number:04}")
#     current_num += 1
#     if (octal_number == 7777):
#       current_num = 0


# def generate_letter_ids():
#   # A = 65
#   curr_ascii = ord('A')
#   while(True):
#     yield chr(curr_ascii)
#     curr_ascii += 1
#     if curr_ascii == 91:
#       curr_ascii = 65


# number_generator = generate_number_ids()
# # for x in range(5000):
# #   print(next(number_generator))

# first_letter_generator = generate_letter_ids()
# second_letter_generator = generate_letter_ids()


# for x in range(4095):
#   number = next(number_generator)
#   for y in range(26):
#     second_letter = next(first_letter_generator)
#     for z in range(26):
#       first_letter = next(second_letter_generator)
#       print(first_letter + number + second_letter)

# def letter():
#   current=65
#   while True:
#     yield chr(current)
#     current+=1

# def number():
#   current=0
#   while True:
#     yield current
#     current+=1

# h=letter()
# for a in range(26):
#   i=next(h)
#   j=number()
#   for b in range(8):
#     k=next(j)
#     l=number()
#     for c in range(8):
#       m=next(l)
#       n=number()
#       for d in range(8):
#         o=next(n)
#         p=number()
#         for d in range(8):
#           q=next(p)
#           r=letter()
#           for a in range(26):
#             s=next(r)
#             print(i+str(k)+str(m)+str(o)+str(q)+s)

# deep copy vs shallow copy

# video1584155929

# from copy import deepcopy, copy

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# old_list = [a,b,c]
# new_list = old_list.copy()

# new_list[0][1] = 10
# print(a)

# # j = deepcopy(new_list)
# # j[0] = 4
# # print(new_list)

# from copy import deepcopy

# a = [1,2,3]
# b = a
# b[1] = 4
# # line 1
# # print(a[1])

# c = a.copy()
# c.append(3)
# print(a)

# d = [a,b,c]
# e = deepcopy(d)

# e[0].append("hello")
# print(d[0])
# print(a)
