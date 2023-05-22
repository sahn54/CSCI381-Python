# Algorithm
# The bubble sort algorithm works as follows

# Step 1) Get the total number of elements. Get the total number of items in the given list

# Step 2) Determine the number of outer passes (n – 1) to be done. Its length is list minus one

# Step 3) Perform inner passes (n – 1) times for outer pass 1. Get the first element value and compare it with the second value. If the second value is less than the first value, then swap the positions

# Step 4) Repeat step 3 passes until you reach the outer pass (n – 1). Get the next element in the list then repeat the process that was performed in step 3 until all the values have been placed in their correct ascending order.

# Step 5) Return the result when all passes have been done. Return the results of the sorted list

# Step 6) Optimize Algorithm

# Optimization is done using the following steps

# Step 1) Create a flag variable that monitors if any swapping has occurred in the inner loop

# Step 2) If the values have swapped positions, continue to the next iteration

# Step 3) If the benefits have not swapped positions, terminate the inner loop, and continue with the outer loop.

import timeit

my_list = [21, 6, 9, 33, 3]


def bubble_sort(the_list):
    n = len(the_list)
    for _ in range(n-1):
        is_swapping = False
        for j in range(n-1):
            if the_list[j] > the_list[j+1]:
                temp = the_list[j]
                the_list[j] = the_list[j+1]
                the_list[j+1] = temp
                is_swapping = True
        if is_swapping == False:
            break
    return the_list


# duration = timeit.timeit(bubble_sort(the_list=my_list), number=1)

print(bubble_sort(my_list))
# print("Execution time:", f"{duration:.4f} seconds")
