import sqlite3
import getpass
from datetime import datetime

def crearTabla():
    # Mejora: agregar código que verifique si la tabla existe.
    conn = sqlite3.connect('ejercicio1.db', isolation_level=None)
    cursor = conn.cursor()

    query = "CREATE TABLE alumnos(id INTEGER PRIMARY KEY, nombre TEXT NOT NULL, apellido TEXT NOT NULL)"
    cursor.execute(query)

    cursor.close()
    conn.close()

def crearAlumnos(id, nombre, apellido):
    # Mejora: agregar código que genere id unicos.
    conn = sqlite3.connect('ejercicio1.db', isolation_level=None)
    cursor = conn.cursor()

    query = f"INSERT INTO alumnos(id, nombre, apellido) VALUES ({id}, '{nombre}', '{apellido}')"
    cursor.execute(query)

    cursor.close()
    conn.close()

def buscarAlumno(nombre):
    conn = sqlite3.connect('ejercicio1.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}'"
    rows = cursor.execute(query)

    for row in rows:
        print(row)

    cursor.close()
    conn.close()

crearTabla()
for i in range(0, 9):
    crearAlumnos(i, f'Nombre{i}', f'Apellido{i}')

nombre = input("Nombre: ")
buscarAlumno(nombre)

# sqlite3 ejercicio1.db
# .tables
# SELECT * FROM alumnos;