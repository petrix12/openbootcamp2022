# Java Básico
+ **Instructor**: Alan Sastre
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
+ https://github.com/Open-Bootcamp/java_basico


## 3.Funciones
### Tipos de funciones en Java



    ```java
    ≡
    ```

### Entrega ejercicios tema 2
+ Para este ejercicio tendréis que crear una función que reciba un precio y devuelva el precio con el IVA incluido.
+ **Resolución**:
+ Crear clase **proyectos\006java\03funciones\precio\src\main\java\com\example\precio\PrecioIVA.java**:
    ```java
    package com.example.precio;

    import java.util.Scanner;

    public class PrecioIVA {
        public static void main(String[] args) {
            double precio = getPrecio();
            System.out.println("Precio con IVA: " + precioIVA(precio));
        }

        static double getPrecio() {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Precio: ");
            double precio = scanner.nextDouble();
            return precio;
        }

        static double precioIVA(double precio) {
            double IVA = 0.1;
            return precio * (1 + IVA);
        }
    }
    ```


## 4.Estructuras de control
### Control del flujo en Java
1. Ejemplo de **if**:
    ```java
    package com.example.estructurascontrol.condicionales;

    public class If {
        public static void main(String[] args) {
            int edad = 19;
            boolean esMayor = edad >= 18; // false

            if(esMayor){
                System.out.println("Es mayor de edad");
            }

            if(edad >= 18){
                System.out.println("Es mayor de edad");
            }
        }
    }
    ```
2. Ejemplo de **if else**:
    ```java
    package com.example.estructurascontrol.condicionales;

    public class IfElse {
        public static void main(String[] args) {
            int edad = 16;

            if (edad >= 18) { // si true entra aquí
                System.out.println("Es mayor de edad");
            } else { // si false entra aquí
                System.out.println("Es menor de edad");
            }
        }
    }
    ```
3. Ejemplo de **if else if**:
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
                System.out.println("Ya es jueves");
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
4. Ejemplo de **switch case**:
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
5. Ejemplo de **for**:
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
6. Ejemplo de **for each**:
    ```java
    package com.example.estructurascontrol.repeticion;

    public class ForEach {
        public static void main(String[] args) {
            String[] nombres = {"Pepe", "Juanito", "Ruperta"};

            for(String nombre : nombres){
                System.out.println(nombre);
            }

            int[] numeros = {5, 10 , 15};

            int suma = 0;
            for(int numero : numeros){
                suma += numero;
            }
            System.out.println(suma);
        }
    }
    ```
7. Ejemplo de **while**:
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

### Dudas Sesiones 1, 2 y 3
1. Ejemplo de **Concatenar textos**:
    ```java
    package com.example.estructurascontrol.repeticion;

    public class ConcatenarTextos {
        public static void main(String[] args) {
            String[] nombres = {"Pepito", "Juanit", "eveready"};

            for(String nombre : nombres){

            }
        }
    }
    ```

### Entrega ejercicios tema 3
+ En este ejercicio tenéis que crear un bucle que permita concatenar textos e imprima el resultado final por consola.
+ Tened en cuenta que los textos pueden venir de un array de tipo String. Por ejemplo:
    + String[] nombres = {"", "", "", ""}
+ **Resolución**:
    ```java
    package com.example.concatenar;

    public class ConcatenarTextos {
        public static void main(String[] args) {
            String[] textos = {"Texto 1", "Texto 2", "Texto 3"};

            String textosConcatenados = "";
            for(String texto : textos){
                textosConcatenados += (texto + " ");
            }

            System.out.println("Textos concatenados: " + textosConcatenados);
        }
    }
    ```


## 5.Clases, objetos, herencia y polimorfismo
### Conceptos y usos de clases y objetos en Java
1. Ejemplo de clase **Main**:
    ```java
    package poo.clases;

    import poo.herencia.Camion;
    import poo.herencia.Coche;
    import poo.herencia.Motocicleta;

    public class Main {

        public static void main(String[] args) {

            // 1. clases y objetos
            // Clase identificador = new Clase();
            Vehiculo toyotaPrius = new Vehiculo();
            Motor motorGTI = new Motor("GTI", 190, 459.0, 6);

            Vehiculo fordMondeo = new Vehiculo("Ford", "Mondeo", 2.1, 2010, false, 0, motorGTI);

            System.out.println(fordMondeo.fabricante);
            System.out.println(fordMondeo.year);
            System.out.println(fordMondeo.speed); // 0
            fordMondeo.acelerar(50);
            System.out.println(fordMondeo.speed); // 50

            // 2. herencia
            Motocicleta kawasakiNinja = new Motocicleta();
            kawasakiNinja.fabricante = "Kawasaki";

            System.out.println("fin de programa");

            // 3. polimorfismo
            Vehiculo vehiculo;

            vehiculo = new Motocicleta();
            vehiculo.acelerar(50);

            vehiculo = new Coche();
            vehiculo.acelerar(50);

            vehiculo = new Camion();
            vehiculo.acelerar(50);

            // 4. clases abstractas: no se pueden instanciar, solo instancian las clases hijas
        }
    }
    ```
