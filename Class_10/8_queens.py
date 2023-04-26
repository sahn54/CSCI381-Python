# the board is 8 queens
# input a queen
from itertools import permutations

candidates = permutations([0, 1, 2, 3, 4, 5, 6, 7])


def diagonal_treat(q):
    for i in range(8):
        for j in range(i+1, 8):
            horizontal_length = j-i
            vertical_length = abs(q[j] - q[i])
            if horizontal_length == vertical_length:
                return False

    return True

# concept is that if the


count = 0
for p in candidates:
    if diagonal_treat(p):
        continue
    count += 1
    print("Solution number", count, ': ', p)
    print()


# row test

# col test

# permutation
# diagonal conflict
# qsubx c and qsuby
