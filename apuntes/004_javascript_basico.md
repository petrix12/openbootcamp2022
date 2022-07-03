# JavaScript Básico
+ **Instructor**: Gorka Villar
+ [Resolución de ejercios](https://github.com/Open-Bootcamp/ResolucionEjercicios/tree/main/JavaScript)
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
    - Una cadena de texto con tu Nombre.
    - Otra cadena de texto con tu Apellido.
    - Una cadena de texto que se llame "estudiante" concatenando tu Nombre y tu Apellido con un espacio entre medias.
    - Una cadena de texto que se llame "estudianteMayus" que contenga la cadena estudiante pero todo en mayúsculas.
    - Una cadena de texto que se llame "estudianteMinus" que contenga la cadena estudiante pero todo en minúsculas.
    - Una variable que contenga el número de letras de la cadena "estudiante" contando los espacios
    - Una variable que contenga la primera letra del Nombre.
    - Otra variable que contenga la última letra del Apellido.
    - Una cadena de texto que elimine los espacios de la variable "estudiante".
    - Una variable booleana que diga si el Nombre está contenido en la variable "estudiante".
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
### Numbers y precisión en JS
+ declaracion-de-variables-numericas.js:
    ```js
    // Sesión 05 - Numbers
    // Declaración de variables numéricas (enteros y con decimales)
    let a = 5;

    console.log(a);

    let b = 0.1;

    console.log(b);

    // Precisión
    let c = 0.2;

    console.log(b + c);
    // Pequeño truco para obtener valores "reales"
    console.log(Math.round((0.1 + 0.2) * 100)/100);
    ```

### Operaciones y redondeo
+ operaciones-aritmeticas-y-redondeo.js:
    ```js
    // Principales operaciones aritméticas
    let a = 3.5;
    let b = 4.8;

    // Suma (+)
    console.log(a + b);
    // Resta (-)
    console.log(a - b);
    // Multiplicación (*)
    console.log(a * b);
    // División (/)
    console.log(a / b);

    // Representación de los números en cadenas de texto
    console.log(typeof a);
    let a_s = a.toString();

    console.log(a_s);
    console.log(typeof a_s);

    // Redondeo de números decimales
    let c = 3.3;
    let d = c * 3;

    console.log(d);
    console.log(typeof d);

    // .toFixed(x) - Limitar el número de decimales al valor x
    console.log(d.toFixed(4));
    console.log(typeof d.toFixed(4));

    let e = 1839.1232456789;
    let f = 2213556153215;
    console.log(e.toFixed(2));
    console.log(f.toFixed(2));

    // .toPrecision(x) - Limita el número de cifras significativas
    console.log(e.toPrecision(7));
    console.log(f.toPrecision(7));

    console.log(typeof f.toPrecision(3));
    ```

### Métodos de numbers y límites en JS
+ casting-valores-extremos-en-JS.js:
    ```js
    // Operador .valueOf() - Obtener valores numéricos a partir de literales
    let a = 2;
    let b = new Number(3);

    console.log(a);
    console.log(b);
    console.log(a + b);
    console.log(a.valueOf() + b.valueOf());

    console.log(b.valueOf());

    let str = new String("Hola soy un string");
    console.log(str);
    console.log(str.valueOf());

    // NaN (Not a Number) - Infinity
    let n = Number('adios');
    console.log(n);
    console.log(isNaN(n));

    let numerador = 19;
    let divisor = 0;
    console.log(numerador / divisor);

    let divisor_2 = null;
    console.log(numerador / divisor_2);

    // Cómo convertir los string a valores numéricos con Number, parseInt y parseFloat
    let numero = '5.89';
    let num2 = 17.2;

    console.log(typeof numero);
    console.log(numero + num2); // Error de concepto

    console.log(Number(numero) + num2);

    console.log(parseInt(numero))
    console.log(parseFloat(numero))

    let num3 = 4;
    console.log(parseInt(num3))
    console.log(parseFloat(num3))

    // Números hexadecimales (base 16)
    let numHex = '0x3a5b7';
    console.log(parseInt(numHex, 16));

    // Obtener los valores máximo y mínimo en Javascript
    let min_precision = Number.EPSILON;
    let min_valor_JS = Number.MIN_VALUE;
    let max_valor_JS = Number.MAX_VALUE;

    console.log(min_precision);
    console.log(min_valor_JS);
    console.log(max_valor_JS);
    ```

### Ejercicio
+ Crea un archivo JS que contenga las siguientes líneas:
    - Una variable que contenga tu altura en centímetros (entero).
    - Una variable que contenga tu altura en metros (número de coma flotante).
    - Una variable que contenga tu peso en kilogramos (número de coma flotante).
    - Una variable que contenga tu altura en metros redondeada hacia arriba.
    - Una variable que contenga tu peso en kilogramos redondeado hacia abajo.
    - Una variable que contenga si "el máximo valor que se puede obtener en Javascript + 1" es igual al máximo valor que se puede obtener en Javascript.
+ **Resolución**:
    ```js
    altura_cm = 183
    altura_m = altura_cm / 100
    peso_k = 102.3
    altura_m_up = Math.ceil(altura_m)
    altura_m_down = Math.floor(altura_m)
    maximoValorJS = Number.MAX_VALUE;
    boolMaxValor = maximoValorJS === (maximoValorJS + 1)

    console.log("altura_cm: ", altura_cm)
    console.log("altura_m: ", altura_m)
    console.log("peso_k: ", peso_k)
    console.log("altura_m_up: ", altura_m_up)
    console.log("altura_m_down: ", altura_m_down)
    console.log("maximoValorJS: ", maximoValorJS)
    console.log("maximoValorJS + 1: ", maximoValorJS + 1)
    console.log("boolMaxValor: ", boolMaxValor)
    ```


## 6.Trabajando con listas
### Listas y métodos de mutacion de listas
+ metodos-basicos-listas.js:
    ```js
    // Cómo trabajar con listas (arrays, arreglos, vectores...)
    let var1 = { id: false }
    let array = [1, "hola", false, { id: 5 }, null, undefined, var1]

    console.log(array)

    // Acceder a los valores de un array a través de su posición
    // array[indice]  => 0, 1, 2, 3, 4, 5, ....
    console.log(array[0])
    console.log(array[1])
    console.log(array[2])
    console.log(array[3])

    // Métodos para introducir nuevos valores en nuestros arrays
    // .push() .unshift() => Mutan el valor de nuestro array

    // Valores al final -> Push
    array.push("final", 45, 100, false)
    console.log(array)

    // Valores al principio -> Unshift
    array.unshift("inicio", 87, 99)
    console.log(array)

    // Métodos para eliminar valores en nuestros arrays
    // .pop() .shift() => Mutan el valor del array


    const array2 = [1, 3, "hola", false]
    // Valores al final -> Pop
    array2.pop()
    console.log(array2)

    // Valores al principio -> Shift
    array2.shift()
    console.log(array2)

    // Método para eliminar, modificar o añadir valores en nuestro array
    // .splice(x, y, z)
    const array3 = [1, 2, 3, 4, 5, 6]

    // Eliminar valores .splice(indice, numValoresAEliminar)
    array3.splice(2, 1);
    console.log(array3)

    // Añadir valores .splice(indice, 0, valores)
    array3.splice(2, 0, "hola")
    console.log(array3)

    // Modificar valores .splice(indice, 1, valores)
    array3.splice(2, 1, 3)
    console.log(array3)
    ```

### Concatenación y obtención de fragmentos de listas
+ concatenacion-listas-y-factor-de-propagacion.js:
    ```js
    // Cómo unir dos listas .concat(lista2)
    const lista1 = ["hola", 2, false, null]
    const lista2 = ["adiós", 8, true, undefined]

    console.log(lista1.concat(lista2))
    console.log(lista1)

    const lista3 = lista1.concat(lista2)
    console.log(lista3)

    // Cómo unir dos listas con el factor de propagación
    console.log(...lista3)

    const lista4 = [...lista1, ...lista2]
    console.log(lista4)

    // ERROR!! Mal entendido el concepto del factor de propagación
    const lista5 = [lista1, lista2]
    console.log(lista5)
    ```
+ obtener-lista-de-otra-lista.js:
    ```js
    // Cómo obtener una lista a partir de otra .slice()
    const array = ["hola", 1, 2, 3, true, null, "adios"]

    // NO MODIFICA EL VALOR DEL ARRAY ORIGINAL
    console.log(array.slice(1, 4))
    const array2 = array.slice(2, 5)
    console.log(array2)

    const array3 = array.slice(2, -2)
    console.log(array3)
    ```

### Métodos de iteración en listas
+ busqueda-valores-find.js:
    ```js
    // Iterar los valores de una lista
    const array = ["hola", 2, 5, 90, false, undefined]

    // Forma antigua (poco eficiente)
    for (let i = 0; i < array.length; i++) {
        console.log(array[i])
    }

    // Forma ES6 (más eficiente) .forEach()
    let suma = 0;
    const arrayNums = [3, 6, 2, 77, 2, 3, 93, 19]
    arrayNums.forEach(valor => {
        suma += valor;
        console.log(valor)
    })
    console.log(suma)

    // Búsqueda de un valor dentro de una lista .find()
    // Quiero encontrar el elemento 90
    const variable = array.find(valor => {
        if (valor === 90) {
            return true
        }
    })

    console.log(variable)

    const listaObjetos = [
        { nombre: "Leire", edad: 35 },
        { nombre: "Gorka", edad: 34 },
        { nombre: "Miguel", edad: 28 },
        { nombre: "Lucía", edad: 3 },
        { nombre: "Amaia", edad: 29}
    ]

    // const objeto = listaObjetos.find(o => {
    //     if (o.nombre === "Miguel") {
    //         return true
    //     }
    // })
    const objeto = listaObjetos.find(o => o.nombre === "Miguel")
    console.log(objeto.edad)

    const { edad } = listaObjetos.find(o => o.nombre === "Miguel")
    console.log(edad)
    ```

### Métodos avanzados, obtención de listas a partir de listas
+ map-filter-reduce.js:
    ```js
    // Trabajar con métodos más avanzados
    // .map() .filter() .reduce()

    const array = ["San Sebastián", "Madrid", "Barcelona", "Alicante", "Bilbao"]

    const val = array.forEach(v => {
        console.log(v)
        return 4
    })
    console.log(val)

    const newArray = array.map((valor, indice) => `${indice + 1} - ${valor}`)
    console.log(newArray)

    const listaObjetos = [
        { nombre: "Leire", edad: 35 },
        { nombre: "Gorka", edad: 34 },
        { nombre: "Miguel", edad: 28 },
        { nombre: "Lucía", edad: 3 },
        { nombre: "Amaia", edad: 29}
    ]
    // const personasMayores = listaObjetos.filter(obj => {
    //     if (obj.edad > 30) {
    //         return true
    //     } else {
    //         return false
    //     }
    // })
    const personasMayores = listaObjetos.filter(obj => obj.edad > 30)
    console.log(personasMayores)

    const nuevaLista = listaObjetos.filter(obj => obj.nombre !== "Miguel")
    console.log(nuevaLista)

    const valores = [3, 56, 23, 5, 90, 100]

    const suma = valores.reduce((acumulado, cur, i, arrayOriginal) => {
        console.log(acumulado)
        console.log(cur)
        console.log(i)
        console.log(arrayOriginal)
        return acumulado + cur
    })
    console.log(suma)    
    ```

### Ordenación de listas y comparación entre dos listas
+ ordenar-listas.js:
    ```js
    // .sort() -> MODIFICA EL ARRAY
    const array = [2, 5, 9, 15, 1, 2, 0, 4]

    console.log(array)

    array.sort((a, b) => {
        if (a < b) {
            return +11568
        } else if (a > b) {
            return -153697
        } else { // a === b
            return 0
        }
    })

    console.log(array)

    // Ordenar únicamente arrays numéricos
    const arrayNumerico = [4, 1, 7, 3, 1, 3, 56, 1, 546]

    arrayNumerico.sort((a, b) => b - a)

    console.log(arrayNumerico)

    // Interesante en arrays de objetos
    const listaObjetos = [
        { nombre: "Leire", edad: 35 },
        { nombre: "Gorka", edad: 34 },
        { nombre: "Miguel", edad: 28 },
        { nombre: "Lucía", edad: 3 },
        { nombre: "Amaia", edad: 29}
    ]

    // listaObjetos.sort((a, b) => {
    //     if (a.edad < b.edad) {
    //         return -1
    //     } else if (a.edad > b.edad) {
    //         return +1
    //     } else {
    //         return 0
    //     }
    // })
    listaObjetos.sort((a, b) => a.edad - b.edad)

    console.log(listaObjetos)
    ```
+ comparacion-listas.js:
    ```js
    // Cómo podemos comparar listas
    // .every()
    const array = [4, 6, 7, 8, 3, 6, 2, 1, -4, -7, 12, 5, -40]

    // const resultado = array.every(valor => {
    //     if (valor > 0) {
    //         return true
    //     } else {
    //         return false
    //     }
    // })
    const resultado = array.every(valor => valor > 0)

    console.log(resultado)

    /// Comparacion de listas
    const ar1 = [1, 2, 3, 4]
    const ar2 = [1, 2, 3, 4]

    console.log(ar1 === ar2)

    const compararArrays = (array_1, array_2) => {
        if (array_1.length !== array_2.length) return false
        const res = array_1.every((valor, i) => valor === array_2[i])
        return res
    }

    console.log(compararArrays(ar1, ar2))

    const ar3 = [1, 2, 3, 9]

    console.log(compararArrays(ar1, ar3))
    ```

### Identificar si existe un valor en un array y objetos iterables
+ some-y-objetos-iterables.js:
    ```js
    // .some()
    const array = [3, 7, 2, 4, 7, 9, 42, 35, 7865, 23, -2]

    const res = array.some(valor => valor < -0)

    console.log(res)

    const existe = array.some(valor => valor === 9)

    console.log(existe)

    const listaObjetos = [
        { nombre: "Leire", edad: 35 },
        { nombre: "Gorka", edad: 34 },
        { nombre: "Miguel", edad: 28 },
        { nombre: "Lucía", edad: 3 },
        { nombre: "Amaia", edad: 29}
    ]

    const existeJuan = listaObjetos.some(persona => persona.nombre === "Juan")

    console.log(existeJuan)

    // Cómo obtener una lista a partir de un objeto iterable
    const str = "Hola soy Gorka"
    console.log(str[5])

    const ar_str = Array.from(str)
    console.log(ar_str)

    const set = new Set([2, 3, "hola", 4])
    const ar_set = Array.from(set)
    console.log(ar_set)

    const keys = array.keys()
    console.log(keys)

    const ar_keys = Array.from(keys)
    console.log(ar_keys)
    ```

### Ejercicio
+ Crea un archivo JS que contenga las siguientes líneas:
    - Una variable que contenga la lista de la compra (mínimo 5 elementos).
    - Modifica la lista de la compra y añádele "Aceite de Girasol".
    - Vuelve a modificar la lista de la compra eliminando "Aceite de Girasol".
    - Una lista de tus 3 películas favoritas (objetos con propiedades: titulo, director, fecha).
    - Una nueva lista que contenga las películas posteriores al 1 de enero de 2010 (utilizando filter).
    - Una nueva lista que contenga los directores de la lista de películas original (utilizando map).
    - Una nueva lista que contenga los títulos de la lista de películas original (utilizando map).
    - Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando concat).
    - Una nueva lista que concatene la lista de directores y la lista de los títulos (utilizando el factor de propagación).