2. Ejemplo de clase **Vehiculo**:
    ```java
    package poo.clases;

    /**
    * Clase base o superclase o clase padre
    */
    public class Vehiculo {

        // 1. atributos
        protected String fabricante;
        protected String modelo;
        protected double cc;
        protected int year;
        protected boolean sport;
        protected int speed;
        protected Motor motor;

        // 2. constructores
        public Vehiculo(){

        }

        public Vehiculo(String fabricante, String modelo, double cc, int year, boolean sport, int speed, Motor motor) {
            this.fabricante = fabricante;
            this.modelo = modelo;
            this.cc = cc;
            this.year = year;
            this.sport = sport;
            this.speed = speed;
            this.motor = motor;
        }

        public Vehiculo(String fabricante, String modelo){
            this.fabricante = fabricante;
            this.modelo = modelo;
        }

        public Vehiculo(String fabricante, int year) {
            this.fabricante = fabricante;
            this.year = year;
        }

        // 3. métodos (comportamiento)
        public void acelerar(int quantity){
            this.speed += quantity;
        }

        // getter y setter

        // toString
    }
    ```
3. Ejemplo de clase **Motor**:
    ```java
    package poo.clases;

    public class Motor {
        // 1. atributos
        String modelo;
        int caballos;
        double parNm;
        int numCilindros;

        // 2. constructores
        public Motor(){
        }

        public Motor(String modelo, int caballos, double parNm, int numCilindros) {
            this.modelo = modelo;
            this.caballos = caballos;
            this.parNm = parNm;
            this.numCilindros = numCilindros;
        }

        // 3. métodos
    }
    ```
4. Ejemplo de clase para ejemplificar herencia **Motocicleta**:
    ```java
    package poo.herencia;

    import poo.clases.Motor;
    import poo.clases.Vehiculo;

    /**
    * Clase derivada o clase hija o subclase
    */
    public class Motocicleta extends Vehiculo {
        boolean baul;

        public Motocicleta(){

        }

        public Motocicleta(String fabricante, String modelo, double cc, int year, boolean sport, int speed, Motor motor, boolean baul) {
            super(fabricante, modelo, cc, year, sport, speed, motor);
            this.baul = baul;
        }
    }
    ```
5. Ejemplo de clase para ejemplificar herencia **Coche**:
    ```java
    package poo.herencia;

    import poo.clases.Vehiculo;

    public class Coche extends Vehiculo {

        int numPuertas;
    }
    ```
6. Ejemplo de clase para ejemplificar herencia **Camion**:
    ```java
    package poo.herencia;

    import poo.clases.Vehiculo;

    public class Camion extends Vehiculo {
        double capacidadCarga;

        public Camion(){
        }
    }
    ```

### Entrega ejercicios tema 4
+ En este ejercicio tendréis que crear una clase SmartDevice. Dentro crearéis las clases hijas: SmartPhone y SmartWatch.
+ Agregaréis atributos tal cual tendrían esos objetos en la realidad.
+ Crear constructor vacío y con todos los parámetros para cada clase.
+ Desde una clase Main: crearéis objetos de cada una y los utilizaréis para imprimir sus valores por consola.
+ **Resolución**:
    ```java
    package com.example.clases;

    public class SmartDevice {
        // Se ha llamado a la clase ejercicio4 para una mejor organización, pero es la SmartDevice
        String marca;
        String modelo;
        String color;

        public SmartDevice() {}

        public SmartDevice(String marca, String modelo, String color) {
            this.marca = marca;
            this.modelo = modelo;
            this.color = color;
        }

        public static class SmartPhone extends SmartDevice {
            int ram;
            String sistema;

            public SmartPhone() {
                super();
            }

            public SmartPhone(String marca, String modelo, String color, int ram, String sistema) {
                super(marca, modelo, color);
                this.ram = ram;
                this.sistema = sistema;
            }

            @Override
            public String toString() {
                return "marca=" + marca +
                        ", modelo=" + modelo +
                        ", color=" + color +
                        ", ram=" + ram +
                        ", sistema=" + sistema;
            }
        }

        public static class SmartWatch extends SmartDevice {
            double pulgadas;
            String conectividad;

            public SmartWatch() {
                super();
            }

            public SmartWatch(String marca, String modelo, String color, double pulgadas, String conectividad) {
                super(marca, modelo, color);
                this.pulgadas = pulgadas;
                this.conectividad = conectividad;
            }

            @Override
            public String toString() {
                return "marca=" + marca +
                        ", modelo=" + modelo +
                        ", color=" + color +
                        ", pulgadas=" + pulgadas +
                        ", conectividad=" + conectividad;
            }
        }

        public static void main(String[] args) {
            SmartPhone smartPhone = new SmartPhone("Samsung", "S10", "Azul",
                    8, "Android");

            SmartWatch smartWatch = new SmartWatch("Xiaomi", "Mi Band 6", "Negro",
                    3.5, "Bluetooth");

            System.out.println("El smartphone es: " + smartPhone + "\nEl smartwatch es: " + smartWatch);
        }
    }
    ```


