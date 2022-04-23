class Vehiculo:
    color = "azul"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 150
    cilindrada = 4

coche = Coche()
print("Color:", coche.color)
print("Ruedas:", coche.ruedas)
print("Puertas:", coche.puertas)
print("Velocidad:", coche.velocidad)
print("Cilindrada:", coche.cilindrada)