+ **Resolución**:
    ```js
    listaCompra = [
        'Aguacate',
        'Queso',
        'Cloro',
        'Limón',
        'Piña'
    ]

    listaCompra.push('Aceite de Girasol')
    listaCompra.pop()

    listaPeliculas = [
        {
            titulo: "La vida es bella",
            director: "Roberto Benigni",
            fecha: new Date(1997, 11, 20)
        },
        {
            titulo: "Los miserables",
            director: "Bille August",
            fecha: new Date(1998, 4, 1)
        },
        {
            titulo: "Escarlata y negro",
            director: "Jerry London",
            fecha: new Date(1983, 1, 2)
        },
        {
            titulo: "Spiderman sin regreso a casa",
            director: "Jon Watts",
            fecha: new Date(2021, 11, 17)
        }
    ]

    listaPeliculasNuevas = listaPeliculas.filter(obj => obj.fecha >= new Date(2010, 0, 1))

    listaDirectores = listaPeliculas.map(obj => obj.director)
    listaTitulos = listaPeliculas.map(obj => obj.titulo)
    listaDirectoresTitulos = listaDirectores.concat(listaTitulos)
    listaDirectoresTitulos2 = [...listaDirectores, ...listaTitulos]

    console.log("listaCompra: ", listaCompra)
    console.log("listaPeliculas: ", listaPeliculas)
    console.log("listaPeliculasNuevas: ", listaPeliculasNuevas)
    console.log("listaDirectores: ", listaDirectores)
    console.log("listaTitulos: ", listaTitulos)
    console.log("listaDirectoresTitulos: ", listaDirectoresTitulos)
    console.log("listaDirectoresTitulos2: ", listaDirectoresTitulos2)
    ```

