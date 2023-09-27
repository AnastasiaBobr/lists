import random

x = []

for i in range(10):
    x.append(random.randint(0, 100))

print((x), '\n' , max(x))