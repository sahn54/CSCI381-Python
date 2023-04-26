from math import sqrt
from random import random

count = 0
for i in range(1000000):
    x = random()
    y = random()
    if sqrt(x * x + y * y) < 1:
        count += 1
print(4*(count/1000000))
