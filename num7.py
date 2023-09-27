import random

x = []

for i in range(10):
    x.append(random.randint(0, 100))

x2 = x.copy()

maxi = x.index(max(x))
mini = x.index(min(x))
x2[maxi] = min(x)
x2[mini] = max(x)

print(x)
print(x2)