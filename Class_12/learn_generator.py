

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

y = map(lambda i: i**2, x)

print(next(y))
print(y.__next__())
print("Next value")

while True:
    try:
        value = next(y)
        print(value)
    except StopIteration:
        print("Done")
        break

# when getting the iterator from a range
# iter()
# .__iter__()
# next(iter(x))


def gen(n):
    for i in range(n):
        yield i


for i in gen(5):
    print(i)