## 6.Interfaces

### structura de las interfaces
1. Ejemplo de proyecto sin interfaces:
    1. Ejemplo de **Main.java**:
        ```java
        package poo.sininterfaces;

        import java.util.List;

        public class Main {
            public static void main(String[] args) {
        //        EmpleadoCRUDV1 empleadoCRUDV1 = new EmpleadoCRUDV1();
        //
        //        Empleado juanito = new Empleado("Juanito", 30, 40000, true);
        //        Empleado patricia = new Empleado("Patricia", 30, 40000, true);
        //        Empleado roberto = new Empleado("Roberto", 30, 40000, true);
        //
        //        System.out.println(juanito);
        //
        //        // guardar empleados
        //        empleadoCRUDV1.save(juanito);
        //        empleadoCRUDV1.save(patricia);
        //        empleadoCRUDV1.save(roberto);
        //
        //        // consultar empleados
        //        List<Empleado> empleados = empleadoCRUDV1.findAll();
        //        System.out.println(empleados);

                // usamos V2

                EmpleadoCRUDV2 empleadoCRUDV2 = new EmpleadoCRUDV2();

                Empleado juanito = new Empleado("Juanito", 30, 40000, true);
                Empleado patricia = new Empleado("Patricia", 30, 40000, true);
                Empleado roberto = new Empleado("Roberto", 30, 40000, true);

                System.out.println(juanito);

                // consultar empleados
                List<Empleado> empleados = empleadoCRUDV2.recuperarEmpleados();
                System.out.println(empleados);
            }
        }
        ```
    2. Ejemplo de **Empleado.java**:
        ```java
        package poo.sininterfaces;

        public class Empleado {

            // 1. atributos
            String nombre;
            int edad;
            double salario;
            boolean alta;

            // 2. constructores
            public Empleado(){}

            public Empleado(String nombre, int edad, double salario, boolean alta) {
                this.nombre = nombre;
                this.edad = edad;
                this.salario = salario;
                this.alta = alta;
            }

            // metodos

            @Override
            public String toString() {
                return "Empleado{" +
                        "nombre='" + nombre + '\'' +
                        ", edad=" + edad +
                        ", salario=" + salario +
                        ", alta=" + alta +
                        '}';
            }
        }
        ```
    3. Ejemplo de **EmpleadoCRUDV1.java**:
        ```java
        package poo.sininterfaces;

        import java.util.ArrayList;
        import java.util.List;

        /**
        * Create
        * Retrieve/Read
        * Update
        * Delete
        */
        public class EmpleadoCRUDV1 {
            // estructura de datos
            private List<Empleado> empleados = new ArrayList<>();

            // OPERACIONES CRUD

            // CREATE - guardar un empleado
            public void save(Empleado empleado){
                empleados.add(empleado);
            }

            public List<Empleado> findAll(){
                return empleados;
            }
        }
        ```
    4. Ejemplo de **EmpleadoCRUDV2.java**:
        ```java
        package poo.sininterfaces;

        import java.util.ArrayList;
        import java.util.List;

        public class EmpleadoCRUDV2 {

            public List<Empleado> recuperarEmpleados(){
                // conexion a base de datos
                List<Empleado> empleados = new ArrayList<>();
                return empleados;
            }
        }
        ```

