#
#Definir variáveis a, b e c

a = int(input("Digite a: "))
b = int(input("Digite b: "))
c = int(input("Digite c: "))

#Definir e calcular Delta

delta = int(b**2 - (4 * a * c))

#Testar Delta == 0, Delta > 0

import math

if delta == 0:
   x1 = -b / (2 * a)
   x2 = x1

else:
   x1 = (-b + math.sqrt(delta)) / (2 * a) 
   x2 = (-b - math.sqrt(delta)) / (2 * a)

# If Delta = 0, tem 1 solução para X
# If Delta > 0, tem 2 soluções para X
# If Delta < 0, não admite solução real. 

print(" A solução é x1 = ", x1, "e x2 = ", x2)


