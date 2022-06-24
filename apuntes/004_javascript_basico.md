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
+ if-else.js:
    ```js
    // Bifurcaciones if...else
    let saldo = 50;
    let efectivo = 100;

    if (efectivo < saldo) {
        console.log("Puedes sacar dinero")
    }

    if (efectivo < saldo) {
        console.log("Puedes sacar dinero")
    } else {
        console.log("Saldo insuficiente")
    }
    ```
+ if-else-ifelse.js:
    ```js
    // If else + if else

    let nota = 200;

    if (nota === 5) {
        console.log("Enhorabuena, has obtenido un sobresaliente");
    } else if (nota === 4) {
        console.log("Buen trabajo, pero podrías haberlo hecho mejor");
    } else if (nota === 3) {
        console.log("Has obtenido un suficiente");
    } else if (nota === 2) {
        console.log("No has aprobado por poco");
    } else if (nota === 1) {
        console.log("No has estudiado nada, trabaja un poquito más para la próxima");
    } else {
        console.log("Error, introduce una nota entre el 1 y el 5");
    }
    ```
+ switch.js:
    ```js
    // Sentencias Switch
    let nota = 3;

    switch (nota) {
        case 5:
            console.log("Buen trabajo, ¡sobresaliente!");
            break;
        case 4:
            console.log("Buen trabajo, pero podrías haberlo hecho mejor");
            break;
        case 3:
            console.log("Has obtenido un suficiente");
            break;
        case 2:
            console.log("No has aprobado por poco");
            break;
        case 1:
            console.log("No has estudiado nada, trabaja un poquito más para la próxima");
            break;
        default:
            console.log("Error")
            break;
    }
    ```

### Comparaciones en JS
+ comparaciones.js:
    ```js
    // Comparaciones

    // Igualdad
    if (5 == 5) {
        console.log("5 es igual a 5")
    }

    if (5 === 5) {
        console.log("5 es muy igual a 5")
    }

    let a = 5;
    console.log(typeof a)
    let b = "5";
    console.log(typeof b)

    // == sólo compara el valor
    // === compara el valor y el tipo

    if (a == b) {
        console.log("a es igual a b - Débil")
    }

    if (a === b) {
        console.log("a es igual a b - Fuerte")
    }

    let c = 4;
    let d = "4";

    if (c != d) {
        console.log("c es diferente a d - Débil")
    }

    if (c !== d) {
        console.log("c es diferente a d - Fuerte")
    }

    // Comparaciones mayor que y menor que
    let max = 10;
    let min = 5;

    if (max > min) {
        console.log("max es mayor que min")
    }
    if (max >= 10) {
        console.log("max es mayor o igual que min")
    }

    if (min < max) {
        console.log("min es menor que max")
    }
    if (min <= max) {
        console.log("min es menor o igual que max")
    }
    ```

### Bucles for y while
+ bucles-for.js:
    ```js
    // Bucles For

    // i = i + 1
    // i += 1
    // i++

    for (let i = 0; i < 10; i++) {
        // Esto es el bucle
        console.log(i)
    }

    let lista = [1, 4, 6, 2, 3, 7, 10, 12, 800];
    for (let i = 0; i < lista.length; i++) {
        console.log(lista[i] * 2)
    }

    // Estructura for...of
    for (let valor of lista) {
        console.log(valor)
    }

    // Estructura forEach
    lista.forEach(valor => {
        console.log(valor)
    })

    // Estructura for...in
    let persona = {
        nombre: "Gorka",
        apellido: "Villar",
        edad: 34,
        isDeveloper: true
    }
    console.log(persona.nombre)

    let prop = "edad";
    console.log(persona[prop])

    for (let propiedad in persona) {
        console.log(propiedad);
        console.log(persona[propiedad])
    }
    ```
+ bucles-while.js:
    ```js
    // Bucles While

    let i = 0;
    let max = 10;
    while (i < max) {
        console.log(i);
        i++;
    }

    i = 15;
    // Do...while
    do {
        console.log("Estoy en el do while")
    } while (i < max)
    ```

### Formas de controlar los bucles con continue y break
+ break-continue.js:
    ```js
    // Casos muy específicos - break, continue
    let lista = [1, 2, 3, 4, 5, 6, 7, 8];

    for (let i = 0; i < lista.length; i++) {
        if (lista[i] === 3) {
            continue;
        }
        let j = 50;
        const k = 100;
        console.log(lista[i]);
        console.log(j);
        console.log(k);

        if (lista[i] > 5) {
            break;
        }
    }

    // Cuál es el ámbito de un bucle
    console.log(k);
    console.log(i);
    console.log(j);
    ```

