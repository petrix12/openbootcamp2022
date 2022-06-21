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




    ```js
    ≡
    ≡
    ```



### Declaración de variables y escritura dinámica

### Notación en JavaScript

### Listas, Objetos y Fechas en JS

### Ejercicio

## 3.Estructuras de control

Bifurcaciones if else y switch

Comparaciones en JS

Bucles for y while

Formas de controlar los bucles con continue y break

Etiquetas en los bucles

Ejercicio

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