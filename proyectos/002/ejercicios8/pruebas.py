import pickle

class Clase:
    nombre = None
    precio = None

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Guardar objeto en archivo (serialización)
objeto = Clase("Petrix", 12)
f = open('proyectos/002/ejercicios8/datos.bin', 'wb')
pickle.dump(objeto, f)
f.close()

# Recuperar objeto desde un archivo (deserialización)
g = open('proyectos/002/ejercicios8/datos.bin', 'rb')
objetoRecuperado = pickle.load(g)
g.close()
print(type(objetoRecuperado))