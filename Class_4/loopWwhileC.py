i = 1
j = 1
while i < 5:
    while j < 5:
        if (i+j) % 2 == 0:
            continue
        print('(', i, ',', j, ')', end='')
    print()
# Do not run
# does not print anything,

# The reason is it is not printing is because, the value does not changes so it will loop continuously.
