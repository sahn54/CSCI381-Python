a = []
for i in range(4):
    a.append(4*[0])

print(a)

b = []
for i in range(4):
    b.extend(4*[0])

print(f"extending: {b}")


c = 3*3*[[0]]
print(c)
