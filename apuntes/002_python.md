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

## Funciones
### Vídeo sesión 5
1. Estructura de una función:
    ```py
    def funcionx():
        pass
    ```
2. Ejemplo de una función:
    ```py
    def suma(a, b):
        print(a + b)
    ```
3. Ejemplo para modificar una variable global dentro de una función:
    ```py
    numero = 12

    def funcion(a, b):
        global numero
        numero = 7
    ```
4. Ejemplo de función con parámetros opcionales:
    ```py
    def suma(a = 1, b = 2, c = 3):
        print(a + b + c)
    
    suma()
    suma(4, 5)
    suma(4, 5, 6)
    suma(c = 7)
    suma(c = 7, a = 2, b = 8)
    ```
5. Ejemplo de función con parámetros variables:
    ```py
    def suma(*args):
        resultado = 0
        for arg in args:
            resultado += arg
        print(resultado)
    
    
    suma(4, 5, 6)
    ```
6. Ejemplo de función que recibe un diccionario como parámetro:
    ```py
    def suma(**kwargs):
        print(kwargs)
        for key, value in kwargs.items():
            print(key, "=", value)
        if 'coche' in kwargs and kwargs['coche'] == 'bonito':
            return "Coche bonito"
    
    # Los paramétros llegan como un diccionario a la función
    suma(viviendo = "piso", coche = "rojo")
    ```
    ```py
    def sumador(**kwargs):
        inicial = kwargs['inicial'] if 'inicial' in kwargs else 0
        final = kwargs['final'] if 'final' in kwargs else inicial

        resultado = 0
        for i in range(inicial, final + 1):
            resutlado += i
        
        return resultado

    print(sumador(inicial = 15, final = 30))
    ```
7. Ejemplo de función que retorna una tupla:
    ```py
    def operaciones(a, b):
        return a + b, a - b, a * b, a / c
    
    suma, resta, multi, divi = suma(7, 3)
    res = sumar(7, 3)
    ```
8. Ejemplo de función anónima (función asignada a una variable):
    ```py
    anonima = lambda: print("hola")
    anonima()
    ```
    + Con parámetro:
    ```py
    anonima = lambda nombre: print("hola", nombre)
    anonima("Petrix")
    ```
    + Con multiples parámetros:
    ```py
    anonima = lambda nombre, apellido: print("hola", nombre, apellido)
    anonima("César", "Pérez")
    ```
    + Otro ejemplo:
    ```py
    anonima = lambda x: x*x
    anonima(3)
    ```

### Ejercicio 1
+ Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
+ **Resolción**:
    ```py
    def areaTriangulo(altura, base):
        return base * altura / 2

    def areaCirculo(radio):
        return 3.14159265359 * radio * radio

    print("Área de un triángulo (h = 2, b = 3) = ", areaTriangulo(2, 3))
    print("Área de un círculo (r = 3) = ", areaCirculo(3))
    ```
### Ejercicio 2
+ Escribe una función que pueda decirte si un número (número entero) es primo o no.
+ **Resolción**:
    ```py
    def esPrimo(numero):
        bPrimo = True
        for i in range(2, numero // 2 + 1):
            if (numero % i == 0):
                bPrimo = False
                break
        return bPrimo

    numero = 15
    print("El número", numero, "es primo" if esPrimo(numero) else "no es primo")
    ```
### Ejercicio 3
+ Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.
+ **Resolción**:
    ```py
    def esBisiesto(anho):
        if ((anho % 4 == 0) and not (anho % 100 == 0)):
            return True
        elif((anho % 4 == 0) and (anho % 400 == 0)):
            return True
        return False

    anho = 2002
    print("El año", anho, "es bisiesto" if esBisiesto(anho) else "no es bisiesto")
    ```

## Clases y objetos
### Vídeo sesión 6
1. Definición de una clase:
    ```py
    class Clase:
        propiedad = False
        def metodo(self):
            self.propiedad = True

    objeto = Clase()
    print(objeto.propiedad)
    objeto.metodo()
    print(objeto.propiedad)
    ```
