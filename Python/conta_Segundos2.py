#

segundos = input ("Por favor, entre com o número de segundos que deseja converter:")
#
dias = int(segundos) // 86400
horas = (int(segundos) % 86400) // 3600
minutos = ((int(segundos) % 3600) // 60)
segundos = ((int(segundos) % 3600) % 60)
#
print (dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")
