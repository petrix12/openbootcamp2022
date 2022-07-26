# Java Básico
+ **Instructor**: Víctor Román Archidona
+ [Resolución de ejercios](https://github.com/Open-Bootcamp/ResolucionEjercicios/tree/main/Java%20B%C3%A1sico)
+ [Repositorio del curso](https://github.com/Open-Bootcamp/java_basico)


## 1.Conceptos
### Entorno de desarrollo
+ https://openjdk.java.net
+ https://jdk.java.net/18
1. Descargar [JDK](https://download.java.net/java/GA/jdk18/43f95e8614114aeaa8e8a5fcf20a682d/36/GPL/openjdk-18_windows-x64_bin.zip.sha256).
2. Descomprimir el JDK en **C:\Users\bazop\jdks**.
3. Añadir la nueva ruta **C:\Users\bazop\jdks\jdk-18** a Variables de entorno (varibles del sistema):
    + Nombre: **JAVA_HOME**
    + Valor: **C:\Users\bazop\jdks\jdk-18**
4. Luego en **Varibles de usuario** editar la variable **path** y agregar la variable **C:\Users\bazop\jdks\jdk-18\bin**.
5. En una terminal para comprobar que la instalación fue exitosa, ejecutar:
    + $ java -version
6. Descargar e instalar [IntelliJ IDEA](https://www.jetbrains.com/es-es/idea/download/#section=windows).
7. Iniciar IntelliJ y dar click en **New Project** y seleccionar tipo **Java**.
8. Click en **Next** y seleccionar **Create project from template**.
9. Click en **Next** y establecer **Project name** en **prueba1** y **Project location** en **C:\xampp\htdocs\carrera\bootcamp\proyectos\001\prueba1**.
10. Modificar **proyectos\001\prueba1\src\com\company\Main.java**:
    ```java
    ≡
    public static void main(String[] args) {
	// write your code here
        System.out.println("Soluciones++");
    }
    ≡
    ```


### Hola mundo
1. Crear proyecto java con IntelliJ:
    + Name: hola
    + Group: com.pruebas
2. Crear clase **proyectos\006java\01conceptos\hola\src\main\java\com\pruebas\hola\HelloWord.java**:
    ```java
    package com.pruebas.hola;

    public class HelloWord {
        public static void main(String[] args){
            System.out.println("Hola mundo desde la clase HelloWord");
        }
    }
    ```
3. Crear clase **proyectos\006java\01conceptos\hola\src\main\java\com\pruebas\hola\ByWorld.java**:
    ```java
    package com.pruebas.hola;

    public class ByWorld {
        public static void main(String[] args) {
            System.out.println("Adios desde la clase ByWorld");
        }
    }
    ```

### Comentarios y documentación

### Variables y tipos de datos
+ Ejemplo de tipos de datos:
    ```java
    package com.example.tiposdatos;


    /**
    * Crear un proyecto java desde cero.
    * Crear un paquete.
    * Dentro del paquete crear una clase.
    * Dentro de la clase crear un método main
    * Imprimir todos los tipos de datos vistos.
    *
    * Tipos de datos mas comunes:
    * int, long, double, boolean, String
    */
    public class Tipos {

        public static void main(String[] args) {

            // 1. numericos


            // 1.1 enteros
            byte variable1 = 5;
            System.out.println(variable1);
            short variable2 = 10;
            int variable3 = 30;
            long variable4 = 100;
            long numeroTelefono = 666555444;
            // long precio = null;

            // 1.2 decimales
            float variable5 = 5.5f;
            double variable6 = 10.5d;
            variable6 = 20.5d;
            double precioSilla = 49.99;

            // 2. booleano
            boolean variable7 = false;
            boolean variable8 = true;

            // 3. texto
            char variable9 = 'a';
            String variable10 = "Lorem ipsum dolor sit amet.....";
        }
    }
    ```

### Operadores
+ Ejemplo de operadores:
    ```java
    package com.example.tiposdatos;

    public class Operadores {

        public static void main(String[] args) {

            // aritmeticos:
            int numero1 = 10;
            int numero2 = 20;
            int resultadoSuma = numero1 + numero2; // 30

            System.out.println(resultadoSuma);
            System.out.println(resultadoSuma + 5.77);

            int resultadoResta = numero1 - numero2;

            /*
            comparación:
            > mayor que
            < menor que
            >= mayor igual que
            <= menor igual que
            == igual que
            === IMPORTANTE: EN JAVA NO EXISTE!!!!
            */
            boolean resultado1 = numero1 > numero2; // false
            System.out.println(resultado1);

            boolean resultado2 = numero1 < numero2; // true
            System.out.println(resultado2);

            /*

            Lógicos
            and &&
            or ||
            */

            boolean resultado3 = numero1 > 5 && numero1 < 30;

            int edad = 17;
            boolean carnetJoven = edad >= 15 && edad <= 26;

            // operadores
            // incremento ++
            // decremento --

        }
    }
    ```

### Palabras reservadas

### Funciones y parámetros
+ Ejemplo de funciones:
    ```java
    package com.example.funciones;

    /**
    * Crear una funcion que reciba un precio y devuelva el precio con el IVA incluido
    */
    public class Funciones {
        static double getPrice() {
            return 100.99;
        }

        /**
        * void indica que no devuelve nada
        */
        static void showMenu(){
            System.out.println("Bienvenidos al E-commerce de zapatillas:");
            System.out.println("1 - Ver zapatillas");
            System.out.println("2 - Comprar zapatilla");
            System.out.println("3 - Salir");
        }

        static String getMenu(){
            System.out.println("Imprimiendo texto prueba");
            return "Bienvenidos al E-commerce de zapatillas: \n 1 - Ver zapatillas....";
        }

        public static void main(String[] args) {

            // opcion 1: funcion sin parámetros y sin tipo de retorno
    //         showMenu();
    //         showMenu();

            // opcion 2: funcion sin parámetros y con tipo de retorno
            String menu = getMenu();
            System.out.println(menu);
            System.out.println(getMenu());

            double price = getPrice();
            System.out.println(price);

            // opcion 3:
            // funcion con parametros y sin tipo de retorno
            imprimirSaludoBuenosDias("OpenBootcamp");

            // opcion4:
            // funcion con parámetros y con tipo de retorno
            String nombre = "Alan";
            String apellido = "Sastre";
            String saludo = obtenerSaludo(nombre, apellido);
            System.out.println(saludo);

            int resultadoSuma = suma(50, 200);
        }

        static int suma(int numero1, int numero2){
            return numero1 + numero2;
        }

        static String obtenerSaludo(String nombre, String apellido){
            return "Buenas tardes " + nombre + " " + apellido;
        }

        static void imprimirSaludoBuenosDias(String nombre){
            System.out.println("Buenas tardes " + nombre);
        }
    }
    ```
### Ámbito y retorno de una función

### Sobrecarga de funciones
+ Ejemplo de sobrecarga:
    ```java
    package com.example.funciones;

    /**
    * Sobrecarga permite duplicar un método siempre y cuando tengan diferente numero/tipo parametros.
    */
    public class Sobrecarga {

        public static void main(String[] args) {

        }

        static double suma(double numero1, double numero2){
            return numero1 + numero2;
        }

        static int suma(int numero1, int numero2){
            return numero1 + numero2;
        }

        static int suma(int numero1, int numero2, int numero3){
            return numero1 + numero2 + numero3;
        }
    }
    ```

### Sentencias if else
+ Ejemplo if else:
    ```java
    package com.example.estructurascontrol.condicionales;

    public class IfElseIf {

        public static void main(String[] args) {

            String dia = "DiaNostro";

            // ejemplos comparar
            boolean resultadoCompararNum = 5 == 5;
            boolean resultado = dia.equals("Martes");

            // if else if

            if (dia.equals("Lunes")) {
                System.out.println("Animo con la semana champions");

            } else if (dia.equals("Martes")) {
                System.out.println("Martes con M de Me besas");

            } else if (dia.equals("Miercoles")) {
                System.out.println("Miercoles con M de Me besas");

            } else if (dia.equals("Jueves")) {
                System.out.println("Ya es juernes");

            } else if (dia.equals("Viernes")) {
                System.out.println("Nos fuimos!");

            } else if (dia.equals("Sabado")) {
                System.out.println("Nos murimos!");

            } else if (dia.equals("Domingo")) {
                System.out.println("Depresión");
            } else {
                System.out.println("El día introducido no es un día válido.");
            }
        }
    }
    ```

### Bucles for
+ Ejemplo bocle for:
    ```java
    package com.example.estructurascontrol.repeticion;

    public class For {

        public static void main(String[] args) {

            for(int i = 0; i < 20; i++){
                // System.out.println("El valor de i es: " + i );
                // System.out.println("Hola mundo");
            }
                                // 0        1           2
            String[] nombres = {"Pepe", "Juanito", "Ruperta"}; // length 3
            for(int i = 0; i < nombres.length; i++){
                System.out.println(nombres[i]);
            }

            int suma = 0;
            int[] numeros = {5, 7, 8}; // length 3
            for(int i = 0; i < numeros.length; i++){
                // suma = suma + numeros[i];
                suma += numeros[i];
            }
        }
    }
    ```


### Bucles while

### Uso de continue y break
+ Código de ejemplo:
    ```java
    package com.example.estructurascontrol.repeticion;

    /**
    * Crear un bucle que permita concatenar textos y imprima el resultado final por consola.
    * Concatenar nombres
    * Los textos pueden venir de un array String
    * String[] nombres = {"", "", "", ""};
    */
    public class While {

        public static void main(String[] args) {

            int contador = 0;

            while(contador < 10){
                String nombre = "Prueba";
                contador++;
                if (contador == 5){
                    // break;
                    continue;
                }
                System.out.println("Valor de contador  " + contador);
            }
            // Variable nombre está fuera del ámbito del que se creó
            // System.out.println(nombre);
        }
    }
    ```

### Sentencias switch
+ Ejemplo de switch:
    ```java
    package com.example.estructurascontrol.condicionales;

    public class Switch {
        public static void main(String[] args) {

            String dia = "Martes";

            switch(dia){
                case "Lunes":
                    System.out.println("Hoy es Lunes!! Animo!!");
                    break;
                case "Martes":
                    System.out.println("Hoy es Martes!! Animo!!");
                    break;
                case "Miercoles":
                    System.out.println("Hoy es Miercoles!! Animo!!");
                    break;
                case "Jueves":
                    System.out.println("Hoy es Jueves!! Animo!!");
                    break;
                case "Viernes":
                    System.out.println("Hoy es Viernes!! Animo!!");
                    break;
                case "Sabado":
                    System.out.println("Hoy es Sabado!! Animo!!");
                    break;
                case "Domingo":
                    System.out.println("Hoy es Domingo!! Animo!!");
                    break;
                default:
                    System.out.println("No es un día válido");
            }
        }
    }
    ```

### Crear clases
+ Ejemplo de clase:
    ```java
    public class Triangulo {
        // atributos
        Double base;
        Double altura;

        // constructor
        public Triangulo(Double base, Double altura) {
            this.base = base;
            this.altura = altura;
        }

        // comportamiento
        public double area() {
            return this.base * this.altura / 2;
        }
    }
    ```

### Crear objetos
+ Ejemplo de creación de objeto (basado en la clase definida en el ejemplo anterior):
    ```java
    ≡
    public static void main(String[] args) {
       Triangulo triangulo = new Triangulo(3, 7);
       System.out.println(triangulo.area())
    }
    ≡
    ```

### Herencia
+ Ejemplo de una clase **CocheElectrico** heredando de una clase **Coche**:
    ```java
    ≡
    public class CocheElectrico extends Coche {

    }
    ≡
    ```

### El método super

### Sobreescritura

### Polimorfismo

### Clases abstractas

### Interfaces

### Técnicas de refactoring

### Métodos de la clase String

### Arrays

### Listas
1. Ejemplo para crear listas:
    ```java
    public com.example;

    import java.util.ArrayList;
    import java.util.List;

    public class ListMain {
        public static void main(String[] args) {
            List<String> nombres = mew ArrayList<>();

            nombre.add("Nombre 1");
            nombre.add("Nombre 2");
            nombre.add("Nombre 3");

            for(String nombre : nombres) {
                System.out.println(nombre);
            }
        }
    }
    ```

### Mapas
1. Ejemplo para crear mapas:
    ```java
    public com.example;

    import java.util.HashMap;
    import java.util.Map;

    public class MapMain {
        public static void main(String[] args) {
            Map<String, String> personas = mew HashMap<>();

            personas.put("123", "Juan");
            personas.put("124", "Pedro");
            personas.put("125", "Carlos");
            personas.put("126", "Alberto");

            for(String key : personas.keySet()) {
                System.out.println(key);
            }

            for(String value : personas.values()) {
                System.out.println(value);
            }

            for(Map.Entry<String, String> pair : personas.entrySet()) {
                System.out.println(pair.getKey() + " : " + pair.getValue());
            }
        }
    }
    ```

### Try catch finally

### Throw y throws

### IO estándar


## 2.IDE, archivos Java y sintaxis
### Instalación, configuración y uso del IDE



    ```java
    ≡
    ```


### Entrega ejercicios tema 1
+ Para este primer ejercicio tendréis que realizar lo siguiente:
    + Crea un proyecto de Java desde 0.
    + Dentro del proyecto tenéis que crear un paquete. En el paquete tendréis que crear una clase.
    + Dentro de la clase tenéis que crear el método main e imprimir todos los datos que se han visto en las sesiones.
+ Recordatorio: Los tipos de datos más comunes son int, long, double, boolean, String.
+ **Resolución**:
    1. Crear proyecto java con IntelliJ:
        + Name: sintaxis
        + Group: com.solucionespp
    2. Crear clase **proyectos\006java\02sintaxis\sintaxis\src\main\java\com\solucionespp\sintaxis\MainDatos.java**:
        ```java
        package com.solucionespp.sintaxis;

        public class MainDatos {
            public static void main(String[] args){
                // Imprimir todos los datos que se han visto en las sesiones.
                // Los tipos de datos más comunes son int, long, double, boolean, String.

                // numéricos entero
                byte variable1 = 3;
                System.out.println(variable1);
                short variable2 = 7;
                System.out.println(variable2);
                int variable3 = 12;
                System.out.println(variable3);
                long variable4 = 77;
                System.out.println(variable4);

                // numéricos decimal
                float variable5 = 5.7f;
                System.out.println(variable5);
                double variable6 = 12.3d;
                System.out.println(variable6);

                // booleano
                boolean variable7 = true;
                System.out.println(variable7);

                // texto
                char variable8 ='a';
                System.out.println(variable8);
                String variable9 = "Soluciones++";
                System.out.println(variable9);
            }
        }
        ```

### Enlace al repositorio


## 3.Funciones

Tipos de funciones en Java

Entrega ejercicios tema 2

## 4.Estructuras de control

Control del flujo en Java

Dudas Sesiones 1, 2 y 3

Entrega ejercicios tema 3

## 5.Clases, objetos, herencia y polimorfismo

Conceptos y usos de clases y objetos en Java

Entrega ejercicios tema 4

## 6.Interfaces

Estructura de las interfaces

Entrega ejercicios tema 5

## 7.Refactoring en Java

Refactorización y conceptos

Dudas Sesiones 4, 5 y 6

## 8.Tipo de datos avanzados

Datos avanzados en Java

## 9.Manejo de errores

Control de errores

## 10.Entrada/Salida

Input / Output

Entrega ejercicios temas 7, 8 y 9

## 11.Eventos, XML y JSON

Gestión de eventos y conceptos sobre tipos de archivos más usados

Dudas sesión 10