2. Ejemplo clase estática:
    ```py
    class Estatica:
        numero = 1
        def incrementa():
            Estatica.numero += 1

    print(Estatica.numero)
    Estatica.incrementa()
    print(Estatica.numero)
    ```
3. Ejemplo de herencia:
    ```py
    class ClasePadre:
        propiedadPadre = False
        def metodoPadre(self):
            self.propiedadPadre = True

    class ClaseHija(ClasePadre):
        propiedadHija = False
        def metodoHija(self):
            self.propiedadHija = True

    objeto = ClaseHija()
    print(objeto.propiedadPadre)
    print(objeto.propiedadHija)
    objeto.metodoPadre()
    objeto.metodoHija()
    print(objeto.propiedadPadre)
    print(objeto.propiedadHija)
    ```
4. Ejemplo de constructor y destructor:
    ```py
    class Clase:
        propiedad = False

        def __init__(self):
            self.propiedad = True

        def __del__(self):
            self.propiedad = False
            print('Se ejecutó el destructor')
            
    objeto = Clase()
    print(objeto.propiedad)

    # forzar la ejecución del destructor
    del(objeto)

    ```
5. **Nota**: las clases en Python realmente son diccionarios.
6. Ejemplo de clase abstracta:
    ```py
    from abc import ABC, abstractmethod

    class Animal(ABC):
        @abstractmethod
        def sonido(self):
            pass

        def diHola(self):
            print("Hola")

    class Perro(Animal):
        def sonido(self):
            print("Guau")

    perro = Perro()
    perro.sonido()
    perro.diHola()
    ```
7. Ejemplo de clase de composición:
    ```py
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
    ```

### Ejercicio 1
+ En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
    + Color
    + Ruedas
    + Puertas
+ Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
    + Velocidad
    + Cilindrada
+ Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
+ **Resolción**:
    ```py
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
    ```

### Ejercicio 2
+ En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
+ **Resolción**:
    ```py
    class Alumno:
        nombre = None
        nota = None

        def setNombre(self, nombre):
            self.nombre = nombre

        def setNota(self, nota):
            self.nota = int(nota)

        def showResultados(self):
            print("Nombre:", self.nombre)
            print("Nota:", self.nota)
            print("APROBADO" if self.nota >= 16 else "REPROBADO")

    alumno = Alumno()
    alumno.setNombre(input("Nombre: "))
    alumno.setNota(input("Nota: "))
    alumno.showResultados()
    ```

## Módulos: ejecutando módulos como scripts
### Vídeo sesión 7
1. Ejemplo de creación de módulos:
    1. Crear módulo principal **proyectos\002\ejercicios7\modulos\main.py**:
        ```py
        import operaciones as op

        def main():
            res1 = op.suma(3, 7)
            operador = op.Operador()
            res2 = operador.multi(5, 12)
            print("Main: ", res1, res2)
            op.nombreModulo()

        if __name__ == '__main__':
            main()
        ```
    2. Crear módulo **proyectos\002\ejercicios7\modulos\operaciones.py**:
        ```py
        def suma(a, b):
            return a + b

        def resta(a, b):
            return a - b

        def nombreModulo():
            print(__name__)

        class Operador:
            def multi(self, a, b):
                return a * b
        ```
2. Ejemplo de creación de paquetes:
    1. Crear módulo principal **proyectos\002\ejercicios7\paquetes\main.py**:
        ```py
        from operaciones import suma
        import operaciones.resta

        def main():
            res1 = suma.suma(2, 7)
            res2 = operaciones.resta.resta(12, 7)
            print(res1, res2)

        if __name__ == '__main__':
            main()
        ```
    2. Crear módulo **proyectos\002\ejercicios7\paquetes\operaciones\\__init__.py**:
        ```py
        # archivo vacio
        ```
    3. Crear módulo **proyectos\002\ejercicios7\paquetes\operaciones\suma.py**:
        ```py
        def suma(a, b):
            return a + b
        ```
    4. Crear módulo **proyectos\002\ejercicios7\paquetes\operaciones\resta.py**:
        ```py
        def resta(a, b):
            return a - b
        ```  

