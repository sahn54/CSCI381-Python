n = int(input("Enter number: "))
i = 1
sum = 0
while i <= n:
    if i % 2 == 1:
        sum += i
    i += 1
print(sum)
