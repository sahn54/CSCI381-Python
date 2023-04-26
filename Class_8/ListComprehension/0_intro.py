# a = [x ** 2 for x in range(1, 101) if x % 2 == 0]
# print(a)


# a = []
# for x in range(1, 101):
#     if x % 2 == 0:
#         a.append(x)
# print(a)

def dot(x, y):

    num = sum([x[i] * y[i] for i in range(len(x))])
    return num


x = [96, 89, 84]
y = [10, 11, 12]
print(dot(x, y))


def get_row(x, i):
    return [x[i][j] for j in range(len(x))]


print(get_row(3, 5))
