a = [64, 25, 12, 22, 11]


def mySort(listOfNum):
    for i in range(len(listOfNum)-1):
        y = listOfNum[i:]  # [i:] starting point and up to next index
        # (finditem , startposition, endpostion)
        position = listOfNum.index(min(y), i, len(listOfNum))
        listOfNum[i], listOfNum[position] = listOfNum[position], listOfNum[i]


mySort(a)
print(a)