### Etiquetas en los bucles
+ labels-bucles-rotulados.js:
    ```js
    // break y continue
    // labels

    let unidades = 0
    let decenas = 0

    bucleDecenas: while (true) {
        bucleUnidades: while (true) {
            console.log(`El número actual es: ${decenas}${unidades}`)
            unidades++
            if (unidades === 10) {
                unidades = 0
                break bucleUnidades
            }
            if (decenas === 2) {
                break bucleDecenas
            }
        }
        decenas++
    }
    console.log("Ya hemos terminado")
    ```

### Ejercicio
+ Crea los siguientes archivos JS:
    - factorial-for.js -> Este archivo debe calcular el factorial de 10 utilizando un solo bucle for.
    - factorial-while.js -> Este archivo debe calcular el factorial de 10 utilizando un bucle while
    - factorial-break.js -> Este archivo debe calcular el factorial de 10 utilizando un bucle while, una bifurcación if y una sentencia break.
+ **Resolución**:
    + factorial-for.js:
        ```js
        numero = 10
        factorial = 1

        for(let i = 1; i <= numero; i++) {
            factorial *= i
        }

        console.log(`El factorial de ${numero} es ${factorial}`)
        ```
    + factorial-while.js:
        ```js
        numero = 10
        factorial = 1

        let i = 1
        while(i <= numero) {
            factorial *= i
            i++
        }

        console.log(`El factorial de ${numero} es ${factorial}`)
        ```
    + factorial-break.js:
        ```js
        numero = 10
        factorial = 1

        let i = 1
        while(true) {
            factorial *= i
            i++
            if(i > numero) {
                break
            }
        }

        console.log(`El factorial de ${numero} es ${factorial}`)
        ```


## 4.Cadenas de texto
### Tipos de declaracion de strings y cuando utilizarlos
+ introduccion-strings.js:
    ```js
    // Sesión 4 - Strings (cadenas de caracteres)
    let str_sng = 'Hola soy un texto con comillas simples';
    let str_dbl = "Hola soy un texto con comillas dobles";

    console.log(str_sng);
    console.log(str_dbl);

    let str_comillas = "El otro día me dijo literalmente \"ve a sacar la basura\""
    let str_comillas_simples = 'El otro día me dijo literalmente "ve a sacar la basura"'
    let str_comillas_dobles = "El otro día me dijo literalmente 've a sacar la basura'"
    let str_comillas_simples_2 = 'El otro día me dijo literalmente \'ve a sacar la basura\''

    console.log(str_comillas)
    console.log(str_comillas_simples)
    console.log(str_comillas_dobles)

    ////// Comillas invertidas (backticks)
    let str_backticks = `Hola esto es un string con backticks`

    console.log(str_backticks)

    let nombre = "Iñigo"
    let saludo = `Hola, ${nombre} bienvenido`

    console.log(saludo)

    // Plantillas HTML
    let plantilla = `
        <html>
            <h1>Página web de ${nombre}</h1>
            <p>Este es un párrafo</p>
        </html>
    `;

    console.log(plantilla)

    //// Introducción de variables en html
    let libros = ["Empieza por el por qué", "El monje que vendió su Ferrari", "El poder del ahora"]
    ```

### Metodos mas comunes de los strings
+ metodos-strings-01.js:
    ```js
    // Métodos más utilizados con cadenas de caracteres
    // Cómo obtener la longitud de un string
    let str = "Hola soy un string";
    console.log(str.length)

    // Obtener partes de cadenas de caracteres
    // slice() substring() substr()
    let slice_str = str.slice(5, 10)
    console.log(slice_str)

    let substring_str = str.substring(5, 10)
    console.log(substring_str)

    let substr_str = str.substr(5, 10)
    console.log(substr_str)

    // Reemplazar parte del contenido de una cadena de texto
    let cadena = "Hola mi nombre es Gorka"
    console.log(cadena)

    // Al utilizar strings sólo reemplaza la primera instancia
    console.log(cadena.replace('Gorka', 'Miguel'))

    let texto_largo = "Tito no es un mono cualquiera. A Tito no le gusta trepar por los árboles y odia comer plátanos. Él prefiere pasear por el bosque, oler las flores y recoger las nueces que se caen de los árboles."

    // Al utilizar strings sólo reemplaza la primera instancia
    console.log(texto_largo.replace('los', 'cinco'))

    // Al utilizar la expresión regular /g (global), reemplaza todas las instancias
    console.log(texto_largo.replace(/los/g, 'cinco'))
    ```