### Ejercicio 1
+ En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.
+ Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
+ **Resolción**:
    + Crear módulo **operaciones.py**:
    ```py
    def suma(a, b):
        return a + b

    def resta(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b
    ```
    + Crear módulo principal **main.py**:
    ```py
    import operaciones as op

    def main():
        a = 12
        b = 7
        res_suma = op.sumar(a, b)
        res_resta = op.restar(a, b)
        res_multiplicacion = op.multiplicar(a, b)
        res_division = op.dividir(a, b)

        print("a = ", a, ", b = ", b)
        print("a + b = ", res_suma)
        print("a - b = ", res_resta)
        print("a * b = ", res_multiplicacion)
        print("a / b = ", res_division)

    if __name__ == '__main__':
        main()
    ```

### Ejercicio 2
+ En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
+ En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
+ **Resolción**:
    ```py
    import time

    horas = time.strftime('%H') 
    minutos = time.strftime('%M') 

    if int(horas) >= 19:
        print ("Hora de ir a casa") 
    else:
        print ("Faltan {} horas y {} minutos para ir a casa".format(18- int(horas), 59-int(minutos)))
    ```


## Entrada y salida
### Vídeo sesión 8
1. Formato de cádenas (Opción 1 - Forma antigua - Mala):
    ```py
    numero = 12
    texto = "Petrix"
    peso = 100.33

    print("Texto: %s" % texto)
    print("El %d es el número de %s, que pesa %.3f" % (numero, texto, peso))
    ```
2. Formato de cádenas (Opción 2 - Forma habitual - Fea):
    ```py
    numero = 12
    texto = "Petrix"
    peso = 100.33

    print("El {} es el número de {}, que pesa {}".format(numero, texto, peso))
    print("El {2} es el número de {0}, que pesa {1}".format(texto, peso, numero))
    print("El {n} es el número de {t}, que pesa {p}".format(n = numero, t = texto, p = peso))
    ```
3. Formato de cádenas (Opción 3 - Forma Moderna - Bonita):
    ```py
    numero = 12
    texto = "Petrix"
    peso = 100.33

    print(f"El {numero} es el número de {texto}, que pesa {peso}")
    print(f"El {numero + numero} es el número de {texto.upper()}, que pesa {peso}")

    salida = f"El {numero + numero} es el número de {texto.upper()}, que pesa {peso}"
    print(salida)
    ```
4. Ejemplo de manipulación de cádenas de texto:
    ```py
    class Clase:
        nombre = None
        precio = None

        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio

        def __str__(self):
            return f'Nombre: {self.nombre}, Precio: {self.precio}'
        
        def __repr__(self):
            return f'Clase({self.nombre}, {self.precio})'

        # Buenas prácticas: str para salidas informales y repr para salidas técnicas

    c1 = Clase("Petrix", 12)
    print(c1)
    print(str(c1))
    print(repr(c1))

    # Métodos de una cádena de texto
    import pprint
    pprint.pprint(dir(""))

    # Métodos comunes de una cádena de texto
    cadena = " eN un lugAr De la manCha "
    print(cadena.capitalize())
    print(cadena.title())
    print(cadena.lower())
    print(cadena.upper())
    print(cadena.strip())
    print(cadena.lstrip())
    print(cadena.rstrip())
    print(cadena.count('a'))
    print(cadena.lower().count('a'))
    print(cadena.upper().count('a'))
    print(cadena.isdigit())
    print(cadena.isalnum())
    print(cadena.isalpha())
    print(cadena.split())
    print(cadena.split('a'))
    print(cadena.startswith('un'))
    print(cadena.startswith(' eN'))
    print(cadena.endswith('un'))
    print(cadena.endswith('Cha '))
    ```
5. Ejemplo 1 de manipulación de archivos:
    ```py
    f = open('/archivo.txt', 'r')
    # Modos:
    # r: lectura
    # a: append
    # w: escritura
    # x: create
    # t: texto
    # b: binary
    # Caracter especial: +

    datos1 = f.readline()
    datos2 = f.read()
    f.close()

    # leer archivo línea a línea
    while datos2 != "":         # o while len(datos2) > 0:
        datos2 = f.readline()

    # para almacenar el archivo en una lista
    datos3 = f.readlines()

    print(datos1)
    print("----------")
    print(datos2)
    ```
