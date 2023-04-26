# integers_list = []

# s = int(sum(range(1, 11)))

# for num in s:
#     integers_list.append(num)


# print(f"My list is {integers_list}")
sum = 0

integers_list = []
for i in range(1, 11):
    integers_list.append(i)
    sum += i
print(f"1. my list is {integers_list} Total: {sum}")


sum1 = 0

integers_list = []
for i in range(0, 11, 2):
    integers_list.append(i)
    sum1 += i
print(f"2. my even list is {integers_list} Total: {sum1}")

sum2 = 0

integers_list = []
for i in range(1, 11, 2):
    integers_list.append(i)
    sum2 += i
print(f"3. my odd list is {integers_list} Total: {sum2}")


sum3 = 0

num10_list = list(range(1, 11))
for i in range(0, len(num10_list), 2):
    sum3 += num10_list[i]
print(f"4. my even list is {num10_list} and the sum is {sum3} ")


sum4 = 0

num10_list = list(range(1, 11))
for i in range(1, len(num10_list), 2):
    sum4 += num10_list[i]
print(f"my odd list is {num10_list} and the sum is {sum4} ")
