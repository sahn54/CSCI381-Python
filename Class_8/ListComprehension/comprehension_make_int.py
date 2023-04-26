# def make_int(x:str) -> list:
#      return [int(i) for i in c]

def matrix_add(x, y):
    l = []
    for i in range(len(x)):
        l.append([x[i][j] + y[i][j] for j in range(len(x))])
    return l


a = [[3, 4, 5], [5, 12, 6], [9, 7, 21]]
b = [[13, 14, 15], [25, 132, 26], [29, 27, 121]]
print(matrix_add(x=a, y=b))


def matrix_product(x, y):
    l = []
    for i in range(len(x)):
        l.append([x[i][j] * y[i][j] for j in range(len(x))])
    return l


print(matrix_product(a, b))