6. Ejemplo 2 de manipulación de archivos:
    ```py
    # Solo funciona en Mac o Linux
    def main():
        usuarios = listarUsuarios()
        for usuario in usuarios:
            print(f'Usurario: {usuario}')

    def listarUsuarios():
        f = open('etc/passwd', 'r')
        datos = f.readlines()
        f.close()

        resultado = []
        for linea in datos:
            if linea[0] == '#':
                continue
            if linea[0] == '_':
                continue
            partes = linea.split(':')
            resultado.append(partes[0])
        
        return resultado

    if __name__ == '__main__':
        main()
    ```
7. Ejemplo 1 de escritura de archivos:
    ```py
    f = open('proyectos/002/ejercicios8/archivo.txt', 'w')

    f.write('datos1\n')
    f.write('datos2\n')
    f.write('datos3\n')

    f.close()

    g = open('proyectos/002/ejercicios8/archivo.txt', 'a')

    g.write('datos4\n')
    g.write('datos5\n')
    g.write('datos5\n')

    g.close()
    ```
8. Ejemplo 2 de escritura de archivos:
    ```py
    f = open('proyectos/002/ejercicios8/archivo.txt', 'w')

    lista = [
        'línea 1\n',
        'línea 2\n',
        'línea 3\n'
    ]

    f.writelines(lista)

    f.close()
    ```
9. Ejemplo de serialización:
    ```py
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
    ```

### Ejercicio 1
+ En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.
+ **Resolción**:
    ```py
    w = open('archivo.txt', 'w')
    w.write('datos linea 1\n')
    w.write('datos linea 2\n')
    w.close()

    a = open('archivo.txt', 'a')
    a.write('datos linea 3\n')
    a.write('datos linea 4\n')
    a.close()
    ```
### Ejercicio 2
+ En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
+ **Resolción**:
    ```py
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
    ```


## Introducción a la biblioteca estándar de Python y funciones Built-in
### Vídeo sesión 9
+ Biblioteca estándar de Python: https://docs.python.org/es/3/library/index.html
1. Ejemplo de programación multi hilo:
    ```py
    import _thread
    import time

    def horaActual(nombre_thread, tiempo_de_espera):
        count = 0
        while count < 5:
            time.sleep(tiempo_de_espera)
            count += 1
            print(f'hilo: {nombre_thread} - {time.ctime(time.time())}')

    _thread.start_new_thread(horaActual, ("thread 1", 1))
    _thread.start_new_thread(horaActual, ("thread 2", 2))

    print("He disparado los hilos")

    while True:
        time.sleep(0.1)
    ```
2. Ejemplo de la libreria logging:
    ```py
    import logging

    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)
    # logging.basicConfig(level=logging.WARNING)
    # logging.basicConfig(level=logging.ERROR)
    # logging.basicConfig(level=logging.CRITICAL)
    logging.debug("sto es un Debug")
    logging.info("sto es un Info")
    logging.warning("Esto es un Warning")
    logging.error("Esto es un Error")
    logging.critical("Esto es un Critical")
    ```
3. Ejemplo de la función filter:
    ```py
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def funcion(x):
        if x % 2 == 0:
            return True
        return False

    resultado1 = filter(funcion, numeros)
    resultado2 = filter(lambda x: x % 2 == 0, numeros)

    print(list(resultado1))
    print(list(resultado2))
    ```
4. Ejemplo de la función map:
    ```py
    def cuadrado(x):
        return x * x

    resultado1 = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    resultado2 = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    print(list(resultado1))
    print(list(resultado2))
    ```
5. Ejemplo del módulo reduce:
    ```py
    from functools import reduce

    def suma(a, b):
        print(f'a = {a}, b = {b}')
        return a + b

    res = reduce(suma, [1, 2, 3, 4])
    print("Prueba 1:", res)

    res = reduce(suma, [1, 2, 3])
    print("Prueba 2:", res)

    res = reduce(suma, [1, 2])
    print("Prueba 3:", res)

    res = reduce(suma, [1])
    print("Prueba 4:", res)
    ```
