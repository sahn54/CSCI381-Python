# Merge Sort

# def merge(arr_1, arr_2):
#     arr_3 = []
#     while len(arr_1) > 0 and len(arr_2) > 0:
#         if arr_1[0] > arr_2[0]:
#             arr_3.append(arr_2[0])
#             arr_2.remove(arr_2[0])
#         else:
#             arr_3.append(arr_1[0])
#             arr_1.remove(arr_1[0])
#     while len(arr_1) > 0:
#         arr_3.append(arr_1[0])
#         arr_1.remove(arr_1[0])
#     while len(arr_2) > 0:
#         arr_3.append(arr_2[0])
#         arr_2.remove(arr_2[0])
#     return arr_3


# def merge_sort(arr_1):
#     if n == 1:
#         return arr_1
#     array_one = arr_1[0]... arr_1[n/2]
#     array_two - a[n/2+1] ... arr_1[n]

#     array_one = merge_sort(array_one)
#     array_two = merge_sort(array_two)

#     return merge(array_one, array_two)

def betterMerge_sort(arr):
    # check if the list is empty
    if len(arr) > 1:
        mid = (len(arr)) // 2
        left = arr[:mid]
        right = arr[mid:]

        betterMerge_sort(left)
        betterMerge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Code to print the list


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# Test code

arr = [12, 11, 13, 5, 6, 7]
print("Given array is", end="\n")
printList(arr)
# mergeSort(arr)
betterMerge_sort(arr)
print("Sorted array is: ", end="\n")
printList(arr)

# This code is contributed by Mayank Khanna


def merge_sort_ex(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_ex(left)
        merge_sort_ex(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


new_list = [1, 23, 34, 5, 45, 2, 24, 21]

print(new_list)
print(merge_sort_ex(new_list))
