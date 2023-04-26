import test


# def find_hack(arr):

#     scores_for_each_grade = {
#         "A": 30,
#         "B": 20,
#         "C": 10,
#         "D": 5
#     }
#     hacked_names = []

#     for person in arr:
#         name = person[0]
#         given_points = person[1]
#         grades = person[2]
#         points = 0
#         count_bonus = 0
#         b_above = False
#         for grade in grades:
#             points += scores_for_each_grade[grade]
#             if grade == "A" or grade == "B":
#                 count_bonus += 1
#                 b_above = True
#             else:
#                 count_bonus = 0
#                 b_above = False
#         if count_bonus >= 5 and b_above:
#             points += 20

#             points = min(points, 200)

#         if points != given_points:
#             hacked_names.append(name)

#     return hacked_names  # hacked entries # hacked entries


# array = [
#     ["name1", 150, ["B", "A", "A", "C", "A", "A"]],
#     ["name2", 120, ["B", "A", "A", "A"]],
#     ["name3", 160, ["B", "A", "A", "A", "A"]],
#     ["name4", 140, ["B", "A", "A", "C", "A"]]
# ]

# find_hack(array)


# https://youtu.be/SgUwPDT9tEs?t=215

original_dict = {'a': [1, 2, 3], 'b': 2, 'c': 3}
copy_dict = original_dict.copy()
# print(original_dict)  # {'a': 1, 'b': 2, 'c': 3}
# print(copy_dict)  # {'a': 1, 'b': 2, 'c': 3}
# copy_dict['d'] = 4
# print(copy_dict)
# print(original_dict)
copy_dict['a'].append(4)
print(copy_dict)
print(original_dict)