2. Ejemplo de proyecto con interfaces:
    1. Ejemplo de **ZZZZZ**:
        ```java
        package poo.coninterfaces;

        import poo.sininterfaces.Empleado;

        public class Main {
            static EmpleadoCRUD empleadoCRUD;

            public static void main(String[] args) {
                empleadoCRUD.findAll();
                empleadoCRUD.save(new Empleado());
            }
        }
        ```
    2. Ejemplo de **EmpleadoCRUD.java**:
        ```java
        package poo.coninterfaces;

        import poo.sininterfaces.Empleado;
        import java.util.List;

        /**
        * Se declaran los métodos, no se implementan.
        *
        * Actúa como un contrato, dice lo que hay que hacer pero no lo hace
        */
        public interface EmpleadoCRUD {
            void save(Empleado empleado);
            List<Empleado> findAll();
            void delete(Empleado empleado);
        }
        ```
    3. Ejemplo de **EmpleadoCRUDMySQL.java**:
        ```java
        package poo.coninterfaces;

        import poo.sininterfaces.Empleado;
        import java.util.List;

        public class EmpleadoCRUDMySQL implements EmpleadoCRUD{
            @Override
            public void save(Empleado empleado) {
            }

            @Override
            public List<Empleado> findAll() {
                return null;
            }

            @Override
            public void delete(Empleado empleado) {
            }
        }
        ```
    4. Ejemplo de **EmpleadoCRUDExcel.java**:
        ```java
        package poo.coninterfaces;

        import poo.sininterfaces.Empleado;
        import java.util.List;

        public class EmpleadoCRUDExcel implements EmpleadoCRUD {
            @Override
            public void save(Empleado empleado) {
            }

            @Override
            public List<Empleado> findAll() {
                return null;
            }

            @Override
            public void delete(Empleado empleado) {
            }
        }
        ```

### Entrega ejercicios tema 5
+ Crear una interfaz CocheCRUD.
+ Crear una implementación CocheCRUDImpl que implemente la interfaz CocheCRUD.
+ Como métodos de CocheCRUD podemos poner:
    + save()
    + findAll()
    + delete()
    + que simplemente impriman por consola el nombre del propio método.
+ Desde una clase Main, Crear un objeto de tipo CocheCRUDImpl y llamar a cada uno de los métodos.
+ **Resolución**:
    + CocheCRUD
        ```java
        package com.example.demo;

        public interface CocheCRUD {
            void save();
            void findAll();
            void delete();
        }
        ```
    + CocheCRUDImpl
        ```java
        package com.example.demo;

        public class CocheCRUDImpl implements CocheCRUD{
            @Override
            public void save() {
                System.out.println("save");
            }

            @Override
            public void findAll() {
                System.out.println("findAll");
            }

            @Override
            public void delete() {
                System.out.println("delete");
            }
        }
        ```
    + Main
        ```java
        package com.example.demo;

        public class Main {
            public static void main(String[] args) {
                CocheCRUD cocheCrud = new CocheCRUDImpl();
                cocheCrud.save();
                cocheCrud.findAll();
                cocheCrud.delete();
            }
        }
        ```


## 7.Refactoring en Java
### Refactorización y conceptos
### Dudas Sesiones 4, 5 y 6


## 8.Tipo de datos avanzados

