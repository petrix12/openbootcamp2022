import sqlite3
#from getpass import getpass
import getpass

def main():
    crear_usuario(4, 'prueba3', '12345678')

def main2():
    username = input("Usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Longin correcto")
    else:
        print("Longin incorrecto")

def verifica_credenciales(username, password):
    conn = sqlite3.connect('bdatos.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar:", query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    print("Data:", type(data))

    cursor.close()
    conn.close()

    if data == None:
        return False
    return True

def crear_usuario(id, username, password):
    conn = sqlite3.connect('bdatos.db', isolation_level=None)
    cursor = conn.cursor()

    # query = f"INSERT INTO users('id', 'username', 'password') VALUES ({id}, '{username}', '{password}')"
    query = '''INSERT INTO users(id, username, password) VALUES (?, ?, ?)'''
    print("Query a ejecutar:", query)
    rows = cursor.execute(query, (id, username, password))
    print("Data:", type(rows))

    # conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main':
    main()




"""
conn = sqlite3.connect('bdatos.db')

cursor = conn.cursor()
rows = cursor.execute('SELECT * FROM users')

for row in rows:
    print(row)

cursor.close()
conn.close()
"""