6. Ejemplo la función zip:
    ```py
    cursos = ['Laravel', 'Vue.js', 'Node.js', 'Elemenot de más']
    asistentes = [15, 20, 4]

    demo = zip(cursos, asistentes)
    print(list(demo))
    ```
7. Ejemplo de las funciones any y all:
    ```py
    listaA = [1 == 1, 2 ==2, 3 == 4]

    res = any(listaA)
    print(res)

    res = all(listaA)
    print(res)
    ```
8. Ejemplo la función round:
    ```py
    a = 5.5
    b = 5.4
    c = 5.6

    print(round(a))
    print(round(b))
    print(round(c))
    ```
9. Ejemplo las funciones min y max:
    ```py
    print(min(5, 4, 1, 3))
    print(max(5, 4, 1, 3))
    ```
10. Ejemplo la función pow:
    ```py
    print(pow(2, 3))
    print(2**3)
    ```
11. Ejemplo la función getpass:
    ```py
    from getpass import getpass

    usuario = input('Usuario: ')
    clave = getpass('Clave: ')

    print(usuario, clave)
    ```

### Ejercicio 1
+ Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
+ **Resolción**:
    ```py
    paisesString = input("Lista de países separados por comas: ")
    paises = [pais for pais in paisesString.split(",")]
    print("Lista ordenada:", ",".join(sorted(list(set(paises)))))
    ```

### Ejercicio 2
+ En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
+ **Resolción**:
    ```py
    from functools import reduce

    def impares(lista):
        return filter(lambda x: x % 2 != 0, lista)

    def sumatoria(lista):
        return reduce(lambda a, b: a + b, lista)

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Elementos impares: ", list(impares(lista)))
    print("Sumatoria de los elementos impares: ", sumatoria(list(impares(lista))))
    ```


## GUI
### Vídeo sesión 10
1. Ejemplo 1 de uso de tkinter con geometría pack:
    ```py
    import tkinter

    window = tkinter.Tk()

    label_saludo = tkinter.Label(window, text="Soluciones++ Hola", bg="yellow", fg="blue")
    label_saludo.pack(ipadx=50, ipady=50, fill='x')

    label_m1 = tkinter.Label(window, text="Mensaje 1", bg="grey", fg="blue")
    label_m1.pack(ipadx=30, ipady=30, expand=True)

    label_m2 = tkinter.Label(window, text="Mensaje 2", bg="green", fg="white")
    label_m2.pack(ipadx=30, ipady=30, side="left")

    label_m3 = tkinter.Label(window, text="Mensaje 3", bg="green", fg="white")
    label_m3.pack(ipadx=30, ipady=30, side="right")

    label_adios = tkinter.Label(window, text="Soluciones++ Chao", bg="red", fg="white")
    label_adios.pack(ipadx=50, ipady=100, fill='both', expand=True)

    window.mainloop()
    ```
2.  Ejemplo 2 de uso de tkinter con geometría pack:
    ```py
    import tkinter

    window = tkinter.Tk()

    label1 = tkinter.Label(window, text="Label1", bg="yellow", fg="blue")
    label1.pack(ipadx=45, ipady=15, expand=True)

    label2 = tkinter.Label(window, text="Label2", bg="purple", fg="white")
    label2.pack(ipadx=45, ipady=15, expand=True)

    label3 = tkinter.Label(window, text="Label3", bg="blue", fg="white")
    label3.pack(ipadx=45, ipady=15, expand=True)

    label4 = tkinter.Label(window, text="Label4", bg="red", fg="white")
    label4.pack(ipadx=15, ipady=15, side="left")

    label5 = tkinter.Label(window, text="Label5", bg="yellow", fg="black")
    label5.pack(ipadx=15, ipady=15, side="left")

    label6 = tkinter.Label(window, text="Label6", bg="green", fg="white")
    label6.pack(ipadx=15, ipady=15, side="right")

    window.mainloop()
    ```
