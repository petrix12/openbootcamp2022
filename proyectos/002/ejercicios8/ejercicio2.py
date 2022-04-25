import pickle

class Vehiculo:
    puertas = None
    ruedas = None
    motor = None

    def __init__(self, puertas, ruedas, motor):
        self.puertas = puertas
        self.ruedas = ruedas
        self.motor = motor

# Guardar objeto en archivo (serialización)
vehiculo = Vehiculo(5, 4, "Diesel")
f = open('vehiculos.bin', 'wb')
pickle.dump(vehiculo, f)
f.close()

# Recuperar objeto desde un archivo (deserialización)
g = open('vehiculos.bin', 'rb')
vehiculoRecuperado = pickle.load(g)
g.close()
print(type(vehiculoRecuperado))