## 7.Trabajando con Sets y Objetos
### Trabajando con Sets
+ sets.js:
    ```js
    // Sets o conjuntos (en castellano)
    const array = [1, 2, 3, 4, 5, 6, 1, 2, 5, "hola", { id: 5 }, "hola"]

    const miSet = new Set(array)

    console.log(array)
    console.log(miSet)

    // .add()
    miSet.add(9)
    console.log(miSet)
    miSet.add(4)
    console.log(miSet)

    // .delete()
    miSet.delete("hola")
    console.log(miSet)

    // .clear()
    // miSet.clear()
    // console.log(miSet)

    // .has()
    // console.log(array.includes(2))
    console.log(miSet.has(40))

    // .size
    console.log(miSet.size)

    miSet.forEach(valor => {
        console.log(valor)
    })

    const it_miSet = miSet.values()
    console.log(it_miSet)

    const ar_miSet = [ ...miSet ]
    console.log(ar_miSet[1])
    ```

### Objetos en JavaScript
+ objetos.js:
    ```js
    // Trabajando con Objetos
    const obj = {
        id: 4,
        nombre: "Juan",
        apellido: "González",
        isDeveloper: false,
        libros_favoritos: ["El método", "El código de la manifestación"],
        "4-juegos": [1, 2, 3, 4]
    }

    console.log(obj.id)
    console.log(obj["4-juegos"])

    const prop = "isDeveloper"
    console.log(obj[prop])

    const obj2 = obj;
    console.log(obj2);

    obj2.nombre = "Iñigo"
    console.log(obj2.nombre)
    console.log(obj.nombre)

    let val1 = 4
    let val2 = val1

    val2 = 6
    console.log(val1)
    console.log(val2)

    //////////////

    const obj3 = { ...obj }

    console.log(obj.nombre)
    console.log(obj3.nombre)

    obj3.nombre = "Gorka"

    console.log(obj.nombre)
    console.log(obj3.nombre)

    /////////////
    // Cómo ordenar listas de objetos en función de una propiedad

    const listaPeliculas = [
        { titulo: "Lo que el viento se llevó", anyo: 1939 },
        { titulo: "Titanic", anyo: 1997 },
        { titulo: "Moana", anyo: 2016 },
        { titulo: "El efecto mariposa", anyo: 2004 },
        { titulo: "TED", anyo: 2012 }
    ]

    console.log(listaPeliculas)
    // .sort() -> MUTA EL VALOR DE LA LISTA ORIGINAL

    listaPeliculas.sort((a, b) => a.anyo - b.anyo)

    console.log(listaPeliculas)
    ```

### Fechas en JavaScript
+ fechas.js:
    ```js
    // Trabajando con fechas
    const fecha = new Date()

    console.log(fecha)

    // Atención - Los meses inicializan en 0 (0 - Enero, 11 - Diciembre)
    const fecha2 = new Date(1987, 10, 20, 1, 23, 52, 192)

    console.log(fecha2)

    const fecha3 = new Date(-10000000000000) // Milisegundos
    console.log(fecha3)

    const fecha4 = new Date("October 13, 1979 12:15:15")
    console.log(fecha4)

    console.log(fecha < fecha2)

    const fecha5 = new Date(1987, 10, 20, 1, 23, 52, 192)
    console.log(fecha5)

    console.log(fecha2 === fecha5) // ERROR - No se pueden comparar fechas de esta manera

    console.log(fecha2.getTime() === fecha5.getTime()) // OK - Esta es la forma de comparar la igualdad entre fechas

    /////// Obtener el día, el mes y el año de una fecha
    // Obtener el día .getDate()
    console.log(fecha2.getDate())

    // Obtener el mes .getMonth() (0 - Enero, 11 - Diciembre)
    console.log(fecha2.getMonth() + 1)

    // Obtener el año .getFullYear()
    console.log(fecha2.getFullYear())

    console.log(fecha2)

    // .toLocaleDateString
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Date/toLocaleDateString
    console.log(fecha2.toLocaleDateString("en-US"))
    ```

### Uso de la consola en JavaScript
+ Para crear un documento html en blanco en el navegador:
    + about:blank
+ Escribir por consola:
    ```js
    const edad = prompt("Cuál es tu edad?")
    ```

### Ejercicio 1
+ Crea un archivo llamado conjuntos.js que contenga las siguientes líneas:
    - Un nuevo Set con los nombres de tu familia.
    - Modifica el Set original añadiendo tu nombre (duplicado) (debería darte lo mismo).
    - Modifica el Set original añadiendo el nombre "Javascript" (ya que empieza a formar parte de tu vida ;).
+ **Resolución**:
    ```js
    const familia = new Set([
        'Pedro',
        'Leticia',
        'Isabel',
        'María',
        'Rebeca'
    ])
    console.log(familia)

    familia.add('Pedro')
    console.log(familia)

    familia.add('Javascript')
    console.log(familia)
    ```

