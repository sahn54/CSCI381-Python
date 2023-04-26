for i in range(1, 5):
    for j in range(1, 5):
        if (i+j) % 2 == 0:
            break
        print('(', i, ',', j, ')', end='')
    print()
# this loop will skip a line

# don't run
