for i in range(1, 5):
    for j in range(1, 5):
        if (i+j) % 2 == 0:
            continue
        print('(', i, ',', j, ')', end='')
    print()

# the continue does not prints and goes back to the j loop and when the condition is not even it prints
# So it only prints when the j loop is an even