### Ejercicio 2
+ Crea un archivo llamado objetos.js que contenga las siguientes líneas:
    - Un objeto con tus datos personales (nombre, apellido, edad, altura, eresDesarrollador).
    - Una variable que obtenga tu edad a partir del objeto anterior.
    - Una lista que contenga el objeto con tus datos personales y un nuevo objeto con los datos personales de tus dos mejores amig@s.
    - Una nueva lista con los objetos de la lista anterior ordenados por edad, de mayor a menor.
+ **Resolución**:
    ```js
    datos = {
        nombre: "Pedro",
        apellido: "Bazó",
        edad: 50,
        altura: 1.82, 
        eresDesarrollador: true
    }
    console.log("datos: ", datos)

    let { edad } = datos
    console.log("edad: ", edad)

    datos2 = {
        nombre: "Leticia",
        apellido: "Rodríguez",
        edad: 44,
        altura: 1.63, 
        eresDesarrollador: false
    }
    console.log("datos2: ", datos2)

    datos3 = {
        nombre: "Isabel",
        apellido: "Bazó",
        edad: 20,
        altura: 1.60, 
        eresDesarrollador: false
    }
    console.log("datos3: ", datos3)

    let lista = [datos, datos2, datos3]
    console.log("lista: ", lista)

    const listaNueva = [ ...lista ]
    console.log("listaNueva: ", listaNueva)
    listaNueva.sort((a, b) => b.edad - a.edad)
    console.log("listaNueva: ", listaNueva)
    ```

### Ejercicio 3
+ Crea un archivo llamado fechas.js que contenga las siguientes líneas:
    - La fecha de hoy.
    - La fecha de tu nacimiento.
    - Un variable que indique si hoy es más tarde (>) que la fecha de tu nacimiento.
    - Una variable que contenga el día de tu nacimiento.
    - Una variable que contenga el mes de tu nacimiento (recuerda que Enero es mes 0).
    - Una variable que contenga el año de tu nacimiento (con 4 dígitos).
+ **Resolución**:
    ```js
    hoy = new Date()
    nacimiento = new Date(1972, 0, 12)
    masTarde = hoy.getTime() > nacimiento.getTime()
    diaNacimiento = nacimiento.getDate()
    mesNacimiento = nacimiento.getMonth() + 1
    anyoNacimiento = nacimiento.getFullYear()

    console.log("hoy:", hoy)
    console.log("nacimiento:", nacimiento)
    console.log("masTarde:", masTarde)
    console.log("diaNacimiento:", diaNacimiento)
    console.log("mesNacimiento:", mesNacimiento)
    console.log("anyoNacimiento:", anyoNacimiento)
    ```

### Ejercicio 4
+ - Abre una nueva ventana "about:blank" en Google Chrome:
    - Abre la consola de desarrollador de Google Chrome (F12).
    - Pregunta al usuario cuál es su edad y almacénala en una variable llamada edad.
+ **Resolución**:
    ```js
    const edad = prompt("Cuál es tu edad?")
    ```


## 8.Introducción a las funciones
### Introducción a las funciones en JavaScript
+ declaracion-funciones.js:
    ```js
    // Qué son las funciones, cómo se declaran y cómo se utilizan
    const nom = "Gorka"

    // saludar("Miguel")
    saludar(nom)

    function saludar(nombre) {
        console.log(`Hola ${nombre}`)
    }

    ////

    let nombre_2 = "Juan"
    console.log(nombre_2)

    despedir(nombre_2)
    console.log(nombre_2)

    function despedir(nombre) {
        nombre = "Diego"
        console.log(`Adiós ${nombre}`)
    }

    ////

    let persona = { nombre: "Juan", apellido: "González" }
    console.log(persona)

    saludarPersona(persona)

    console.log(persona)

    function saludarPersona(objeto) {
        objeto.apellido = "Villar"
        console.log(`Hola ${objeto.nombre} ${objeto.apellido}`)
    }

    saludar()

    ///////

    function imprimeNumero(numero = 7) { // Parámetros por defecto
        console.log(numero)
    }

    imprimeNumero()

    /////////

    function imprimir(...parametros) {
        console.log(parametros)
    }

    imprimir(1, 3, 9, 2, "hola", { id: 9 })

    /////

    function suma(...nums) {
        return nums.reduce((a, b) => a + b)
    }

    const s = suma(1, 2, 3, 4, 9, 15, 16)

    console.log(s)

    //////
    let variable = "hola"

    function multiplicar(a = 0, b = 0) {
        console.log(variable)
        let variable_interna = "adiós"
        console.log(variable_interna)
        return a * b
    }

    console.log(multiplicar(4, 9))
    ```

### Funciones de tipo flecha y anónimas
+ funciones-flecha-y-anonimas.js:
    ```js
    // Funciones tipo flecha - funciones anónimas

    const array = [1, 5, 6, 2, 7, 12, 8, 92]

    const array2 = array.map((valor) => valor * 2)

    console.log(array2)

    // const dobleDelValor = valor => {
    //     return valor * 2
    // }
    const dobleDelValor = valor => valor * 2

    console.log(doble(6))
    console.log(dobleDelValor(6))

    const array3 = array.map(dobleDelValor)

    console.log(array3)

    function doble(valor) {
        return valor * 2
    }
    ```

### Carga y sobrecarga de funciones
+ carga-y-sobrecarga-de-funciones.js:
    ```js
    // Carga y sobrecarga de funciones
    function saludar() {
        hola()
    }

    function hola() {
        console.log("Hola! Soy la función hola()")
    }

    saludar()

    /// 1. global()
    /// 2. saludar() global()
    /// 3. hola() saludar() global()
    /// 4. saludar() global()
    /// 5. global()

    // function recursivo() {
    //     recursivo()
    // }

    // recursivo()
    ```

### Funciones asíncronas y promesas
+ funciones-asincronas-y-promesas.js:
    ```js
    // Funciones asíncronas

    function miAsinc() {
        // Hace una llamada a una base de datos externa
        // Puede darnos algún error
    }

    const miPromesa = new Promise((resolve, reject) => {
        const i = Math.floor(Math.random() * 2)
        // Si está todo correcto
        if (i !== 0) {
            resolve()
        } else {
            reject()
        }
    })

    miPromesa
        .then(() => console.log("Se ha ejecutado de forma correcta"))
        .catch(() => console.log("ERROR"))
        .finally(() => console.log("Yo me ejecuto siempre"))

    // async await
    ```

### Funciones generadoras
+ funciones-generadoras.js:
    ```js
    function* generaId() {
        let id = 0;
        while(true) {
            id++
            if (id === 10) {
                return id
            }
            yield id // Esperando hasta que se vuelva a llamar
        }
    }

    const gen = generaId();

    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    ```

### Ejercicio
+ Crea un archivo JS que contenga las siguientes líneas:
    - Una función sin parámetros que devuelva siempre "true".
    - Una función asíncrona que utilice un setTimeout y pase por consola un "Hola soy una promesa" 5 segundos después de haberse ejecutado.
    - Una función generadora de índices pares automáticos.
+ **Resolución**:
    ```js
    // Parte I: Una función sin parámetros que devuelva siempre "true"
    const cierto = () => true

    // Parte II: Una función asíncrona que utilice un setTimeout y pase por consola un "Hola soy una promesa" 5 segundos después de haberse ejecutado
    const funcionAsync = new Promise((resolve, reject) => {
        if (true) {
            setTimeout(() => console.log("Hola soy una promesa"), 5000)
        } else {
            reject()
        }
    })

    // Parte III: Una función generadora de índices pares automáticos
    function* generaId() {
        let id = 0;
        while(true) {
            id += 2
            yield id
        }
    }

    const gen = generaId();

    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    console.log(gen.next().value)
    ```


