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
	print("a raiz desta equação é", x1)

else:
	x1 = (-b + math.sqrt(delta)) / (2 * a) 
	x2 = (-b - math.sqrt(delta)) / (2 * a)
	if x1 > x2:
		print("as raízes da equação são", x2, "e", x1)
	else:
		print("as raízes da equação são", x1, "e", x2)

if delta < 0:
	print("esta equação não possui raízes reais")



# If Delta = 0, tem 1 solução para X
# If Delta > 0, tem 2 soluções para X
# If Delta < 0, não admite solução real. 



