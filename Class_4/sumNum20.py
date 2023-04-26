# Problem:
# Generate and print all numbers between 1 and 1000 such that the sum of the digits equals 20

for i in range(1, 1001):
    digit_sum = sum(int(d) for d in str(i))
    if digit_sum == 7:
        print(i, end=",")