## 9.Gestión de errores
### Errores en JavaScript
+ errores-javascript.js:
    ```js
    const miFuncion = val => {
        if (typeof val === "number") {
            return 2 * val
        }
        throw new Error("El valor debe ser de tipo número")
    }

    // const elDoble = miFuncion("a1a")
    const numero = "8";

    try {
        // Código que puede fallar
        console.log("Está ejecutándose de manera correcta")
        const doble = miFuncion(numero)
        console.log(doble)
    } catch (e) {
        // En caso de fallar, quiero que ejecutes
        console.error(`El valor de e es: ${e}`)
        console.error("ERROR!")
    } finally {
        console.log("Esto se va a ejecutar tanto si se produce algún error, como si no existe ninguno")
    }

    // InternalError, SyntaxError, TypeError, RangeError y ReferenceError
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Error
    ```

### Gestión de logs en NodeJS
1. Crear proyecto node:
    + $ npm init -y
2. Modificar **proyectos\004\09gestion-errores\package.json**:
    ```json
    ≡
    "scripts": {
        "start": "node index.js"
    },
    ≡
    ```
3. Crear **C:\xampp\htdocs\carrera\bootcamp\proyectos\004\09gestion-errores\index.js**:
    ```js
    const logger = require('./logger')

    // logger.log("Hola estoy saliendo por pantalla")
    logger.info("Hola esto es un mensaje informativo")
    logger.debug("Esto es un mensaje de debug")
    logger.warn("Esto es un mensaje de advertencia")
    logger.error("Esto es un error")
    ```
4. Instalar la dependencia Winston:
    + https://www.npmjs.com/package/winston
    + $ npm install winston
5. Crear **proyectos\004\09gestion-errores\logger\index.js**:
    ```js
    const winston = require('winston');

    const logger = winston.createLogger({
        level: 'debug',
        format: winston.format.json(),
        // defaultMeta: { service: 'user-service' },
        transports: [
            //
            // - Write all logs with importance level of `error` or less to `error.log`
            // - Write all logs with importance level of `info` or less to `combined.log`
            //
            new winston.transports.Console(),
            new winston.transports.File({ filename: 'error.log', level: 'error' }),
            new winston.transports.File({ filename: 'combined.log' }),
        ],
    });

    module.exports = logger;
    ```
6. Ejecutar proyecto:
    + $ npm start

### Ejercicio
+ Crea un nuevo proyecto de Node:
    - Instala la dependencia Winston.
    - En el archivo index.js crea una función que devuelva un error con un mensaje personalizado.
    - Registra el error en un archivo a través de un try...catch.
+ **Resolución**:
    + $ npm init -y
    + Modificar **proyectos\004\09gestion-errores\entrega\package.json**:
        ```json
        ≡
        "scripts": {
            "start": "node index.js"
        },
        ≡
        ```
    + $ npm install winston
    + Crear **proyectos\004\09gestion-errores\entrega\logger\index.js**:
        ```js
        const winston = require('winston');

        const logger = winston.createLogger({
            level: 'debug',
            format: winston.format.json(),
            // defaultMeta: { service: 'user-service' },
            transports: [
                //
                // - Write all logs with importance level of `error` or less to `error.log`
                // - Write all logs with importance level of `info` or less to `combined.log`
                //
                new winston.transports.Console(),
                new winston.transports.File({ filename: 'error.log', level: 'error' }),
                new winston.transports.File({ filename: 'combined.log' }),
            ],
        });

        module.exports = logger;
        ```
    + Crear **proyectos\004\09gestion-errores\entrega\index.js**:
        ```js
        const logger = require('./logger')

        try {
            logger.info("Hola esto es un mensaje informativo")
        } catch (error) {
            logger.error("Esto es un error")
        }
        ```
    + $ npm start

## 10.Módulos en JavaScript
### Módulos y su utilización con CommonJS
1. Crear **proyectos\004\10modulos\index.js**:
    ```js
    // Formas de importar/exportar módulos
    // 1. CommonJS - require
    // 2. Import ES6 - import

    // const moduloMatematicas = require("./modulos/matematicas.js")
    // const factorial = moduloMatematicas.factorial;
    // const { factorial, suma } = moduloMatematicas;
    // const suma = moduloMatematicas.suma;
    // console.log(moduloMatematicas.suma)

    const { factorial, suma } = require("./modulos/matematicas.js")

    const fact = factorial(5)
    console.log(fact)

    const sum = suma(12, 90)
    console.log(sum)

    // console.log(module)
    ```
2. Crear **proyectos\004\10modulos\detalles.js**:
    ```js
    function factorial(a) {
        // Factorial de 5: 5 * 4 * 3 * 2 * 1
        let factorial = 1;
        for (let i = 2; i <= a; i++) {
            factorial *= i;
        }
        return factorial;
    }

    console.log(factorial(10))
    ```
3. Crear **proyectos\004\10modulos\modulos\matematicas.js**:
    ```js
    function suma(a, b) {
        return a + b
    }

    function multiplica(a, b) {
        return a * b
    }

    function eleva(a, b) {
        return a ** b
    }

    function factorial(a) {
        // Factorial de 5: 5 * 4 * 3 * 2 * 1
        let factorial = 1;
        for (let i = 2; i <= a; i++) {
            factorial *= i;
        }
        return factorial;
    }

    module.exports = {
        suma,
        multiplica,
        eleva,
        factorial
    }
    ```

### Utilizando módulos con ES6
1. Crear carpeta **proyectos\004\10modulos\modulos-es6**.
2. Crear proyecto:
    + $ npm init -y
3. Crear **proyectos\004\10modulos\modulos-es6\index.js**:
    ```js
    // import { suma, eleva, nombre } from './modulos/matematicas.js'
    import * as moduloMatematicas from './modulos/matematicas.js'
    import getAutor, { libro } from './modulos/literatura.js'

    const sum = moduloMatematicas.suma(4, 12)
    console.log(sum)

    const potencia = moduloMatematicas.eleva(2, 21)
    console.log(potencia)

    console.log(moduloMatematicas.nombre)

    console.log(getAutor())
    console.log(libro)
    ```
4. Crear **proyectos\004\10modulos\modulos-es6\modulos\matematicas.js**:
    ```js
    export function suma(a, b) {
        return a + b
    }

    export function multiplica(a, b) {
        return a * b
    }

    export function eleva(a, b) {
        return a ** b
    }

    export function factorial(a) {
        // Factorial de 5: 5 * 4 * 3 * 2 * 1
        let factorial = 1;
        for (let i = 2; i <= a; i++) {
            factorial *= i;
        }
        return factorial;
    }

    export const nombre = "matematicas"
    ```
5. Modificar **proyectos\004\10modulos\modulos-es6\package.json**:
    ```json
    ≡
    "main": "index.js",
    "type": "module",
    ≡
    ```
6. Crear módulo **proyectos\004\10modulos\modulos-es6\modulos\literatura.js**:
    ```js
    const getAutor = () => {
        return "Miguel de Cervantes"
    }

    export const libro = "Don Quijote de la Mancha"

    export default getAutor
    ```

### Librerías en Node y NPM y su utilización
+ https://www.npmjs.com
1. Crear carpeta **proyectos\004\10modulos\video-librerias** e ingresar en ella.
2. Ejecutar:
    + $ npm init -y
