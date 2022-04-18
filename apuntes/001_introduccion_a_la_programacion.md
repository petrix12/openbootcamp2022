# Introducción a la programación


## 1 Programación. Variables y constantes

### Vídeo sesión 1
+ **Contenido**: un poco de historia de la programación e introducción a variables y a constantes.

### Instalación Java e Intellij
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


## 2.Tipos de datos: primitivos y complejos

### Vídeo sesión 2
+ **Contenido**: sobre tipos de datos.

## 3.Funciones

### Vídeo sesión 3 parte 1
+ **Contenido**: sobre funciones, ambitos de variables y punteros.

### Vídeo sesión 3 parte 2
+ **Contenido**: sobre variables principalmente.

### Ejercicios tema 3
+ **Primera parte**:
    + Crear una función con tres parámetros que sean números que se suman entre sí.
    + Llamar a la función en el main y darle valores.
+ **Segunda parte**:
    + Crear una clase coche.
    + Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
    + Una función que incremente el número de puertas que tiene el coche.
    + Crear un objeto miCoche en el main y añadirle una puerta.
    + Mostrar el número de puertas que tiene el objeto.
+ **Resolución**:
    1. Iniciar IntelliJ y modificar el proyecto **prueba1**.
    2. Modificar **proyectos\001\prueba1\src\com\company\Main.java**:
        ```java
        package com.company;

        public class Main {

            public static void main(String[] args) {
                // Parte I
                System.out.println(suma(3, 7, 12));

                // Parte II
                Coche miCoche = new Coche();
                miCoche.AddPuerta();
                System.out.println("Puertas de mi coche: " + miCoche.puertas);
            }

            // Parte I
            public static int suma(int a, int b, int c) {
                return a + b + c;
            }
        }

        // Parte II
        class Coche {
            public int puertas = 0;

            public void AddPuerta() {
                this.puertas++;
            }
        }
        ```


## 4.Sentencias de control

### Vídeo sesión 4
+ Operadores lógicos.
+ Operadores de comparación.
+ Lógica booleana.
+ Tabla de la verdad.
+ Bucles.
+ Interruptores (select case).

### Ejercicios tema 4
+ En este ejercicio practicarás las estructuras de control, para ello deberás crear:
    + Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
        + Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
    + Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
        + Incrementar el valor de la variable en uno cada vez que se ejecute.
        + Mostrarlo por pantalla cada vez que se ejecute.
    + Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
    + Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.
    + Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.
+ **Resolución**:
    1. Iniciar IntelliJ y modificar el proyecto **prueba1**.
    2. Modificar **proyectos\001\prueba1\src\com\company\Main.java**:
        ```java
        package com.company;

        public class Main {

            public static void main(String[] args) {
                // PARTE I
                System.out.println("PARTE I");
                // Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
                int numeroIf = 3;

                if(numeroIf > 0) {
                    System.out.println("El número " + numeroIf + " es positivo");
                } else if(numeroIf == 0) {
                    System.out.println("El número " + numeroIf + " es igual a cero");
                } else {
                    System.out.println("El número " + numeroIf + " es negativo");
                }

                // PARTE II
                System.out.println("PARTE II");
                // Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3,
                // el bloque de código que tendrá el bucle deberá:
                //      + Incrementar el valor de la variable en uno cada vez que se ejecute.
                //      + Mostrarlo por pantalla cada vez que se ejecute.
                int numeroWhile = 0;
                while(numeroWhile < 3) {
                    numeroWhile++;
                    System.out.println("Número = " + numeroWhile);
                }

                // PARTE III
                System.out.println("PARTE III");
                // Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
                int numeroDoWhile = 3;
                do {
                    numeroWhile++;
                    System.out.println("Número = " + numeroWhile);
                } while(numeroDoWhile < 3);

                // PARTE IV
                System.out.println("PARTE IV");
                // Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será
                // que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute
                // y deberá mostrarse por pantalla.
                for(int numeroFor = 0; numeroFor <=3; numeroFor++){
                    System.out.println("Número = " + numeroFor);
                }

                // PARTE V
                System.out.println("PARTE V");
                // Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro
                // estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por
                // consola informando de la estación en la que está. También habrá que poner un default para cuando el
                // valor de la variable no sea una estación.
                String estacion = "VERANO";
                switch (estacion) {
                    case "VERANO":
                        System.out.println("La estación es VERANO");
                        break;
                    case "OTOÑO":
                        System.out.println("La estación es OTOÑO");
                        break;
                    case "INVIERNO":
                        System.out.println("La estación es INVIERNO");
                        break;
                    case "PRIMAVERA":
                        System.out.println("La estación es PRIMAVERA");
                        break;
                    default:
                        System.out.println("El valor " + estacion + " no se corresponde con ninguna estación");
                }
            }
        }
        ```

## 5.Errores

### Vídeo sesión 5
+ **Contenido**: sobre los errores comunes de los programadores.
    + Como nombrar las variables.
    + Comentar el código.
    + Construcción de funciones.
    + Uso adecuado en la definición del tipo de variables.
    + Optimización de la memoria.

