a = [4, 2, 7, 1, 45, 23]


def select_sort(listOfNum):
    for i in range(len(listOfNum)-1):
        y = listOfNum[i:]  # [i:] starting point and up to next index
        position = listOfNum.index(min(y), i, len(listOfNum))
        listOfNum[i], listOfNum[position] = listOfNum[position], listOfNum[i]


select_sort(a)
print(a)
