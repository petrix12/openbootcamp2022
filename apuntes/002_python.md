# Python
+ [Resolución de ejercios](https://github.com/Open-Bootcamp/ResolucionEjercicios/tree/main/Python)


## Introducción a Python
### Vídeo sesión 1
+ [Python página oficial](https://www.python.org/downloads/windows)
+ [Python de ActiveState](https://www.activestate.com/products/python)
+ [PyGTK - para interfaz gráfica de usuario](https://pypi.org/project/PyGTK)
+ [PyQt - para interfaz gráfica de usuario](https://pypi.org/project/PyQt5)
+ [PyQt - para interfaz gráfica de usuario](https://riverbankcomputing.com/software/pyqt/download)
+ [wxPython - para interfaz gráfica de usuario](https://www.wxpython.org)
+ [tkinter - para interfaz gráfica de usuario - muy popular](https://docs.python.org/3/library/tkinter.html)
+ [django - framework de backend](https://www.djangoproject.com)
+ [Flask - framework de backend](https://flask.palletsprojects.com/en/2.1.x)
+ [psycopg - para acceder a bases de datos](https://www.psycopg.org)
+ [PyGreSQL - para acceder a bases de datos](http://www.pygresql.org)
+ [PyMongo - para acceder a bases de datos](https://pymongo.readthedocs.io/en/stable)
+ [pysqlite3 - para acceder a bases de datos](https://pypi.org/project/pysqlite3)
+ [NumPy - para cálculo científico](https://numpy.org)
+ [SciPy - para cálculo científico](https://scipy.org)
+ [pandas - libreria de análisis de datos](https://pandas.pydata.org)

### Ejercicio 1
+ Desde la consola de python, debes de imprimir las siguientes cadenas de texto:
    + Hola, soy [tu_nombre]
    + Estoy empezando el curso de python
    + Espero aprender mucho
+ Tienes que subir capturas de pantalla en una carpeta comprimida zip.
+ **Resolción**:
    ```
    >>> nombre = "Pedro"
    >>> print("Hola, soy " + nombre)
    Hola, soy Pedro
    >>> print("Estoy empezando el curso de python")
    Estoy empezando el curso de python
    >>> print("Espero aprender mucho")
    Espero aprender mucho
    ```

### Ejercicio 2
+ Desde la consola de python almacena la cadena “Hola mundo!” en una variable y muéstrala.
+ Tienes que subir capturas de pantalla en una carpeta comprimida zip.
+ **Resolción**:
    ```
    >>> cadena = "Hola mundo!"
    >>> print(cadena)
    Hola mundo!
    ```


## El intérprete de Python
### Vídeo sesión 2
+ Obtener versión de Python instalada:
    + $ python --version
    + $ python2 --version
    + $ python3 --version
+ Pip: comando para instalar librerias de Python a nivel de sistema, para ver la versión:
    + $ pip --version
    + $ pip2 --version
    + $ pip3 --version
+ Instalar y desintalar SciPy con pip:
    + $ pip install scipy
    + $ pip uninstall scipy
+ Obtener la ayuda de SciPy:
    + $ help(scipy)
+ Página oficial de Pip:
    + https://pypi.org
+ Ver las librerias instaladas:
    + $ pip list
+ Ejercicio para ilustrar problemas con las versiones de paquetes instalados con pip:
    + Crear proyecto **demo1** en **proyectos\002\demo1**.
    + Crear archivo de dependencias **proyectos\002\demo1\requirements.txt**:
        ```txt
        flask==0.12.1
        ```
    + En la raíz del proyecto **demo1**:
        + $ pip install -r requirements.txt
    + Crear proyecto **demo2** en **proyectos\002\demo2**.
    + Crear archivo de dependencias **proyectos\002\demo2\requirements.txt**:
        ```txt
        flask>=1.0.0
        ```
    + En la raíz del proyecto **demo2**:
        + $ pip install -r requirements.txt
+ **Entorno virtual virtualenv**:
    + Crear proyecto **demo3** en **proyectos\002\demo3**.
    + En la raíz del proyecto **demo3**:
        + $ virtualenv venv .
    + Para ejecutar entorno virtual:
        + $ source demo3/venv/bin/activate
    + Para salir del entorno virtual:
        + $ deactivate
    + sss
+ **Entorno virtual pyenv**: existe una alternativa al virtualenv que es pyenv, pero este no funciona en Windows.
+ **Entorno virtual pipenv**:
    + Instalar pipenv:
        + $ pip install pipenv
    + Crear proyecto **demo4** en **proyectos\002\demo4**.
    + En la raíz del proyecto **demo4** crear entorno virtual:
        + $ pipenv shell
    + Para salir y volver a entrar al entorno virtual:
        + $ exit
        + $ pipenv shell

### Ejercicio 1
+ En este ejercicio tendrás que crear una variable a la cual asignarás una cadena de texto y la imprimirás por consola, a su vez, tendrás que imprimir también el tipo de la variable por consola.
+ Este ejercicio lo tienes que realizar desde la consola de python y subir capturas de pantalla en una carpeta comprimida zip.
+ **Resolción**:
    ```
    >>> texto = "Una cádena de texto"
    >>> print("Texto: " + texto + ". Tipo: " + str(type(texto))) 
    Texto: Una cádena de texto. Tipo: <class 'str'>
    ```

### Ejercicio 2
+ Modifica la variable del anterior ejercicio en la consola de python y después muestrala por consola para ver la modificación de la variable.
+ Tienes que subir capturas de pantalla en una carpeta comprimida zip.
+ **Resolción**:
    ```
    >>> texto = "cádena de texto modificada" 
    >>> print("Texto: " + texto)
    Texto: cádena de texto modificada
    ```


## Introducción a los tipos de objetos
### Vídeo sesión 3
+ Ejemplo de comando python para obtener la dirección de memoria:
    ```py
    >>> a=7
    >>> id(a)
    2790000689584
    ```
+ Ejemplo tuplas:
    + tupla = ('1', 255, 'hola', 5.8)
    + Elemento: tupla[i]
    + No son modificables
+ Ejemplo listas:
    + lista = ['1', 255, 'hola', 5.8]
    + Elemento: lista[i]
    + Añadir elemento: lista.append('otro elemento')
    + Remover un elemento: lista.remove('hola')
    + Convertir lista en string: ' '.join(lista)
+ Ejemplo de diccionario:
    + diccionario = { "clave1": "valor1", "clave2": "valor2" }
    + Elemento: diccionario['clave2']
    + Eliminar elemento: diccionario.pop('clave2')
        + También sirve: diccionario.del('clave2')
+ Ejemplo de conjunto:
    + conjunto = { 1, 2, 3 }
    + En los conjuntos no puede haber elementos duplicados a diferencias de las listas.
    + Unión de conjuntos: conjunto1 | conjunto2
    + Intersección de conjuntos: conjunto1 & conjunto2
    + Diferencia de conjuntos: conjunto1 - conjunto2
    + Diferencia simétrica de conjuntos: conjunto1 ^ conjunto2
+ Ejemplo de tipos de datos:
    + numero = 7
    + string = 'Esto es una cádena de texto'
    + booleano = True
    + flotante = 3.33
    + lista = ['a', 1, '7', 'k']
    + tupla = ('a', 1, '7', 'k')
    + diccionario = { "clave1": "valor1", "clave2": "valor2" }
    + conjunto = { 1, 2, 3 }
+ Ejemplo de métodos en string:
    ```
    >>> texto = "Hola, est es un texto"
    >>> texto.capitalize()
    'Hola, est es un texto'
    >>> texto = "hola, esto es un texto"
    >>> texto.capitalize()               
    'Hola, esto es un texto'
    >>> texto.title()
    'Hola, Esto Es Un Texto'
    >>> texto.lower()
    'hola, esto es un texto'
    >>> texto.upper()
    'HOLA, ESTO ES UN TEXTO'
    >>> texto.replace('a', 'o')
    'holo, esto es un texto'
    >>> texto.find("esto")
    6
    >>> texto.split()
    ['hola,', 'esto', 'es', 'un', 'texto']
    >>> texto.split(',') 
    ['hola', ' esto es un texto']
    ```
+ Obtener toda la ayuda para trabajar con string:
    + help(str)
+ Operadores:
    + Asignación: =
    + Aritméticos: +, -, *, /, //, %, **
    + Set: &=, |=, ^=, >>=, <<=
    + Bit: &, |, ^, ~, <<, >>
    + Comparación: ==, !=, >, >=, <, <=
    + Identidad: is, is not
    + Membresia: in, not in
+ Ejemplo de algunas funciones de la libreria math:

    ```
    >>> import math
    >>> math.pi
    3.141592653589793
    >>> math.floor(5.9)
    5
    >>> math.ceil(5.9)
    6
    >>> math.ceil(5.3)
    6
    >>> help(math)
    ```


### Ejercicio 1
+ Para este ejercicio tenéis que crear en la consola de python variables que representen los siguientes datos de un contacto:
    + Nombre
    + Apellidos
    + Edad
    + Email
    + Teléfono
    + Casado (verdadero o falso)
    + Con Hijos (verdadero o falso)
    + Lista de amigos
    + Películas vistas (diccionario con clave y valor. El valor será el título de la película)
+ Una vez hayas creado todas las variables, muéstralas por consola haciendo uso de la función print().
+ Tienes que subir capturas de pantalla en una carpeta comprimida zip.
+ **Resolción**:
    ```
    >>> Nombre = "Josemaría"
    >>> Apellidos = "Pérez Soler" 
    >>> Edad = 33
    >>> Email = "correo47@gmail.com"
    >>> Casado = False
    >>> Hijos = True
    >>> Amigos = ['Carlos', 'Gerardo', 'Marco'] 
    >>> Peliculas = {"clave1": "Terminator", "clave2": "Rambo", "clave3": "Spiderman"}
    >>> print(Nombre)
    Josemaría
    >>> print(Apellidos) 
    Pérez Soler
    >>> print(Edad)
    33
    >>> print(Email)
    correo47@gmail.com
    >>> print(Casado) 
    False
    >>> print(Hijos)  
    True
    >>> print(Amigos) 
    ['Carlos', 'Gerardo', 'Marco']
    >>> print(Peliculas)
    {'clave1': 'Terminator', 'clave2': 'Rambo', 'clave3': 'Spiderman'}
    ```

### Ejercicio 2
+ Escribe un programa en la consola de python que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, e imprima por pantalla la frase "Tu índice de masa corporal es" (donde es el índice de masa corporal calculado redondeado con dos decimales). Tienes que subir capturas de pantalla en una carpeta comprimida zip.
+ **Resolción**:
    ```
    >>> peso = input("Peso (en kg)")
    Peso (en kg)3
    >>> peso = input("Peso (en kg) = ")
    Peso (en kg) = 100
    >>> estatura = input("Estatura (en metros) = ")
    Estatura (en metros) = 1.83
    >>> indice = round(float(peso)/float(estatura)**2,2)
    >>> print("Tu índice de masa corporal es: " + str(indice))
    Tu índice de masa corporal es: 29.86
    ```

## Control de flujo
### Vídeo sesión 4
+ Uso de **Y**: **and** o **&&**.
+ Uso de **O**: **or** o **||**.
+ Uso de **O exclusivo**: **xor** o **^**.
+ Sentencia de control **if**:
    ```py
    if condicion1:
        bloque_acciones1
    elif condicion2:
        bloque_acciones2
    elif condicion3:
        bloque_acciones3
    elif condicion4:
        bloque_acciones4
    else:
        bloque_acciones5
    ```    
+ Sentencia de control **while**:
    ```py
    while condicion:
        bloque_acciones
    ```
    + Interruptores: **break** (interrumpe el bucle) y **continue** (interrumpe la iteración).
+ Sentencia de control **for**:
    ```py
    for valor in cosa:
        bloque_acciones
    ```
    + Cosa puede ser:
        + lista: [....]
        + tupla: (....)
        + rango de valores: range(12) o range(3, 7)
    + Interruptores: **break** (interrumpe el bucle) y **continue** (interrumpe la iteración).
    + Ejemplo de **for** con **else**:
        ```py
        lista = ["hola", "adios", "café"]
        for palabra in lista:
            if palabra == "café":
                print("Hay café")
                break
        else:
            print("No hay café")
        ```
        + **Nota**: el **else** se dispara si no se ejecuta el **break**.
+ Ejemplo de uso de **in** y **not in**:
    ```py
    # in
    lista = ["hola", "adios", "café"]
    if "café" in lista:
        print("Hay café")
    if "café" not in lista:
        print("No hay café")
    ```
+ Ordenar lista
    ```py
    lista = [1, 7, 3, 2, 5]
    # Orden asc
    listaOrdenada1 = sorted(lista)
    # Orden desc
    listaOrdenada2 = sorted(lista, reverse = True)
    ```
    + **Nota**: cuando la lista son caracteres se ordenan según el código ASCII.
+ Sentencia de control **match**:
    ```py
    match valor:
        case 1:
            bloque_acciones1
        case 2:
            bloque_acciones2
    ```
+ Ejemplo de uso de **pass**:
    ```py
    lista = ["hola", "adios", "café"]
    for palabra in lista:
        pass
    ```
    + **Nota**: el **pass** evita que se genere un error de sintaxis cuando aún no se tiene implementado el cuerpo del **for**.

### Ejercicio 1
+ Escribe un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
+ **Resolción**:
    ```py
    edad = int(input("¿Cuál es tu edad?: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    ```

### Ejercicio 2
+ Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
+ Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]
+ **Resolción**:
    ```py
    numero_inicial = 2
    numero_final = 8
    for numero in range(numero_inicial, numero_final + 1):
        if(numero % 2 == 0):
            print(numero," es par")
    ```

### Ejercicio 3
+ Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso.
+ **Resolción**:
    ```py
    for numero in range(0, 100):
        print("Número: ", 100 - numero)
    ```



    ```py
    ≡
    ≡
    ```


## Funciones
4 lecciones
1h3min
Vídeo sesión 5
48min
Ejercicio 1
5min
Ejercicio 2
5min
Ejercicio 3
5min
6
Clases y objetos
3 lecciones
1h 11min
Vídeo sesión 6
1h1min
Ejercicio 1
5min
Ejercicio 2
5min
7
Módulos: ejecutando módulos como scripts
3 lecciones
1h 17min
Vídeo sesión 7
1h7min
Ejercicio 1
5min
Ejercicio 2
5min
8
Entrada y salida
3 lecciones
1h 18min
Vídeo sesión 8
1h8min
Ejercicio 1
5min
Ejercicio 2
5min
9
Introducción a la biblioteca estándar de Python y funciones Built-in
3 lecciones
49min
Vídeo sesión 9
39min
Ejercicio 1
5min
Ejercicio 2
5min
10
GUI
3 lecciones
1h 31min
Vídeo sesión 10
1h 21min
Ejercicio 1
5min
Ejercicio 2
5min
11
Bases de datos
2 lecciones
48min
Vídeo sesión 11
43min
Ejercicio 1
5min
12
Introducción a Django
2 lecciones
1h6min
Vídeo sesión 12
1h1min
Ejercicio 1