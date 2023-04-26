def bubble_Sort(a):
    for i in range(len(a)):
        sorted = True
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[i]
                sorted = False
        if sorted == True:
            return


a = [44, 32, 12, 22, 6, 7, 77, 2, 34]
bubble_Sort(a)
print(a)
