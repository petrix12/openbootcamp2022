import time

horas = time.strftime('%H') 
minutos = time.strftime('%M') 

if int(horas) >= 19:
	print ("Hora de ir a casa") 
else:
	print ("Faltan {} horas y {} minutos para ir a casa".format(18- int(horas), 59-int(minutos)))