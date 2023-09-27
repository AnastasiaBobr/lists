import random

n = int(input('Введите число: '))

x = [random.randint(0, 100) for _ in range(10)]

print(x)

if n in x:
        print(x.index(n))
else:
        print('-1')