class Motor:
    tipo = "Diesel"

class Ventanas:
    cantidad = 5

class Ruedas:
    cantidad = 4

class Carroceria:
    ventanas = Ventanas()
    ruedas = Ruedas()

class Coche:
    motor = Motor()
    carroceria = Carroceria()

coche = Coche()
print("Motor: ", coche.motor.tipo)
print("Ventanas: ", coche.carroceria.ventanas.cantidad)
print("Ruedas: ", coche.carroceria.ruedas.cantidad)