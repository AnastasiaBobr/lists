n = int(input('Введите число:'))
x = []
x2 = []

for i in range(n):
        
    number = int(input('Число:'))
        
    x.append(number)

for i in range(len(x)):
        
    if i % 2 != 0:
            
        x2.append(i)


for i in x2:
  
    x.pop(i)

print(x)