## 6.Depuración de código

### Vídeo sesión 6
+ **Contenido**: sobre los depuradores.

## 7.Introducción a la Programación Orientada a Objetos

### Vídeo sesión 7
+ **Contenido**: sobre POO.


## 8.Privacidad, abstracción y encapsulación

### Vídeo sesión 8
+ **Contenido**: sobre la privacidad, la abstracción y la encalpsulación en la POO.

### Ejercicios tema 8
+ Para practicar la encapsulación:
    + Crear clase Persona.
    + Crear variables las privadas edad, nombre y telefono de la clase Persona.
    + Crear gets y sets de cada propiedad.
    + Crear un objeto persona en el main.
    + Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
+ **Resolución**:
    1. Iniciar IntelliJ y modificar el proyecto **prueba1**.
    2. Modificar **proyectos\001\prueba1\src\com\company\Main.java**:
        ```java
        package com.company;

        public class Main {

            public static void main(String[] args) {
                Persona persona = new Persona();

                persona.setEdad(50);
                persona.setNombre("Pedro");
                persona.setTelefono("0035-218-254.44.89");

                int edad = persona.getEdad();
                String nombre = persona.getNombre();
                String telefono = persona.getTelefono();

                System.out.println(nombre + " tiene " + edad + " años y su número es " + telefono);
            }
        }

        class Persona {
            private int edad;
            private String nombre;
            private String telefono;

            public void setEdad(int edad) {
                this.edad = edad;
            }

            public int getEdad() {
                return this.edad;
            }

            public void setNombre(String nombre) {
                this.nombre = nombre;
            }

            public String getNombre() {
                return this.nombre;
            }

            public void setTelefono(String telefono) {
                this.telefono = telefono;
            }

            public String getTelefono() {
                return this.telefono;
            }
        }
        ```

## 9.Herencia, Polimorfismo e Interfaces

### Vídeo sesión 9
+ **Contenido**: sobre herencia, polimorfismo e interfaces.

### Ejercicio tema 9
+ Crea una clase Persona con las siguientes variables:
    + La edad
    + El nombre
    + El teléfono
+ Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.
+ Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
+ Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.
+ **Resolución**:
    1. Iniciar IntelliJ y modificar el proyecto **prueba1**.
    2. Modificar **proyectos\001\prueba1\src\com\company\Main.java**:
        ```java
        package com.company;

        public class Main {

            public static void main(String[] args) {
                // Cliente
                Cliente cliente = new Cliente();

                cliente.setEdad(50);
                cliente.setNombre("Pedro");
                cliente.setTelefono("0035-218-254.44.89");
                cliente.setCredito(2500);

                int edadCliente = cliente.getEdad();
                String nombreCliente = cliente.getNombre();
                String telefonoCliente = cliente.getTelefono();
                double creditoCliente = cliente.getCredito();

                System.out.println(nombreCliente + " tiene " + edadCliente + " años, su número es " + telefonoCliente + " y tiene un crédito de " + creditoCliente);

                // Trabajador
                Trabajador trabajador = new Trabajador();

                trabajador.setEdad(35);
                trabajador.setNombre("Carlos");
                trabajador.setTelefono("0057-325-524.77.33");
                trabajador.setSalario(4500);

                int edadTrabajador = trabajador.getEdad();
                String nombreTrabajador = trabajador.getNombre();
                String telefonoTrabajador = trabajador.getTelefono();
                double salarioTrabajador = trabajador.getSalario();

                System.out.println(nombreTrabajador + " tiene " + edadTrabajador + " años, su número es " + telefonoTrabajador + " y tiene un salario de " + salarioTrabajador);
            }
        }

        class Persona {
            private int edad;
            private String nombre;
            private String telefono;

            public void setEdad(int edad) {
                this.edad = edad;
            }

            public int getEdad() {
                return this.edad;
            }

            public void setNombre(String nombre) {
                this.nombre = nombre;
            }

            public String getNombre() {
                return this.nombre;
            }

            public void setTelefono(String telefono) {
                this.telefono = telefono;
            }

            public String getTelefono() {
                return this.telefono;
            }
        }

        class Cliente extends Persona {
            private double credito;

            public void setCredito(double credito) {
                this.credito = credito;
            }

            public double getCredito() {
                return this.credito;
            }
        }

        class Trabajador extends Persona {
            private double salario;

            public void setSalario(double salario) {
                this.salario = salario;
            }

            public double getSalario() {
                return this.salario;
            }
        }
        ```

## 10.Métodos de clase

### Vídeo sesión 10
+ **Contenido**:
    + Sobre interfaces
    + Sobre paso de interfaces como paramétros a un función.
    + Sobre paso de variables por valor y por referencia.
    + Sobre recursividad.

## 11.Lenguajes: compilados e interpretados

### Vídeo sesión 11
+ **Contenido**:
    + Sobre como opera un compilador.
    + Sobre lenguajes compilados e interpretados.

### Vídeo ronda de preguntas
+ **Contenido**:
    + Ronda de preguntas y respuestas. 




    ```java
    ≡
    ≡
    ```