### Datos avanzados en Java
1. Ejemplo de **Datos.java**:
    ```java
    import java.math.BigDecimal;
    import java.util.*;

    public class Sesion7 {
        // En esta función suprimo los warnings de ConstantConditions, arrojados por los "if"
        // de starts/endsWith al ser siempre cierta/falsa la condición.
        @SuppressWarnings("ConstantConditions")
        public static void demoStrings() {
            // Declarar un string
            String cadena = "Esto es una cadena";

            // Obtener longitud de la cadena
            int cadenaLen = cadena.length();
            System.out.println(cadenaLen);

            // Convertir toda la cadena a minúsculas
            String cadenaMinus = cadena.toLowerCase();
            System.out.println(cadenaMinus);

            // Convertir toda la cadena a mayúsculas
            String cadenaMayus = cadena.toUpperCase();
            System.out.println(cadenaMayus);

            // Verificar si una cadena empieza por otra cadena
            if (cadena.startsWith("Es")) {
                System.out.println("La cadena empieza por \"Es\"'");
            }

            if (cadena.startsWith("hola")) {
                System.out.println("La cadena empieza por \"hola\"");
            }

            // Verificar si uan cadena finaliza por otra cadena
            if (cadena.endsWith("cadena")) {
                System.out.println("La cadena finaliza por \"cadena\"");
            }

            if (cadena.endsWith("adios")) {
                System.out.println("La cadena finaliza por \"adios\"");
            }

            // Imprimimr un string carácter a carácter
            for (int i = 0; i < cadena.length(); i++) {
                char caracter = cadena.charAt(i);
                System.out.println("Caracter: " + caracter);
            }
        }

        // Para mostar una copia de array a mano, hay una copia literal en un for abajo del todo.
        // Como esto es un warning, vamos a suprimirlo, ya que queremos mostrar el ejemplo.
        @SuppressWarnings("ManualArrayCopy")
        public static void demoArrays() {
            // Declarar un array
            int []arrayUno = new int[5];

            // Asignar valores a un array previamente declarado:
            arrayUno[0] = 1;
            arrayUno[1] = 2;
            arrayUno[2] = 3;
            arrayUno[3] = 4;
            arrayUno[4] = 5;

            // Declarar e inicializar un array
            String []arrayDos = {"Naranja", "Limon", "Pomelo"};

            // Recorrer un array:
            for (int i = 0; i < arrayUno.length; i++) {
                System.out.println("Posicion del array " + i + " contiene el valor " + arrayUno[i]);
            }

            // Recorrer un array con la forma corta:
            for (String citrico : arrayDos) {
                System.out.println("Cítrico actual " + citrico);
            }

            // Declarar un array multidimensional
            int [][]arrayBidiUno = new int[2][4];

            // Asignar valores a un array multidimensional previamente declarado:
            arrayBidiUno[0][0] = 1;
            arrayBidiUno[0][1] = 2;
            arrayBidiUno[0][2] = 3;
            arrayBidiUno[0][3] = 4;

            arrayBidiUno[1][0] = 10;
            arrayBidiUno[1][1] = 20;
            arrayBidiUno[1][2] = 30;
            arrayBidiUno[1][3] = 40;

            // Recorrer un array bidimensional:
            for (int i = 0; i < arrayBidiUno.length; i++) {
                for (int j = 0; j < arrayBidiUno[i].length; j++) {
                    System.out.println("Posición: [" + i + "][" + j + "] y contiene el valor " + arrayBidiUno[i][j]);
                }
            }

            // Declarar e inicializar un array multidimensional
            int [][]arrayBidiDos = {
                    {1, 2, 3, 4},
                    {10, 20, 30, 40},
            };

            // Recorrer un array bidimensional:
            for (int i = 0; i < arrayBidiDos.length; i++) {
                for (int j = 0; j < arrayBidiDos[i].length; j++) {
                    System.out.println("Posición: [" + i + "][" + j + "] y contiene el valor " + arrayBidiDos[i][j]);
                }
            }

            // "Crecer" un array.
            // Solo podemos hacerlo creando uno nuevo de más tamaño y llenándolo con el contenido del original.
            int nuevoArrayLen = arrayUno.length * 2;
            int []nuevoArray = new int[nuevoArrayLen];

            // Esto dará un warning: Copia manual del array
            for (int i = 0; i < arrayUno.length; i++) {
                nuevoArray[i] = arrayUno[i];
            }

            // Para copiar un array "elegántemente":
            System.arraycopy(nuevoArray, 0, arrayUno, 0, arrayUno.length);
        }

        public static void demoVector() {
            // Un vector es similar a un array, pero puede (de)crecer dinámicamente.
            Vector<Integer> vector = new Vector<>();

            // Añadir elementos
            vector.add(1);
            vector.add(2);
            vector.add(3);
            System.out.println("Contenido del vector: " + vector);

            // Quitar un elemento:
            vector.remove(1);
            System.out.println("Contenido del vector: " + vector);

            // Los vectores tienen capacidad y tamaño:
            System.out.println("Tamaño: " + vector.size() + " - Capacidad: " + vector.capacity());

            // Podemos ajustar la capacidad al tamaño actual:
            vector.trimToSize();
            System.out.println("Tamaño: " + vector.size() + " - Capacidad: " + vector.capacity());

            // Al añadir un elemento al vector, si superamos su capacidad, esta aumenta en capacityIncrement.
            // capacityIncrement se declara en el constructor del vector, y si es menor o igual a cero, por
            // defecto es el doble de la capacidad previa.
            vector.add(9);
            System.out.println("Tamaño: " + vector.size() + " - Capacidad: " + vector.capacity());

            // Recorrer un vector
            for (int i = 0; i < vector.size(); i++) {
                System.out.println("Valor en la posicion " + i + " del vector: " + vector.get(i));
            }

            // Recorrerlo con la forma corta:
            for (int i : vector) {
                System.out.println("Valor actual del vector: " + i);
            }

            // Comparar dos vectores
            Vector<Integer> vector2 = new Vector<>();
            vector2.add(1);
            vector2.add(3);
            vector2.add(9);

            if (vector.equals(vector2)) {
                System.out.println("Los dos vectores son equivalentes");
                System.out.println("    -> vector: " + vector);
                System.out.println("    -> vector: " + vector2);
            }
        }

        public static void demoList() {
            // Similares a los vectores, usando un array de forma subyacente.
            // No están sincronizados, es importante tenerlo en cuenta cuando necesitamos código "thread-safe".

            // Tambien varía la forma de aumentar su capacidad. Por defecto, el vector dobla la capacidad, y
            // el ArrayList aumenta con la formula "capacidad += capacidad * 0.5". En el constructor no podemos
            // darle un tamaño de autocrecimiento (a diferencia del Vector), y utiliza la formula previa.

            // Crear una lista de tipo ArrayList:
            ArrayList<String> lista = new ArrayList<>();

            // Añadir elementos
            lista.add("Uno");
            lista.add("Dos");
            lista.add("Tres");
            System.out.println("Contenido de la lista: " + lista);

            // Quitar un elemento:
            lista.remove("Dos");
            System.out.println("Contenido de la lista: " + lista);

            // Las listas tienen tamaño:
            System.out.println("Tamaño: " + lista.size());

            // Recorrer una lista
            for (int i = 0; i < lista.size(); i++) {
                System.out.println("Valor en la posicion " + i + " de la lista: " + lista.get(i));
            }

            // Recorrerlo con la forma corta:
            for (String e : lista) {
                System.out.println("Valor actual de la lista: " + e);
            }

            // Comparar dos listas
            ArrayList<String> lista2 = new ArrayList<>();
            lista2.add("Uno");
            lista2.add("Tres");

            if (lista.equals(lista2)) {
                System.out.println("Las dos listas son equivalentes");
                System.out.println("    -> lista: " + lista);
                System.out.println("    -> lista2: " + lista2);
            }

            // Podemos convertir una lista en un array:
            String []array = new String[lista.size()];
            for (int i = 0; i < lista.size(); i++) {
                array[i] = lista.get(i);
            }

            for (String elemento : array) {
                System.out.println("Elemento de la lista convertida en array es: " + elemento);
            }

            // Otra forma de hacer lo mismo:
            for (Object arrayObjeto : lista.toArray()) {
                System.out.println("Elemento de la lista convertida en array es: " + arrayObjeto.toString());
            }

            // Las listas pueden ser de más tipos, además de ArrayList:
            LinkedList<String> listaEnlazada = new LinkedList<>();

            // Y tienen las mismas operaciones que un ArrayList:
            listaEnlazada.add("Hola");
            System.out.println(listaEnlazada.get(0));
            listaEnlazada.remove("Hola");

            // Y pueden copiarse unas a otras
            LinkedList<String> listaEnlazadaDos = new LinkedList<>(lista);

            // Podemos recorrer nuestra nueva lista, tipo enlazada, y a la que hemos copiado
            // los valores desde "lista", que es del tipo ArrayList.
            for (String elemento : listaEnlazadaDos) {
                System.out.println("Elemento actual en la lista enlazada: " + elemento);
            }

            // Cada tipo de lista tiene sus pros y sus contras:
            // ArrayList:
            //  - Utiliza un array dinámico internamente
            //  - Es más rápida para almacenar y buscar datos
            //  - Solo implementa la interfaz "List", por lo que solo puede actuar como una lista
            //
            // LinkedList:
            //  - Utiliza una lista doblemente enlazada a nivel interno
            //  - Es más rápida para modificar datos
            //  - Puede funcionar como lista y como cola, ya que implementa las interfaces "List" y "Deque"
            //
            // Hay más tipos, ¡búscalos!
        }

        public static void demoMap() {
            // Los mapas implementan colecciones "clave" = "valor".

            // Crear un mapa del tipo "HashMap":
            HashMap<String, Integer> mapa = new HashMap<>();

            // Añadir elementos:
            mapa.put("clave1", 1);
            mapa.put("clave2", 2);
            mapa.put("clave3", 3);

            // Imprimir un valor de una clave del mapa accediendo a él:
            System.out.println("Valor de \"clave2\": " + mapa.get("clave2"));

            // Eliminar una clave del mapa:
            mapa.remove("clave2");

            // Un mapa no puede tener claves duplicadas, esto no se añadirá de nuevo, pero si reemplazará
            // su valor por "4":
            mapa.put("clave3", 4);
            System.out.println("Valor de \"clave3\": " + mapa.get("clave3"));

            // Un mapa puede cambiar el valor de una clave. Es más rapido reemplazar una clave que conozcamos
            // con replace que mediante mapa.put:
            mapa.replace("clave3", 100);

            // Recorrer un mapa:
            for (Map.Entry<String, Integer> elemento : mapa.entrySet()) {
                System.out.println("Clave: " + elemento.getKey() + " - Valor: " + elemento.getValue());
            }
        }

        public static void demoMath() {
            // Math es muy preciso con decimales utilizando BigDecimal.
            double valorInicial = 3.14f;
            BigDecimal valorA = BigDecimal.valueOf(valorInicial);

            double valorSecundario = 3.15f;
            BigDecimal valorB = BigDecimal.valueOf(valorSecundario);

            // Suma el BigDecimal "valorB" a "valorA"
            BigDecimal resultado = valorA.add(valorB);

            // Imprime la suma
            System.out.println(resultado);
        }
    }
    ```