3. Ejemplo de uso de tkinter con geometría grid:
    ```py
    import tkinter
    from tkinter import ttk

    window = tkinter.Tk()

    # Referencia para posicionar elementos
    # (0, 0)    (1, 0)  (2, 0)
    # (0, 1)    (1, 1)  (2, 1)
    # (0, 2)    (1, 2)  (2, 2)
    # (0, 3)    (1, 3)  (2, 3)

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    # Usuario
    user_label = ttk.Label(window, text="User:")
    user_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    user_entry = ttk.Entry(window)
    user_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

    # Password
    password_label = ttk.Label(window, text="Password:")
    password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

    password_entry = ttk.Entry(window, show="*")
    password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

    # Botón Login
    login_button = ttk.Button(window, text="Login")
    login_button.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)

    window.mainloop()
    ```
4. Ejemplo de uso de tkinter con geometría place:
    ```py
    import tkinter
    import random

    window = tkinter.Tk()

    colors = ['blue', 'green', 'yellow', 'orange', 'purple', 'black']

    for x in range(0, 10):
        color = random.randint(0, len(colors)-1)
        color2 = random.randint(0, len(colors)-1)
        label = tkinter.Label(window, text="etiqueta!", bg=colors[color], fg=colors[color2])
        label.place(x=random.randint(0, 100), y=random.randint(0, 100))

    label1 = tkinter.Label(window, text="Posicionamiento absoluto", bg="blue", fg="white")
    label1.place(x=10, y=50)

    label2 = tkinter.Label(window, text="posicionamiento relativo", bg="red", fg="yellow")
    label2.place(relx=0.1, rely=0.15, relwidth=0.5, anchor="ne")
    # label2.place(x=25, y=30)

    window.mainloop()
    ```
5. Ejemplo de uso de frame de ttk:
    ```py
    import sys
    import tkinter
    from tkinter import ttk

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    frame = ttk.Frame(window)
    label = ttk.Label(frame, text="Label en un Frame")
    label.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)
    frame.grid(column=0, row=0, sticky=tkinter.W)
    frame['relief'] ='sunken'

    window.mainloop()

    sys.exit(0)

    # Usuario
    user_label = ttk.Label(window, text="User:")
    user_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    user_entry = ttk.Entry(window)
    user_entry.grid(column=1, row=0, sticky=tkinter.E, padx=5, pady=5)

    # Password
    password_label = ttk.Label(window, text="Password:")
    password_label.grid(column=0, row=1, sticky=tkinter.W, padx=5, pady=5)

    password_entry = ttk.Entry(window, show="*")
    password_entry.grid(column=1, row=1, sticky=tkinter.E, padx=5, pady=5)

    # Botón Login
    login_button = ttk.Button(window, text="Login")
    login_button.grid(column=1, row=2, sticky=tkinter.E, padx=5, pady=5)

    window.mainloop()
    ```
6. Ejemplo de uso de listBox:
    ```py
    import tkinter

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    lista = ['Laravel', 'Vue.js', 'MongoDB', 'Reect.js', 'Node.js', 'Angular']
    lista_items = tkinter.StringVar(value=lista)
    listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
    listbox.grid(column=0, row=0, sticky=tkinter.W)

    window.mainloop()
    ```
7. Ejemplo de uso de radio button
    ```py
    import tkinter
    from tkinter import ttk

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    selected = tkinter.StringVar()
    r1 = ttk.Radiobutton(window, text="Radiobutton 1", value="1", variable=selected)
    r2 = ttk.Radiobutton(window, text="Radiobutton 2", value="2", variable=selected)
    r3 = ttk.Radiobutton(window, text="Radiobutton 3", value="3", variable=selected)

    r1.grid(column=0, row=1, pady=5, padx=5)
    r2.grid(column=0, row=2, pady=5, padx=5)
    r3.grid(column=0, row=3, pady=5, padx=5)

    window.mainloop()
    ```
