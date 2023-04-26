i = 1
j = 1
while i < 5:
    while j < 5:
        if (i+j) % 2 == 0:
            break
        print('(', i, ',', j, ')', end='')
        j += 1
    print()
    i += 1
# Do not run
# does not print anything,

# The reason why it is printing this output is because
# when it breaks it prints blank print()
# when it does not breaks it prints normally