### Manipulación de cadenas de texto
+ metodos-strings-02.js:
    ```js
    // Métodos de cadenas de texto (parte 2)
    let input = "ESCORpio"
    let db = "escorpio"

    // toLowerCase() - toUpperCase()
    console.log(input.toLowerCase())
    console.log(input.toUpperCase())
    console.log(input.toLowerCase() === db.toLowerCase())
    console.log(input.toUpperCase() === db.toUpperCase())

    // Formas de concatenar dos cadenas de caracteres
    let str_1 = "Hola soy la primera cadena."
    let str_2 = "Y yo soy la segunda cadena."

    console.log(str_1.concat(" ", str_2))
    console.log(str_1 + " " + str_2)
    console.log(`${str_1} ${str_2}`)

    // Eliminar espacios al inicio y al final
    let str_3 = "    Hola soy un string con espacios al final.   "
    console.log(str_3.length)
    // trim()
    console.log(str_3.trim().length)
    console.log(str_3.trimStart().length)
    console.log(str_3.trimEnd().length)

    // Obtener el caracter que hay en cierta posición
    let str_4 = "Hola soy el string número 4" // ["H", "o", "l", "a", " ", "s"........]

    console.log(str_4.charAt(5))
    console.log(str_4[5])

    // Obtener la posición de una palabra dentro de una cadena de caracteres
    let str_5 = "Hola soy Gorka y me gusta el surf. Mi nombre es Gorka y mi apellido es Villar"
    console.log(str_5.indexOf("Gorka"))
    console.log(str_5.charAt(9))
    console.log(str_5.lastIndexOf("Gorka"))
    ```

### Expresiones regulares y metodos de busqueda de cadenas
+ metodos-strings-03.js:
    ```js
    // Métodos de cadenas de texto (parte 3)
    // https://regexr.com
    let texto_largo = "Tito no es un mono cualquiera. A Tito no le gusta trepar por los árboles y odia comer plátanos. Él prefiere pasear por el bosque, oler las flores y recoger las nueces que se caen de los árboles."

    console.log(texto_largo.match(/no/g))

    // ¿Existe la palabra dentro del texto?
    console.log(texto_largo.includes("terremoto"))

    // Saber si un texto empieza con una palabra
    console.log(texto_largo.startsWith("Tito no es un mono"))

    // Saber si un texto termina con otra palabra
    console.log(texto_largo.endsWith("árboles."))
    ```

### Ejercicio
+ Crea un archivo JS que contenga las siguientes líneas:
    - Una cadena de texto con tu Nombre
    - Otra cadena de texto con tu Apellido
    - Una cadena de texto que se llame "estudiante" concatenando tu Nombre y tu Apellido con un espacio entre medias
    - Una cadena de texto que se llame "estudianteMayus" que contenga la cadena estudiante pero todo en mayúsculas
    - Una cadena de texto que se llame "estudianteMinus" que contenga la cadena estudiante pero todo en minúsculas
    - Una variable que contenga el número de letras de la cadena "estudiante" contando los espacios
    - Una variable que contenga la primera letra del Nombre
    - Otra variable que contenga la última letra del Apellido
    - Una cadena de texto que elimine los espacios de la variable "estudiante"
    - Una variable booleana que diga si el Nombre está contenido en la variable "estudiante"
+ **Resolución**:
    ```js
    nombre = "Pedro"
    apellido = "Bazó"
    estudiante = `${nombre} ${apellido}`
    estudianteMayus = estudiante.toUpperCase()
    estudianteMinus = estudiante.toLowerCase()
    letrasEstudiante = estudiante.length
    primerLetraNombre = nombre.substring(0,1)
    ultimaLetraApellido = apellido.substring(apellido.length - 1, apellido.length)
    estudianteSinEspacios = estudiante.replace(/ /g, '')
    estaNombreEnEstudiante = estudiante.includes(nombre)

    console.log("nombre:", nombre)
    console.log("apellido:", apellido)
    console.log("estudiante:", estudiante)
    console.log("estudianteMayus:", estudianteMayus)
    console.log("estudianteMinus:", estudianteMinus)
    console.log("letrasEstudiante:", letrasEstudiante)
    console.log("primerLetraNombre:", primerLetraNombre)
    console.log("ultimaLetraApellido:", ultimaLetraApellido)
    console.log("estudianteSinEspacios:", estudianteSinEspacios)
    console.log("estaNombreEnEstudiante:", estaNombreEnEstudiante)
    ```


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