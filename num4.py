import random

x = []

for i in range(10):
    x.append(random.randint(0, 100))

summ = 0
proizv = 1

for i in x:
    summ += i
    proizv *= i

print(summ,'\n', proizv)