## 9.Manejo de errores
### Control de errores


## 10.Entrada/Salida

### Input / Output

### Entrega ejercicios temas 7, 8 y 9
+ Escribe el código que devuelva una cadena al revés. Por ejemplo, la cadena "hola mundo", debe retornar "odnum aloh".
+ Crea un array unidimensional de Strings y recórrelo, mostrando únicamente sus valores.
+ Crea un array bidimensional de enteros y recórrelo, mostrando la posición y el valor de cada elemento en ambas dimensiones.
+ Crea un "Vector" del tipo de dato que prefieras, y añádele 5 elementos. Elimina el 2o y 3er elemento y muestra el resultado final.
+ Indica cuál es el problema de utilizar un Vector con la capacidad por defecto si tuviésemos 1000 elementos para ser añadidos al mismo.
+ Crea un ArrayList de tipo String, con 4 elementos. Cópialo en una LinkedList. Recorre ambos mostrando únicamente el valor de cada elemento.
+ Crea un ArrayList de tipo int, y, utilizando un bucle rellénalo con elementos 1..10. A continuación, con otro bucle, recórrelo y elimina los numeros pares. Por último, vuelve a recorrerlo y muestra el ArrayList final. Si te atreves, puedes hacerlo en menos pasos, siempre y cuando cumplas el primer "for" de relleno.
+ Crea una función DividePorCero. Esta, debe generar una excepción ("throws") a su llamante del tipo ArithmeticException que será capturada por su llamante (desde "main", por ejemplo). Si se dispara la excepción, mostraremos el mensaje "Esto no puede hacerse". Finalmente, mostraremos en cualquier caso: "Demo de código".
+ Utilizando InputStream y PrintStream, crea una función que reciba dos parámetros: "fileIn" y "fileOut". La tarea de la función será realizar la copia del fichero dado en el parámetro "fileIn" al fichero dado en "fileOut".
+ Sorpréndenos creando un programa de tu elección que utilice InputStream, PrintStream, excepciones, un HashMap y un ArrayList, LinkedList o array.
+ **Resolución**:
1. Ejemplo de **Ejercicio10.java**:
    ```java
    package com.example;

    import java.io.FileInputStream;
    import java.io.InputStream;
    import java.io.PrintStream;
    import java.util.Scanner;
    import java.util.*;

    public class ejercicios789 {

        /*
            Escribe el código que devuelva una cadena al revés.
            Por ejemplo, la cadena "hola mundo", debe retornar "odnum aloh".
        */

        public static class CadenaReves {
            public static void main(String[] args) {
                System.out.println("-------------------- \n Cadena al Reves\n--------------------");

                Scanner scanner = new Scanner(System.in);
                String texto;
                System.out.println("Introduce un texto");
                texto = scanner.nextLine();

                StringBuilder reves = new StringBuilder(texto);
                texto = reves.reverse().toString();

                System.out.println(texto);
            }
        }

        /*
            Crea un array unidimensional de Strings y recórrelo, mostrando únicamente sus valores.
        */

        public static class ArrayUnidimensional {
            public static void main(String[] args) {
                System.out.println("-------------------- \n Array Unidimensional\n--------------------");

                String textos[] = {"Principio ", "Intermedio ", "Conclusion "};

                for (String texto : textos) {
                    System.out.print(texto);
                }
            }
        }

        /*
            Crea un array bidimensional de enteros y recórrelo, mostrando la posición y el valor de cada elemento
            en ambas dimensiones.
        */

        public static class ArrayBidimensional {
            public static void main(String[] args) {
                System.out.println("-------------------- \n Array Bidimensional\n--------------------");

                Integer[][] numeros = {
                        {5, 10, 15},
                        {20, 25, 30}
                };

                for (int i = 0; i < numeros.length; i++) {
                    for (int y = 0; y < numeros[i].length; y++) {
                        System.out.println("Fila: " + (i + 1) + " | Columna: " + (y + 1) +
                                "\nEl valor es: " + numeros[i][y] + "\n");
                    }
                }
            }
        }

        /*
            Crea un "Vector" del tipo de dato que prefieras, y añádele 5 elementos.
            Elimina el 2o y 3er elemento y muestra el resultado final.
        */

        public static class EjercicioVector {
            public static void main(String[] args) {
                System.out.println("-------------------- \n Vector\n--------------------");

                Vector vector = new Vector();

                vector.add(1);
                vector.add(2);
                vector.add(3);
                vector.add(4);

                System.out.println("Vector antes de borrar: " + vector);

                vector.remove(2);
                vector.remove(1);

                System.out.println("Vector despues de borrar: " + vector + " -> Eliminados el 2 y 3");

                /*
                    Indica cuál es el problema de utilizar un Vector con la capacidad por defecto si tuviésemos
                    1000 elementos para ser añadidos al mismo.
                */

                System.out.println("\n-------------------- \n Respuesta\n--------------------");

                System.out.println("Desperdiciamos mucha memoria del sistema, ya que cada vez que se sobrepasa" +
                        " el limite establecido (Por defecto, 10) la dimension del vector se duplica.");
            }
        }

        /*
            Crea un ArrayList de tipo String, con 4 elementos. Cópialo en una LinkedList.
            Recorre ambos mostrando únicamente el valor de cada elemento.
        */

        public static class ArrayString {
            public static void main(String[] args) {

                System.out.println("-------------------- \n Array y LinkedList\n--------------------");

                ArrayList<String> lista = new ArrayList<String>();
                lista.add("Paco");
                lista.add("Ana");
                lista.add("Jesus");
                lista.add("Lucia");

                LinkedList<String> linkedlist = new LinkedList<String>();

                for (int i = 0; i < lista.size(); i++) {
                    linkedlist.add(i, lista.get(i));
                }

                System.out.println("Elementos del Array:");
                for (String elementos : lista) {
                    System.out.print(elementos + " ");
                }

                System.out.println("\n\nElementos de la LinkedList:");
                for (String elementos : linkedlist) {
                    System.out.print(elementos + " ");
                }
            }
        }

        /*
            Crea un ArrayList de tipo int, y, utilizando un bucle rellénalo con elementos 1..10.
            A continuación, con otro bucle, recórrelo y elimina los numeros pares. Por último, vuelve a recorrerlo
            y muestra el ArrayList final. Si te atreves, puedes hacerlo en menos pasos, siempre y cuando cumplas
            el primer "for" de relleno.
        */

        public static class ArrayInt {

            public static void main(String[] args) {

                System.out.println("-------------------- \n ArrayInt\n--------------------");

                ArrayList<Integer> lista = new ArrayList<Integer>();

                for (int i = 1; i < 11; i++) {
                    lista.add(i);

                    for (int num = 0; num < lista.size(); num++) {

                        if (lista.get(num) % 2 == 0) {
                            lista.remove(num);
                        }
                    }
                }

                System.out.println(lista);
            }
        }

        /*
            Crea una función DividePorCero. Esta, debe generar una excepción ("throws") a su llamante del tipo
            ArithmeticException que será capturada por su llamante (desde "main", por ejemplo). Si se dispara la excepción,
            mostraremos el mensaje "Esto no puede hacerse". Finalmente, mostraremos en cualquier caso: "Demo de código".
        */

        public static class DividePorCero {
            private static int Dividir(int a, int b) throws ArithmeticException {
                return a / b;
            }

            public static void main(String[] args) {
                System.out.println("-------------------- \n DividePorCero\n--------------------");

                Scanner scanner = new Scanner(System.in);
                System.out.println("Indica los numeros que quieres dividir: ");
                System.out.print("Numero 1: ");
                int a = scanner.nextInt();
                System.out.print("Numero 2: ");
                int b = scanner.nextInt();
                try {
                    System.out.println("Resultado: " + Dividir(a, b));
                } catch (ArithmeticException e) {
                    System.out.println("Esto no puede hacerse");
                } finally {
                    System.out.println("Demo de código");
                }
            }

        /*
            Utilizando InputStream y PrintStream, crea una función que reciba dos parámetros: "fileIn" y "fileOut".
            La tarea de la función será realizar la copia del fichero dado en el parámetro "fileIn" al fichero
            dado en "fileOut".
        */

            public static class CopiarFicheros {
                public static void main(String[] args) {

                    Scanner scanner = new Scanner(System.in);
                    System.out.println("Introduce el fichero de origen: ");
                    String fileIn = scanner.nextLine();
                    System.out.println("Introduce el fichero de destino: ");
                    String fileOut = scanner.nextLine();
                    copiar(fileIn, fileOut);
                }

                private static void copiar(String fileIn, String fileOut) {
                    try {
                        InputStream in = new FileInputStream(fileIn);
                        byte[] datos = in.readAllBytes();
                        in.close();

                        PrintStream out = new PrintStream(fileOut);
                        out.write(datos);
                        out.close();
                    } catch (Exception e) {
                        System.out.println("Excepcion: " + e.getMessage());
                    }
                }
            }
        }
    }
    ```


## 11.Eventos, XML y JSON

### Gestión de eventos y conceptos sobre tipos de archivos más usados
1. Ejemplo de **ZZZZZ**:
    ```java
    ≡
    ```

### Dudas sesión 10
1. Ejemplo de **ZZZZZ**:
    ```java
    ≡
    ```