3. Modificar **proyectos\004\10modulos\video-librerias\package.json**:
    ```json
    ≡
    "main": "index.js",
    "type": "module",
    "scripts": {
        "start": "node index.js"
    },
    ≡
    ```
4. Ejecutar:
    + $ npm i axios
5. Crear **proyectos\004\10modulos\video-librerias\index.js**:
    ```js
    // Instalar axios para hacer llamadas a servicios externos
    import axios from "axios"

    axios.get('https://pokeapi.co/api/v2/pokemon/charmander')
        .then(function (response) {
            // handle success
            console.log("Success!!!")
            console.log(response.data)
        })
        .catch(function (error) {
            // handle error
            console.log("Error!!!")
            console.log(error);
        })
    ```
6. Ejecutar:
    + $ npm start

### Librerías interesantes
+ **Contenido**: sobre algunas librerias o framework de JavasScript.

### Ejercicio
+ Crea un nuevo proyecto de Node:
    - Configura el proyecto para utilizar los módulos de ES6.
    - Crea un archivo controller.js que exporte 2 funciones: suma(a, b) y multiplica(a, b).
    - En el entrypoint index.js, importa el módulo controller.js.
    - El entrypoint index.js debe utilizar las funciones del módulo para devolver la multiplicación de suma(1, 2) y suma(4, 5).
    - Instala e importa la librería chalk (https://www.npmjs.com/package/chalk).
    - Modifica el último console.log del entrypoint index.js para devolver el resultado en color verde.
+ **Resolución**:
    + $ npm init -y
    + Modificar **proyectos\004\10modulos\entrega\package.json**:
        ```json
        ≡
        "main": "index.js",
        "type": "module",
        "scripts": {
            "start": "node index.js"
        },
        ≡
        ```
    + Crear módulo **proyectos\004\10modulos\entrega\controller.js**:
        ```js
        export function suma(a, b) {
            return a + b
        }

        export function multiplica(a, b) {
            return a * b
        }
        ```
    + Crear **proyectos\004\10modulos\entrega\index.js**:
        ```js
        importance * as moduloController from './controller.js'
        import chalk from 'chalk'

        console.log(moduloController.suma(1, 2))
        console.log(chalk.green(moduloController.suma(4, 5)))
        ```
    + $ npm i chalk
    + $ npm start


## 11.POO en JavaScript
### Introducción a la Programación Orientada a Objetos
+ index.js:
    ```js
    const persona = {
        nombre: "Gorka",
        edad: 34,
        isDeveloper: true,
        saludo: function() {
            console.log('Hello')
        }
    }

    // console.log(persona)
    persona.saludo()

    const otra_persona = {
        nombre: "Miguel",
        edad: 15,
        isDeveloper: false,
        saludo: function() {
            console.log('Hello')
        }
    }

    otra_persona.saludo()

    // Función factory
    const creaPersona = (nombre, edad, isDeveloper) => {
        return {
            nombre, // nombre: nombre
            edad,
            isDeveloper,
            saludo: function() {
                console.log('Hello')
            }
        }
    }

    const nueva_persona = creaPersona("Juan", 23, true)
    console.log(nueva_persona)

    const nueva_persona_2 = creaPersona("Maria", 44, false)
    ```

### Creación y uso de clases en JavaScript
+ instanciacion-clases.js:
    ```js
    class Persona {
        constructor(nombre, edad, isDeveloper) {
            this.nombre = nombre
            this.edad = edad
            this.isDeveloper = isDeveloper
        }

        saludo() {
            console.log(`Hola, mi nombre es ${this.nombre}, tengo ${this.edad} años.`)
        }
    }

    const nueva_persona = new Persona("Gorka", 34, true)
    console.log(nueva_persona)
    nueva_persona.saludo()

    let numero = 60 // inicializar
    console.log(typeof numero)

    let persona_2 = new Persona("Maria", 34, false) // instanciar
    console.log(typeof persona_2)
    console.log(persona_2 instanceof Persona)

    // instanceof -> similar a typeof pero para clases
    ```

### Ámbito de las clases, métodos y atributos públicos, privados y protegidos
+ atributos-metodos-privados-protegidos.js:
    ```js
    class Persona {
        // Private -> #
        // Private -> Sólo se puede acceder desde dentro de la clase
        #nombre
        #edad

        // Protected -> _
        // Protected -> Sólo se puede acceder desde dentro de la clase y desde clases descendientes
        _isDeveloper = true
        constructor(nom, edad) {
            this.#nombre = nom
            this.#edad = edad
        }

        saludo() {
            console.log(`Hola, mi nombre es ${this.nombre}, tengo ${this.edad} años.`)
        }

        obtenNombre() { // Función getter -> Nos permite acceder (de forma controlada) a algún atributo protegido
            return this.#nombre
        }

        #obtenEdad() {
            return this.#edad
        }

        getEdad() {
            return this.#edad
        }

        setEdad(nuevaedad) {
            this.#edad = nuevaedad
        }
    }

    const persona = new Persona("Gorka", 70)
    // console.log(persona)
    // console.log(persona.nombre)
    // persona.saludo()
    // console.log(persona.obtenNombre())
    // console.log(persona.#obtenEdad())
    // console.log(persona._isDeveloper)

    ////////////////////////

    // Getter -> métodos que nos permiten obtener atributos/métodos privados o protegidos
    const edad = persona.getEdad()
    console.log(edad)

    // Setter -> métodos que nos permiten cambiar el valor de alguno de los atributos privados o protegidos
    // Quiero cambiar la edad de la persona
    persona.setEdad(15)
    console.log(persona.getEdad())
    ```

### Getters y Setters en objetos
+ https://github.com/Open-Bootcamp/JavaScript-Basico/blob/main/sesion-11-programacion-orientada-a-objetos/atributos-metodos-privados-protegidos.js

### Herencia y Polimorfismo
+ herencia.js:
    ```js
    // Inheritance - Herencia
    class Persona {
        _nombre
        _edad
        constructor(nombre, edad) {
            this._nombre = nombre
            this._edad = edad
        }

        saludo() {
            console.log(`Hola, mi nombre es ${this._nombre}, tengo ${this._edad} años.`)
        }
    }

    class Desarrollador extends Persona {
        constructor(nombre, edad, lenguaje) {
            super(nombre, edad)
            this.lenguaje = lenguaje
        }

        saludo() { // Override
            super.saludo()
            console.log(`Y soy desarrollador de ${this.lenguaje}`)
        }
    }

    const nuevodev = new Desarrollador("Gorka", 34, "Javascript")
    console.log(nuevodev)
    nuevodev.saludo()

    // Polimorfismo => Varias formas
    ```

### Por qué no se habla de Interfaces en JavaScript y alternativas
+ **Contenido**: sobre las interfaces en JavaScript (realmenten no existen, pero si existen en TypeScript, que es un lenguaje derviado de JavaScript).

### Ejercicio
+ Crea un nuevo fichero JS que contenga las siguientes líneas:
    - Una clase llamada "Estudiante" que tenga:
        - Una variable llamada nombre.
        - Otra variable lista llamada asignaturas con 3 asignaturas: Javascript, HTML, CSS.
        - Un método "obtenDatos" que devuelva un objeto con las propiedades nombre y asignaturas.
    - Crea una nueva instancia de "Estudiante".
    - Haz la llamada al método obtenDatos.
+ **Resolución**:
    ```js
    class Estudiante {
        nombre = "Pedro"
        asignaturas = ['Javascript', 'HTML', 'CSS']

        obtenDatos() {
            return {
                nombre: this.nombre,
                asignaturas: this.asignaturas
            }
        }
    }

    const estudiante = new Estudiante
    const datos = estudiante.obtenDatos()
    console.log(datos)
    ```


## 12.Depuración de código
### Introducción a la Depuración en VSCode
+ index.js:
    ```js
    const persona = {
        nombre: "Gorka",
        edad: 34
    }

    console.log(persona)

    function obtenDobleEdad(edad) {
        return 2 * edad
    }

    const dobleEdad = obtenDobleEdad(persona.edad)

    console.log(dobleEdad)

    function obtenArray(edad) {
        let arrayNums = []
        for (let i = 0; i < 10; i++) {
            const numero = edad + i
            console.log(numero)
            arrayNums = [...arrayNums, numero]
        }
        return arrayNums
    }

    const array = obtenArray(persona.edad)

    console.log(array)
    ```

### Ejercicios
+ Crea un nuevo fichero JS que contenga las siguientes líneas:
    - Una función que admita un parámetro "num", y devuelva una lista con esa cantidad de números de la secuencia de Fibonacci (Por ejemplo: num = 6 => Resultado [1, 1, 2, 3, 5, 8]).
    - Ejecuta la depuración de VSCode para visualizar la ejecución de la función.
+ **Resolución**:
    ```js
    function fibonacci(num) {
        let serie = [1]
        let anterior = 0
        for(let i = 1; i < num; i++) {
            serie = [...serie, anterior + serie[i-1]]
            anterior = serie[i-1]
        }
        return serie
    }

    const prueba = fibonacci(6)
    console.log(prueba)
    ```


## 13.Configuracion y uso de ESLint
### Qué es el linting y ESLint
+ https://eslint.org

### Fichero de configuración ESLint
+ Crear **proyectos\004\13eslint\index.js**:
    ```js
    var nombre = "Gorka"

    var nombre2 = "Maria"

    var objeto = {
        nombre: "Círculo",
        radio: 2
    }
    ```
+ Crear archivo de configuración de reglas ESLint **proyectos\004\13eslint\\.eslintrc.json**:
    ```json
    {
        "rules": {
            "indent": [
                "error",
                4
            ],
            "linebreak-style": [
                "error",
                "windows"
            ],
            "quotes": [
                "error",
                "double"
            ],
            "semi": [
                "error",
                "never"
            ]
        }
    }
    ```

### Instalación y creación de ficheros de configuración personalizados
1. Crear carpeta **proyectos\004\13eslint\eslint-npm**.
2. Ejecutar:
    + $ npm init -y
    + $ npm i -D eslint
3. Crear **proyectos\004\13eslint\eslint-npm\index.js**:
    ```js
    // Este es el archivo que vamos a utilizar

    const nombre = "Gorka"

    /* eslint-disable */

    const persona2 = 'Maria';

    /* eslint-enable */

    // En esta línea quiero tener comillas simples (quiero que me desactives la regla de las comillas dobles)
    const nuevoString = 'Esto es un nuevo string'; // eslint-disable-line

    /* eslint-disable-next-line indent */
    const string2 = "Más strings"

    console.log("Hola")

    const persona3 = "Maria"

    const nombre3 = "Julián"

    console.log(4)
    ```
4. Ejecutar:
    + $ npm init @eslint/config
    + ? How would you like to use ESLint? ... 
        + > To check syntax, find problems, and enforce code style
    + ? What type of modules does your project use? ... 
        + > CommonJS (require/exports)
    + ? Which framework does your project use? ... 
        + > None of these
    + ? Does your project use TypeScript? » No / Yes
        + No
    + ? Where does your code run? ... 
        + √ Node
    + ? How would you like to define a style for your project? .
        + > Answer questions about your style
    + ? What format do you want your config file to be in? ... 
        + > JSON
    + ? What style of indentation do you use? ... 
        + > Spaces
    + ? What quotes do you use for strings? ... 
        + > Double
    + ? What line endings do you use? ... 
        + > Windows
    + ? Do you require semicolons? » No / Yes
        + No

### Reglas temporales y scrips para ejecución de ESLint en nuestro código
### Ejercicio
+ mmm
+ **Resolución**:
    ```js
    ≡
    ≡
    ```


## 14.Gestión de eventos
### Introducción a HTML con JS
+ proyectos\004\14eventos\index.html:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi primera web con Javascript</title>
        
    </head>
    <body>
        <h1>Hola mundo</h1>

        <p id="parrafo">Esto es un párrafo</p>
        <span id="myElement"></span>
        <script src="index.js"></script>

        <script src="https://unpkg.com/typeit@8.2.0/dist/index.umd.js"></script>
        <script src="animacion.js"></script>
    </body>
    </html>
    ```
+ proyectos\004\14eventos\index.js:
    ```js
    const a = 4
    const b = 8

    console.log(a * b)
    console.log("Hola")

    const p = document.getElementById("parrafo")

    console.log(p)
    ```
+ $ npm init -y
+ $ npm install --global http-server
+ proyectos\004\14eventos\package.json:
    ```json
    ≡
    "scripts": {
        "start": "http-server ."
    },
    ≡
    ```
+ $ npm start

### Utilización de librerías de terceros
+ proyectos\004\14eventos\animacion.js:
    ```js
    new TypeIt("#myElement", {
        strings: "Este es un texto personalizado",
    }).go();
    ```

### Manejo de eventos en JavaScript
+ proyectos\004\14eventos\formulario\index.html:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Formulario</title>
    </head>
    <body>
        Hola soy el formulario
        <form action="/" method="post" id="formulario">
            <input type="text" name="Nombre" placeholder="Cuál es tu nombre"></input>
            <input type="submit" value="Enviar"></input>
        </form>
    </body>
    <script src="index.js"></script>
    </html>
    ```
+ proyectos\004\14eventos\formulario\index.js:
    ```js
    const f = document.getElementById("formulario")

    console.log(f)

    f.addEventListener("submit", evento => {
        console.log(evento)
        evento.preventDefault()
    })
    ```

### Eventos personalizados
+ proyectos\004\14eventos\eventos\index.html:
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Eventos Personalizados</title>
    </head>
    <body>
        <h1 id="h-texto">Hola</h1>
    </body>
    <script src="index.js"></script>
    </html>
    ```
+ proyectos\004\14eventos\eventos\index.js:
    ```js
    const hTexto = document.getElementById("h-texto")

    console.log(hTexto)

    hTexto.addEventListener("cambioTexto", evento => {
        console.log(evento.detail)
        hTexto.innerText = evento.detail.texto
        hTexto.style.color = evento.detail.color
    })

    function cambiarTexto(nuevoTexto, color) {
        const evento = new CustomEvent("cambioTexto", {
            detail: {
                texto: nuevoTexto,
                color
            }
        })
        hTexto.dispatchEvent(evento)
    }
    ```

### JQuery
+ proyectos\004\14eventos\jquery\index.html:
    ```js
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Trabajando con JQuery</title>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <h1>Trabajando con JQuery</h1>
        <ul>
            <li id="el-1">Elemento 1</li>
            <li id="el-2">Elemento 2</li>
            <li id="el-3">Elemento 3</li>
        </ul>
        <button class="hide-btn">Hide</button>
        <button class="show-btn">Show</button>
        <br />
        <button class="new-element">Add Element</button>
    </body>
    <script src="index.js"></script>
    </html>
    ```
+ proyectos\004\14eventos\jquery\index.js:
    ```js
    // $(selector).acción()

    // $("h1").hide()

    // $(document).ready(() => {
    $(() => {
        // Selectores:
        // id="el-1" => "#el-1"
        // class="el-1" => ".el-1"
        // $("#el-1").hide()

        $(".hide-btn").click(() => {
            // $("h1").hide()
            $("h1").fadeOut()
        })
        $(".show-btn").click(() => {
            // $("h1").show()
            $("h1").fadeIn()
        })

        $("li").dblclick(() => {
            $("h1").css({ color: "red" })
        })

        $(".new-element").click(() => {
            // $("ul").append("<li>New Element</li>")
            $("ul").prepend("<li>New Element</li>")
        })

        $("li").mouseenter((elem) => {
            elem.target.style.color = "blue"
        })

        $("li").mouseleave(elem => {
            elem.target.style.color = "black"
        })

    })
    ```

### Alertas y Dialogos en pantalla
+ proyectos\004\14eventos\dialogos\index.html:
    ```js
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Diálogos</title>
    </head>
    <body>
        <h1>Diálogos por pantalla</h1>
        <button id="btn">Botón</button>
        <button id="info">Más información</button>
    </body>
    <script src="index.js"></script>
    </html>
    ```
+ proyectos\004\14eventos\dialogos\index.js:
    ```js
    const boton = document.querySelector("#btn")

    // console.log(boton)

    boton.addEventListener("click", () => {
        // alert("Se ha hecho click")
        // confirm("¿Estás de acuerdo?") && console.log("OK")
        // confirm("¿Estás de acuerdo?") 
        //     ? console.log("OK") 
        //     : console.log("NO!!")

        const respuesta = confirm("¿Seguro?")
        if (respuesta) {
            console.log("Estás de acuerdo")
        } else {
            console.log("NO estás de acuerdo")
        }
    })

    const botonInfo = document.querySelector("#info")
    botonInfo.addEventListener("click", () => {
        const nombre = prompt("¿Cuál es tu nombre?")
        if (nombre) {
            console.log("Tu nombre es " + nombre)
        } else {
            console.log("No has introducido nada")
        }
    })

    const lista = [{
        nombre: "Gorka",
        edad: 34
    }, {
        nombre: "Julen",
        edad: 21
    }, {
        nombre: "Amaia",
        edad: 30
    }]

    // console.log(lista)
    console.table(lista)
    ```

### Ejercicio
+ Crea un nuevo proyecto de Node
    - Instala la dependencia HTTP Server en entorno global (https://www.npmjs.com/package/http-server).
    - Crea un fichero index.html (utiliza el comando "!").
    - Crea un fichero index.js.
    - Integra el fichero index.js en el html.
    - Crea un botón en html (<button>Botón</button>).
    - Vincula un evento de tipo "click" al botón anterior, que muestre una alerta en el navegador "click en el botón".
    - Crea un script para lanzar un servidor de desarrollo con http-server.
    - Lanza el servidor de desarrollo a través del script anterior y prueba que el botón funciona correctamente.
    - Integra jQuery a través del CDN (https://releases.jquery.com/).
    - En el fichero index.js crea un evento click en el botón a través de jQuery, que muestre por consola "Hola, estoy utilizando jQuery".
+ **Resolución**:
    + $ npm init -y
    + $ npm install --global http-server
    + proyectos\004\14eventos\entrega\index.html
        ```html
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Entrega 14</title>
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        </head>
        <body>
            <button id="btn">Botón</button>
            <button class="btn-jquery">jQuery</button>
        </body>
        <script src="index.js"></script>
        </html>
        ```
    + proyectos\004\14eventos\entrega\index.js
        ```js
        const boton = document.querySelector("#btn")

        boton.addEventListener("click", () => {
            alert("click en el botón")
        })

        $("button").click(function() {
            console.log("Hola, estoy utilizando jQuery")
        })
        ```
    + proyectos\004\14eventos\entrega\package.json
        ```json
        ≡
        "scripts": {
            "start": "http-server ."
        },
        ≡
        ```
    + $ npm start

## 15.Persistencia de datos en navegador
### Persistencia de datos en navegador
+ proyectos\004\15persistencia\index.html:
    ```js
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Persistencia</title>
    </head>
    <body>
        
    </body>
    <script src="index.js"></script>
    </html>
    ```
+ proyectos\004\15persistencia\index.js:
    ```js
    // localStorage.setItem("nombre", "Gorka")
    // localStorage.setItem("nombre", "Miguel")

    // console.log(localStorage.getItem("nombre"))

    // localStorage.setItem("persona", JSON.stringify({ nombre: "gorka", edad: 32 }))

    // console.log(JSON.parse(localStorage.getItem("persona")))

    // JSON.stringify -> Convierte un objeto/array en string
    // JSON.parse -> Convierte un objeto/array convertido a través de stringify en un objeto de Javascript

    localStorage.removeItem("nombre")

    sessionStorage.setItem("nombre-sesion", "Gorka")

    /* Cookies */

    document.cookie = "nombreCookie=GorkaCookie"

    document.cookie = "nombreCaducidad=Nombre;expires=" + new Date(2023, 0, 1).toUTCString()

    console.log(document.cookie)
    ```

### Ejercicio
+ Crea un nuevo proyecto de Node:
    - Crea un fichero index.html (utiliza el comando "!").
    - Crea un fichero index.js.
    - Integra el fichero index.js en el html.
    - En el fichero index.js:
        - Crea una variable con tu nombre
        - Crea una variable con tu apellido
        - Crea un objeto con tu nombre y tu apellido
        - Almacena el objeto anterior en la SessionStorage
        - Almacena el objeto anterior en la LocalStorage
        - Crea una cookie que caduque en 2 minutos con los datos del objeto anterior
    - Observa en Google Chrome cómo se almacenan los datos en la SessionStorage, LocalStorage y las cookies
    - Cierra el navegador, comenta las líneas que almacenan SessionStorage, LocalStorage y CookieStorage y vuelve a abrirlo
    - Observa cómo la SessionStorage está vacía
    - Observa cómo la LocalStorage sigue manteniendo el objeto que has almacenado antes de cerrar el navegador
    - Observa cómo la cookie sigue manteniendo el objeto que has almacenado antes, aunque ya está caducado
+ **Resolución**:
    + $ npm init -y
    + proyectos\004\15persistencia\entrega\index.html
        ```html
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Persistencia de datos</title>
        </head>
        <body>    
        </body>
        <script src="index.js"></script>
        </html>
        ```
    + proyectos\004\15persistencia\entrega\index.js
        ```js
        let nombre = "Pedro"
        let apellido = "Bazó"
        let persona = {
            nombre,
            apellido
        }

        sessionStorage.setItem("persona", JSON.stringify(persona))
        localStorage.setItem("persona", JSON.stringify(persona))

        const now = new Date()
        `persona=${JSON.stringify(persona)};expires=${new Date(now.getTime() + 2 * 60000)}`
    ```


## 16.Aplicando Drag & Drop
### Drag and Drop con JavaScript
+ mmm:
    ```js
    ≡
    ≡
    ```

### Ejercicio
+ mmm
+ **Resolución**:
    ```js
    ≡
    ≡
    ```


## 17.Usado Geolocalización
### Inicialización de Mapas en HTML
+ mmm:
    ```js
    ≡
    ≡
    ```

### Geolocalización
+ mmm:
    ```js
    ≡
    ≡
    ```

### Ejercicio
+ mmmm:
    ```js
    ```
