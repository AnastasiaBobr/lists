import random

x = []

for i in range(10):
        
    x.append(random.randint(0, 10))

print(x)

for i in x:
        
    if x.count(i) > 1:
     
      print(i)