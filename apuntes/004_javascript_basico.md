# JavaScript Básico
+ **Instructor**: Gorka Villar
+ [Resolución de ejercios](https://github.com/Open-Bootcamp/ResolucionEjercicios/tree/main/Java%20B%C3%A1sico)
+ [Repositorio del curso](https://github.com/Open-Bootcamp/JavaScript-Basico)


## 1.Introducción a JavaScript
### Introducción al curso
+ **Contenido**: breve introducción a JavaScript, recomendación de VSCode como editor de código y extensiones de VSCode de utilidad.

### Node y NPM
+ **Contenido**: acerca de Node.js y NPM.

### Primer proyecto Node
1. Crear carpeta para proyecto: **proyectos\004\01introduccion\primer-proyecto**.
2. Crear proyecto Node:
    + $ npm init
        + package name: (primer-proyecto): hola-mundo
        + version: (1.0.0): ENTER
        + description: Proyecto de prueba.
        + entry point: (index.js): ENTER
        + test command: ENTER
        + git repository: ENTER
        + keywords: holamundo, first project
        + author: Pedro Bazó
        + license: (ISC): ENTER
        + Muestra el package.json:
            ```json
            {
                "name": "hola-mundo",
                "version": "1.0.0",
                "description": "Proyecto de prueba.",
                "main": "index.js",
                "scripts": {
                    "test": "echo \"Error: no test specified\" && exit 1"
                },
                "keywords": [
                    "holamundo",
                    "first",
                    "project"
                ],
                "author": "Pedro Bazó",
                "license": "ISC"
            }
            ```
        + Is this OK? (yes): y
3. Crear **proyectos\004\01introduccion\primer-proyecto\index.js**:
    ```js
    console.log("Iniciar servidor")
    ```
4. Crear **proyectos\004\01introduccion\primer-proyecto\hola_mundo.js**:
    ```js
    console.log("Hola Mundo")
    ```
5. Ejecutar:
    + $ node hola_mundo.js

### Ejecución y comentarios
1. Ejecutar script test:
    + $ npm run test
2. Modificar **proyectos\004\01introduccion\primer-proyecto\package.json**:
    ```json
    ≡
    "scripts": {
        "start": "node index.js",
        "saludar": "node hola_mundo.js",
        "test": "echo \"Error: no test specified\" && exit 1"
    },
    ≡
    ```
3. Ejecutar script saludar:
    + $ npm run saludar
    + $ node start

### Enlace al repositorio
+ https://github.com/Open-Bootcamp/JavaScript-Basico

### Ejercicio
+ Crea un nuevo proyecto de Node, y dentro del package.json crea un script que muestre por pantalla "Hola, este es mi primer ejercicio con Node en el mejor Bootcamp de programación del mundo".
+ **Resolución**:
    + Crear proyecto Node:
        + $ npm init
            + package name: (primer-proyecto): nuevo-proyecto
            + version: (1.0.0): ENTER
            + description: Nuevo proyecto.
            + entry point: (index.js): ENTER
            + test command: ENTER
            + git repository: ENTER
            + keywords: ENTER
            + author: Pedro Bazó
            + license: (ISC): ENTER
            + Muestra el package.json:
                ```json
                {
                    "name": "nuevo-proyecto",
                    "version": "1.0.0",
                    "description": "Nuevo proyecto.",
                    "main": "index.js",
                    "scripts": {
                        "test": "echo \"Error: no test specified\" && exit 1"
                    },
                    "author": "Pedro Bazó",
                    "license": "ISC"
                }
                ```
            + Is this OK? (yes): y
    + Modificar **proyectos\004\01introduccion\entrega\package.json**:
        ```json
        ≡
        "scripts": {
            "saludar": "Hola, este es mi primer ejercicio con Node en el mejor Bootcamp de programación del mundo",
            ≡
        },
        ≡
        ```


## 2.Sintaxis, variables y palabras reservadas de JS
### Tipado en JS y tipos primitivos
1. iniciacion-tipos.js:
    ```js
    // Tipos primitivos

    // number
    4;
    0;

    // string
    "Hola mundo";
    'Hola mundo';
    `Hola mundo`;

    // booleanos
    true;
    false;

    // nulo y undefined
    null;
    undefined;

    // null, undefined, false, 0 ==> Todas son False
    console.log(null === undefined)

    if (true) {
        console.log("cumple")
    } else {
        console.log("no cumple")
    }
    ```

### Declaración de variables y escritura dinámica
1. iniciacion-variables.js:
    ```js
    var variable;
    let variableLet_;

    // const constante;
    const constante = "Hola soy una constante";
    console.log(constante)
    // constante = "Adiós" // Nos da un error

    var a = 1;
    console.log(a);

    a = 4;
    console.log(a);

    let b = 3;
    console.log(b);

    b = 5;
    console.log(b);

    var variable = "Hola soy una variable VAR"

    for (var i = 0; i < 3; i++) {
        var variable = "Soy la segunda variable"
    }

    console.log(variable)

    let variableLet = "Hola soy una variable LET";

    for (var i = 0; i < 3; i++) {
        let variableLet = "Soy la segunda variable LET";
    }

    console.log(variableLet);

    /////////////////////////

    var num = 4;

    console.log(typeof num);

    num = "Hola soy num";

    console.log(typeof num);
    ```

### Notación en JavaScript
1. iniciacion-notacion.js:
    ```js
    // Notación
    // ; -> Delimitar el final de una línea
    const b = 4;
    b + 4;

    // . -> Se utiliza en los objetos para acceder a los atributos 
    // movil.anchura

    // [] -> listas, arreglos o arrays
    const ar = [1, 2, 3, 4]
    console.log(ar[2])

    // () -> Funciones
    function suma(a, b) {
        // Se escribe la función
    }

    // {} -> Llaves para objetos, funciones y estructuras de control
    const movil = {
        anchura: 5,
        altura: 10
    }

    if (true) {
        // todo lo que haya entre llaves
        const constante2 = "hola"
    }
    ```

### Listas, Objetos y Fechas en JS
1. Listas:
    ```js
    // Formas de definir listas
    const lista1 = [1, "hola", ture, undefined, null]
    const lista2 = new Array(1, "hola", ture, undefined, null)
    const lista3 = new Array(3)
    lista3[0] = "Primer elemenot de la lista"
    const lista4 = [lista1, lista2, lista3]
    ```
2. Objetos:
    ```js
    // Formas de definir objetos
    const objeto = {
        atributo1: 10,
        atributo2: "letras",
        "atributo-5": 4,
        otro_objeto: {
            atributo1: 10,
            atributo2: "letras",
        }
    }

    objeto.atributo3 = 2022
    objeto.atributo1 = 12
    // objeto.atributo-5 = 7
    ```
3. Fechas:
    ```js
    // Fechas
    // Librerias de apoyo: Moment.js
    const ahora = new Date()
    const fecha_milis = new Date(10)
    const fecha_cadena = new Date("march 25 2022")
    const fecha_valores = new Date(1972, 0, 15) // 15 de enero de 1972

    const dia = ahora.getDate()
    const mes = ahora.getMonth() + 1
    const anho = ahora.getFullYear()
    ```

### Ejercicio
+ Crea un nuevo archivo JS que contenga una lista con los siguientes elementos:
    - Tu nombre (string).
    - Tu edad (number).
    - ¿Eres desarrollador? (boolean).
    - Tu fecha de nacimiento (Date).
    - Tu libro favorito (Objeto con propiedades: titulo, autor, fecha, url).
+ **Resolución**:
    ```js
    const fechaNacimiento = new Date(1972, 0, 12)
    const libroFavorito = {
        titulo: "El principito",
        autor: "Antoine de Saint-Exupéry",
        fecha: new Date(1943, 3, 6),
        url: "https://books.google.co.ve/books/about/El_Principito.html?id=1N0KDgAAQBAJ&printsec=frontcover&source=kp_read_button&hl=es-419&redir_esc=y#v=onepage&q&f=false"
    }

    const lista = [
        "Pedro Bazó",
        50,
        true,
        fechaNacimiento,
        libroFavorito
    ]

    console.log(lista)
    ```



## 3.Estructuras de control
### Bifurcaciones if else y switch



    ```js
    ≡
    ≡
    ```



### Comparaciones en JS
### Bucles for y while
### Formas de controlar los bucles con continue y break
### Etiquetas en los bucles
### Ejercicio




## 4.Cadenas de texto

Tipos de declaracion de strings y cuando utilizarlos

Metodos mas comunes de los strings

Manipulación de cadenas de texto

Expresiones regulares y metodos de busqueda de cadenas

Ejercicio

## 5.Números en JavaScript

Numbers y precisión en JS

Operaciones y redondeo

Métodos de numbers y límites en JS

Ejercicio

## 6.Trabajando con listas

Listas y métodos de mutacion de listas

Concatenación y obtención de fragmentos de listas

Métodos de iteración en listas

Métodos avanzados, obtención de listas a partir de listas

Ordenación de listas y comparación entre dos listas

Identificar si existe un valor en un array y objetos iterables

Ejercicio

## 7.Trabajando con Sets y Objetos

Trabajando con Sets

Objetos en JavaScript

Fechas en JavaScript

Uso de la consola en JavaScript

Ejercicio 1

Ejercicio 2

Ejercicio 3

Ejercicio 4

## 8.Introducción a las funciones

Introducción a las funciones en JavaScript

Funciones de tipo flecha y anónimas

Carga y sobrecarga de funciones

Funciones asíncronas y promesas

Funciones generadoras

Ejercicio

## 9.Gestión de errores

Errores en JavaScript

Gestión de logs en NodeJS

Ejercicio

## 10.Módulos en JavaScript

Módulos y su utilización con CommonJS

Utilizando módulos con ES6

Librerías en Node y NPM y su utilización

Librerías interesantes

Ejercicio

## 11.POO en JavaScript

Introducción a la Programación Orientada a Objetos

Creación y uso de clases en JavaScript

Ámbito de las clases, métodos y atributos públicos, privados y protegidos

Getters y Setters en objetos

Herencia y Polimorfismo

Por qué no se habla de Interfaces en JavaScript y alternativas

Ejercicio

## 12.Depuración de código

Introducción a la Depuración en VSCode

Ejercicios

## 13.Configuracion y uso de ESLint

Qué es el linting y ESLint

Fichero de configuración ESLint

Instalación y creación de ficheros de configuración personalizados

Reglas temporales y scrips para ejecución de ESLint en nuestro código

Ejercicio

## 14.Gestión de eventos

Introducción a HTML con JS

Utilización de librerías de terceros

Manejo de eventos en JavaScript

Eventos personalizados

JQuery

Alertas y Dialogos en pantalla

Ejercicio

## 15.Persistencia de datos en navegador

Persistencia de datos en navegador

Ejercicio

## 16.Aplicando Drag & Drop

Drag and Drop con JavaScript

Ejercicio

## 17.Usado Geolocalización

Inicialización de Mapas en HTML

Geolocalización

Ejercicio