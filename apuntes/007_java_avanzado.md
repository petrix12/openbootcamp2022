# Java Avanzado
+ **Instructor**: Víctor Román Archidona
+ [Repositorio del curso](https://github.com/Open-Bootcamp/java_avanzado)


## 1.Introducción y puesta en marcha
### Vídeo del tema 1: Introducción y puesta en marcha - Parte I
### Vídeo del tema 1: Introducción y puesta en marcha - Parte II
### Enlace al repositorio
+ Repositorio: https://github.com/Open-Bootcamp/java_avanzado


## 2.Programación funcional
### Vídeo del tema 2: Programación funcional
### Dudas sesiones 1 y 2


## 3.Rendimiento y recursión
### Vídeo del tema 3: Rendimiento y recursión
1. **Main.java**:
    ```java
    import sesion3.Sesion3;

    public class Main {
        public static void main(String []args) {
            System.out.println(Sesion3.factorialIterativo(5));
            System.out.println(Sesion3.factorialRecursivo(5));
            System.out.println(Sesion3.factorialFuncional(5));

            System.out.println(Sesion3.sumaIterativa(5));
            System.out.println(Sesion3.sumaRecursiva(5));
            System.out.println(Sesion3.sumaFuncional(5));

            Sesion3 sesion3 = new Sesion3();
            System.out.println(sesion3.sumaFuncionalVariable.apply(5));
        }
    }
    ```
2. **Sesion3.java**:
    ```java
    package sesion3;

    import java.util.function.Function;
    import java.util.stream.IntStream;
    import java.util.stream.Stream;

    public class Sesion3 {
        public Function<Integer,Integer> sumaFuncionalVariable = x -> IntStream.rangeClosed(1, x).reduce(0, (a, b) -> a + b);

        public static int factorialIterativo(int n) {
            int resultado = 1;

            for (int i = 1; i <= n; i++ ) {
                resultado *= i;
            }

            return resultado;
        }

        public static int factorialRecursivo(int n) {
            if (n == 0) {
                return 1;
            }

            // Usando "tail recursion":
            return n * factorialRecursivo(n-1);
        }

        public static int factorialFuncional(int n) {
            return IntStream.rangeClosed(1, n)
                    .reduce(1, (a, b) -> a * b);
        }

        public static int sumaIterativa(int n) {
            int result = 0;

            for (int i = 0; i <= n; i++) {
                result += i;
            }

            return result;
        }

        public static int sumaRecursiva(int n) {
            if (n == 1) {
                return 1;
            }

            return n + sumaRecursiva(n - 1);
        }

        public static int sumaFuncional(int n) {
            return IntStream.rangeClosed(1, n).reduce(0, (a, b) -> a + b);
        }


        public static IntStream fibonacciFuncional(int max) {
            return Stream.iterate(
                    new int[]{1, 1},
                    fib -> new int[] {fib[1], fib[0] + fib[1]}
            ).mapToInt(fib -> fib[0]);
        }
    }
    ```


## 4.Servicios REST
### Vídeo del tema 4: Servicios REST
1. Crear nuevo proyecto con **IntelliJ**:
    ```java
    ≡
    ```


## 5.Postman
### Vídeo del tema 5: Postman
    ```java
    ≡
    ```

### Entrega ejercicios 3, 4 y 5
    ```java
    ≡
    ```


## 6.Patrones de diseño
### Vídeo del tema 6: Patrones de diseño


## 7.Patrones creacionales
### Vídeo del tema 7: Patrones creacionales


## 8.Patrones estructurales
### Vídeo del tema 8: Patrones estructurales
### Ejercicios sesiones 6, 7 y 8
### Entrega ejercicios 6, 7 y 8


## 9.Patrones de comportamiento
### Vídeo del tema 9: Patrones de comportamiento


## 10.Refactoring en Java
### Vídeo del tema 10: Refactoring en Java


## 11.Introducción al código limpio en Java
### Vídeo del tema 11: Introducción al código limpio en Java
### Dudas sesiones 9, 10 y 11
### Ejercicios sesiones 9, 10 y 11
### Entrega ejercicios 9, 10 y 11


## 12.Nombrado
### Vídeo del tema 12: Nombrado


## 13.Las funciones
### Vídeo del tema 13: Las funciones


## 14.Documentación a través de comentarios
### Vídeo del tema 14: Documentación a través de los comentarios
### Ejercicios sesiones 12, 13 y 14
### Entrega ejercicios 12, 13 y 14


## 15.Formato
### Vídeo del tema 15: Formato


## 16.Procesamiento correcto de errores
## Vídeo del tema 16: Procesamiento correcto de errores


## 17.Objetos y la directiva de menor conocimiento
### Vídeo del tema 17: Objetos y la directiva de menor conocimiento


## 18.La organización de las clases
### Vídeo del tema 18: La organización de las clases
### Ejercicios sesiones 15, 16, 17 y 18
### Entrega ejercicios 15, 16, 17 y 18


## 19.Argumentos
### Vídeo del tema 19: Argumentos


## 20.Arquitectura limpia
### Vídeo del tema 20: Arquitectura limpia


## 21.Limpiando nuestros proyectos
### Vídeo del tema 21: Limpiando nuestros proyectos
### Dudas sesiones 19, 20 y 21
### Ejercicios sesiones 19, 20 y 21
### Entrega ejercicios 19, 20, 21


## 22.Aplicando la S de SOLID
### Vídeo del tema 22: Aplicando la S de SOLID


## 23.Aplicando la O de SOLID
### Vídeo del tema 23: Aplicando la L de SOLID


## 24.Aplicando la L de SOLID
### Vídeo del tema 24: Aplicando la L de SOLID
### Ejercicios sesiones 22, 23 y 24
### Entrega ejercicios 22, 23 y 24


## 25.Aplicando la I de SOLID
### Vídeo del tema 25: Aplicando la I de SOLID


## 26.Aplicando la D de SOLID
### Vídeo del tema 26: Aplicando la D de SOLID


## 27.Creación de proyectos con arquitectura limpia
### Vídeo del tema 27: Creación de proyectos con arquitectura limpia
### Ejercicios sesiones 25, 26 y 27
### Entrega ejercicios 25, 26, 27


## 28.Patrones y código limpio en el proyecto
### Vídeo del tema 28: Patrones y código limpio en el proyecto