8. Ejemplo de uso de check button
    ```py
    import tkinter
    from tkinter import ttk

    def funcion():
        print("Clicado")

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=3)

    selected = tkinter.StringVar()

    checkbox = ttk.Checkbutton(window, text="Check", variable=selected, command=funcion)

    checkbox.grid(column=0, row=0, pady=5, padx=5)

    window.mainloop()
    ```
9. Ejemplo de eventos
    ```py
    import tkinter
    from tkinter import ttk

    def click(event):
        print("Ocurrió el evento click")

    def dobleClick(event):
        print("Ocurrió el evento doble click")

    def salir(event):
        print("Chao")
        window.quit()


    window = tkinter.Tk()

    boton = tkinter.Button(window, text="Haz click")
    boton.pack()
    boton.bind('<Button-1>', click)
    boton.bind('<Double-1>', dobleClick)

    botonSalir = tkinter.Button(window, text="Salir")
    botonSalir.pack()
    botonSalir.bind('<Button-1>', salir)

    window.mainloop()
    ```
10. Ejemplo de uso de cuadro de diálogo para abrir archivos:
    ```py
    import tkinter
    from tkinter import filedialog

    window = tkinter.Tk()
    filename = filedialog.askopenfilename()
    window.mainloop()
    ```
11. Ejemplo de uso de cuadro de diálogo para abrir archivos:
    ```py
    import tkinter
    from tkinter import colorchooser

    window = tkinter.Tk()
    filename = colorchooser.askcolor(initialcolor='#ffffff')
    window.mainloop()
    ```

### Ejercicio 1
+ En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

Al principio no tiene que haber una opción seleccionada.
+ **Resolción**:
    ```py
    import tkinter
    from tkinter import ttk

    def OpcionSeleccionada():
        opcion_label = ttk.Label(window, text=seleccion.get())
        opcion_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    def Reiniciar():
        seleccion.set(None)
        opcion_label = ttk.Label(window, text="Seleccione una opción")
        opcion_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=4)

    opcion_label = ttk.Label(window, text="Seleccione una opción")
    opcion_label.grid(column=0, row=0, sticky=tkinter.W, padx=5, pady=5)

    seleccion = tkinter.StringVar()
    r1 = ttk.Radiobutton(window, text="Opción 1", value="Seleccionó la opción 1", variable=seleccion, command=OpcionSeleccionada)
    r2 = ttk.Radiobutton(window, text="Opción 2", value="Seleccionó la opción 2", variable=seleccion, command=OpcionSeleccionada)
    r3 = ttk.Radiobutton(window, text="Opción 3", value="Seleccionó la opción 3", variable=seleccion, command=OpcionSeleccionada)

    r1.grid(column=0, row=1, pady=5, padx=5)
    r2.grid(column=0, row=2, pady=5, padx=5)
    r3.grid(column=0, row=3, pady=5, padx=5)

    reset_button = ttk.Button(window, text="Reiniciar", command=Reiniciar)
    reset_button.grid(column=1, row=4, sticky=tkinter.E, padx=5, pady=5)

    window.mainloop()
    ```

### Ejercicio 2
+ En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
+ **Resolción**:
    ```py
    import tkinter
    from tkinter import ttk

    window = tkinter.Tk()

    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=10)

    lista = ['Laravel', 'Vue.js', 'MongoDB', 'Reect.js', 'Node.js', 'Angular', 'Python', 'JavaScript', 'MySQL']
    lista_items = tkinter.StringVar(value=lista)
    listbox = tkinter.Listbox(window, height=10, listvariable=lista_items)
    listbox.grid(column=0, row=0, sticky=tkinter.W)

    libre_label = ttk.Label(window, text="El texto que queráis")
    libre_label.grid(column=1, row=0, sticky=tkinter.W, padx=5, pady=5)

    window.mainloop()
    ```


## Bases de datos
### Vídeo sesión 11




    ```py
    ≡
    ≡
    ```





### Ejercicio 1
+ mmmm
+ **Resolción**:
    ```py
    ```


## Introducción a Django
### Vídeo sesión 12





    ```py
    ≡
    ≡
    ```





### Ejercicio 1
+ mmmm
+ **Resolción**:
    ```py
    ```