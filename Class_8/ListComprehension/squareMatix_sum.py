import random

my_list = [[1, 2, 3], [12, 45]]

for i in range(1, 100):
    random_value = random.randint(1, 100)
    my_list.append(random_value)  # type: ignore


def sum_col(x, i):
    return sum([x[j][i] for j in range(len(x))])


print(sum_col(my_list, 1))
