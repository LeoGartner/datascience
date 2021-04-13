#

numero = int(input("Digite um número: "))

a = (numero % 5) + (numero % 3)

if a == 0:
	print ("Fizzbuzz")

else:
	print (numero)