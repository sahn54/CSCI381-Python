# Selection Sort

# Step 1) Get the value of n which is the total size of the array

# Step 2) Partition the list into sorted and unsorted sections. The sorted section is initially empty while the unsorted section contains the entire list

# Step 3) Pick the minimum value from the unpartitioned section and placed it into the sorted section.

# Step 4) Repeat the process (n – 1) times until all of the elements in the list have been sorted.

my_list = [21, 6, 9, 33, 3]


def selection_sort(get_list):
    n = len(get_list)
    for i in range(n - 1):
        min_value_index = i
        for j in range(i+1, n):
            if get_list[j] < get_list[min_value_index]:
                # we point to the new min_value index (we didn't swap anything yet)
                min_value_index = j
        if min_value_index != i:
            temp = get_list[i]
            get_list[i] = get_list[min_value_index]
            get_list[min_value_index] = temp
    return get_list


print(selection_sort(my_list))
