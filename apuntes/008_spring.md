# Spring
+ **Instructor**: Alan Sastre
+ [Repositorio del curso](https://github.com/Open-Bootcamp/spring)


## 1.Introducción a Spring
### Vídeo del tema 1: Introducción a Spring
+ Página oficial de Spring: https://spring.io
+ Framework: https://spring.io/projects/spring-framework
+ Dependencias Maven: https://mvnrepository.com
+ Dependencias Maven para Spring: https://mvnrepository.com/search?q=org.springframework
+ Crear un proyecto **Spring** con **IntelliJ** desde **Maven**:
    1. Ejecutar **IntelliJ** y crear un nuevo proyecto.
    2. Seleccionar **Maven**.
    3. Dar nombre al proyecto (Por ejemplo: ob-spring-helloword) e indicar su localización.
    4. Ajustar el resto de los parámetros y presionar en **Create**.
+ Añadir la dependencia **Spring Context** al proyecto:
    1. Ir a https://mvnrepository.com/artifact/org.springframework/spring-context
    2. Seleccionamos la versión requerida (Ejemplo 5.3.22)
    3. Seleccionamos la dependencia Maven:
        ```xml
        <!-- https://mvnrepository.com/artifact/org.springframework/spring-context -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>5.3.22</version>
        </dependency>
        ```
    4. La copiamos y la pegamos en el archivo **pom.xml**:
    ```xml
    <project ...>
        ≡
        <dependencies>
            <dependency>
                <groupId>org.springframework</groupId>
                <artifactId>spring-context</artifactId>
                <version>5.3.22</version>
            </dependency>
        </dependencies>
    </project>
    ```
+ Inicializar contenedor:
    1. Crear archivo **proyectos\008spring\ob-spring-helloword\src\main\resources\beans.xml**:
        ```xml
        <?xml version="1.0" encoding="UTF-8"?>
        <beans xmlns="http://www.springframework.org/schema/beans"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://www.springframework.org/schema/beans
                https://www.springframework.org/schema/beans/spring-beans.xsd">

            <bean id="calculadora" class="org.example.Calculadora" scope="prototype">
            </bean>

            <bean id="gestorFacturas" class="com.example.GestorFacturas">
                <constructor-arg name="calculadora" ref="calculadora" />
                <constructor-arg name="nombre" value="Facturator 3000" />
            </bean>
        </beans>
        ```    
    2. Crear clase **proyectos\008spring\ob-spring-helloword\src\main\java\org\example\Calculadora.java**:
        ```java
        package org.example;

        public class Calculadora {
            public Calculadora(){
                System.out.println("Ejecutando constructor CalculatorService");
            }

            public String holaMundo(){
                return "Hola mundo!";
            }
        }
        ```
    3. Crear clase **proyectos\008spring\ob-spring-helloword\src\main\java\org\example\Main.java**:
        ```java
        package org.example;

        import org.springframework.context.ApplicationContext;
        import org.springframework.context.support.ClassPathXmlApplicationContext;

        public class Main {
            public static void main(String[] args) {
                ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

                // CONCEPTO 1: cómo obtener beans de Spring

                // Opción 1. Crear un objeto de forma normal
                // Calculadora service = new Calculadora();

                // Opción 2. Recibir un objeto de Spring
                Calculadora calculadora = (Calculadora) context.getBean("calculadora");
                String texto = calculadora.holaMundo();
                System.out.println(texto);
                // Se puede volver a obtener
                // OJO: se recupera el mismo objeto
                Calculadora calculadora2 = (Calculadora) context.getBean("calculadora");
                texto = calculadora.holaMundo();
                System.out.println(texto);

                // CONCEPTO 2: cargar un bean dentro de otro bean
                //GestorFacturas gestor = (GestorFacturas) context.getBean("gestorFacturas");
                //System.out.println(gestor.calculadora.holaMundo());

                // CONCEPTO 3: scope o alcance
                // los beans por defecto son singleton, se crea el objeto y se reutiliza para toda la aplicación
                // podemos cambiarlo a scope="prototype" si queremos que se cree un nuevo objeto cada vez
                // verificarlo viendo cómo se ejecuta varias veces un constructor
            }
        }
        ```

### Repositorio del curso


## 2.Spring Beans
### Vídeo del tema 2: Spring Beans
+ https://github.com/Open-Bootcamp/spring/tree/main/sesiones_1_2_3
1. Ejecutar IntelliJ.
2. Crear proyecto **Maven**:
    + Name: ob-spring-scan
3. Modificar archivo de configuración **proyectos\008spring\sesion02\pom.xml**:
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>org.example</groupId>
        <artifactId>ob-spring-scan</artifactId>
        <version>1.0-SNAPSHOT</version>

        <properties>
            <maven.compiler.source>18</maven.compiler.source>
            <maven.compiler.target>18</maven.compiler.target>
        </properties>

        <dependencies>
            <!-- https://mvnrepository.com/artifact/org.springframework/spring-context -->
            <dependency>
                <groupId>org.springframework</groupId>
                <artifactId>spring-context</artifactId>
                <version>5.3.10</version>
            </dependency>
        </dependencies>
    </project>
    ```
4. Crear archivo **proyectos\008spring\sesion02\src\main\resources\beans.xml**:
    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <beans xmlns="http://www.springframework.org/schema/beans"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:context="http://www.springframework.org/schema/context"
        xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context https://www.springframework.org/schema/context/spring-context.xsd">

        <context:component-scan base-package="com.example" />
    </beans>
    ```
5. Crear paquete **com.example** en **proyectos\008spring\sesion02\src\main\java**.
6. Crear clase **proyectos\008spring\sesion02\src\main\java\com\example\Calculadora.java**:
    ```java
    package com.example;

    import org.springframework.stereotype.Component;

    @Component
    public class Calculadora {
        public Calculadora(){
            System.out.println("Ejecutando constructor CalculatorService");
        }
        public String holaMundo(){
            return "Hola mundo!";
        }
    }
    ```
7. Crear clase **proyectos\008spring\sesion02\src\main\java\com\example\GestorFacturas.java**:
    ```java
    package com.example;

    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.beans.factory.annotation.Value;
    import org.springframework.stereotype.Component;

    @Component
    public class GestorFacturas {
        // 1. atributos
        Calculadora calculadora;

        //2. constructores

        public GestorFacturas(Calculadora calculadora){
            System.out.println("Ejecutando constructor GestorFacturas");
            this.calculadora = calculadora;
        }

        // 3. metodos....
    }
    ```
8. Crear clase principal **proyectos\008spring\sesion02\src\main\java\com\example\Main.java**:
    ```java
    package com.example;

    import org.springframework.context.ApplicationContext;
    import org.springframework.context.support.ClassPathXmlApplicationContext;

    public class Main {
        public static void main(String[] args) {
            ApplicationContext context = new ClassPathXmlApplicationContext("beans.xml");

            // CONCEPTO 1: cómo obtener beans de Spring

            // Opción 1. Crear un objeto de forma normal
            // Calculadora service = new Calculadora();

            // Opción 2. Recibir un objeto de Spring
            Calculadora calculadora = (Calculadora) context.getBean("calculadora");
            String texto = calculadora.holaMundo();
            System.out.println(texto);
            // Se puede volver a obtener
            // OJO: se recupera el mismo objeto
            Calculadora calculadora2 = (Calculadora) context.getBean("calculadora");
            texto = calculadora.holaMundo();
            System.out.println(texto);

            // CONCEPTO 2: cargar un bean dentro de otro bean
            GestorFacturas gestor = (GestorFacturas) context.getBean("gestorFacturas");
            System.out.println(gestor.calculadora.holaMundo());

            // CONCEPTO 3: scope o alcance
            // los beans por defecto son singleton, se crea el objeto y se reutiliza para toda la aplicación
            // podemos cambiarlo a scope="prototype" si queremos que se cree un nuevo objeto cada vez
            // verificarlo viendo cómo se ejecuta varias veces un constructor
        }
    }
    ```


## 3.Spring Data
### Vídeo del tema 3: Spring Data - Parte I
### Vídeo del tema 3: Spring Data - Parte II
1. Ir a https://start.spring.io
2. Dejar valores por defecto.
3. Añadir dependencias:
    + Spring Data JPA
    + H2 Database
        + **Nota**: Para ver las bases de datos H2 Database ir a: https://dbeaver.io
4. Generar proyecto y descargar en local.
5. Abrir proyecto con IntelliJ.
6. Crear clase (Entity) **proyectos\008spring\sesion03\prueba-sesion03\src\main\java\com\example\pruebasesion03\Coche.java**:
    ```java
    package com.example.pruebasesion03;

    import javax.persistence.Entity;
    import javax.persistence.GeneratedValue;
    import javax.persistence.GenerationType;
    import javax.persistence.Id;

    @Entity
    public class Coche {
        // atributos
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
        private String manufacturer;
        private String model;
        private Integer year;

        // constructores
        public Coche() {
        }

        public Coche(Long id, String manufacturer, String model, Integer year) {
            this.id = id;
            this.manufacturer = manufacturer;
            this.model = model;
            this.year = year;
        }

        // getter y setter
        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getManufacturer() {
            return manufacturer;
        }

        public void setManufacturer(String manufacturer) {
            this.manufacturer = manufacturer;
        }

        public String getModel() {
            return model;
        }

        public void setModel(String model) {
            this.model = model;
        }

        public Integer getYear() {
            return year;
        }

        public void setYear(Integer year) {
            this.year = year;
        }

        // tostring
        @Override
        public String toString() {
            return "Coche{" +
                    "id=" + id +
                    ", manufacturer='" + manufacturer + '\'' +
                    ", model='" + model + '\'' +
                    ", year=" + year +
                    '}';
        }
    }
    ```
7. Crear interface (Repository) **proyectos\008spring\sesion03\prueba-sesion03\src\main\java\com\example\pruebasesion03\CocheRepository.java**:
    ```java
    package com.example.pruebasesion03;

    import org.springframework.data.jpa.repository.JpaRepository;
    import org.springframework.stereotype.Repository;

    @Repository
    public interface CocheRepository extends JpaRepository<Coche, Long> {
    }
    ```
8. Modificar clase **proyectos\008spring\sesion03\prueba-sesion03\src\main\java\com\example\pruebasesion03\PruebaSesion03Application.java**:
    ```java
    package com.example.pruebasesion03;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.context.ApplicationContext;

    @SpringBootApplication
    public class PruebaSesion03Application {

        public static void main(String[] args) {
            // SpringApplication.run(PruebaSesion03Application.class, args);
            ApplicationContext context = SpringApplication.run(PruebaSesion03Application.class, args);
            CocheRepository repository = context.getBean(CocheRepository.class);

            System.out.println("find");
            System.out.println(repository.count());

            // Crear y almecenar un coche en base de datos
            Coche toyota = new Coche(null, "Toyota", "Corolla", 2010);
            repository.save(toyota);
            System.out.println("El número de coches en base de datos es: " + repository.count());

            // Recuperar todos
            System.out.println(repository.findAll());
        }
    }
    ```

### Sesión de dudas
### Ejercicios sesiones 1, 2 y 3
### Entrega ejercicio 1, 2 y 3


## 4.Spring Boot
### Video del tema 4: Spring Boot
1. Iniciar proyecto Spring Boot en **https://start.spring.io**:
    + Artifact: ob-rest-datajpa
    + Dependencias:
        + Spring Data JPA (SQL)
        + H2 Database (SQL)
        + Spring Web (WEB)
        + Spring Boot DevTools (DEVELOPER TOOLS)
2. Abrir proyecto con IntelliJ y ejecutar aplicación:
3. En caso de conflicto con el puerto, configurar nuevo puerto en **proyectos\008spring\sesion04\ob-rest-datajpa\src\main\resources\application.properties**:
    ```java
    server.port=8081
    ```
4. Crear archivo sobre inforamación del proyecto **proyectos\008spring\sesion04\ob-rest-datajpa\README.md**:
    ```md
    ## Spring Boot

    Proyecto Spring Boot con las dependencias / atartes:
    * Spring Data JPA (SQL)
    * H2 Database (SQL)
    * Spring Web (WEB)
    * Spring Boot DevTools (DEVELOPER TOOLS)

    Aplicación API REST con acceso a base de datos H2 para persistir la información.

    El acceso se puede realizar desde Postman o un navegador.

    ## Entidad Book
    1. Book
    2. BookRepository
    3. BookController
    ```
5. Crear entidad **Book** (proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\Book.java):
    ```java
    package com.example.obrestdatajpa;

    import javax.persistence.*;
    import java.time.LocalDate;

    @Entity
    @Table(name = "books")
    public class Book {
        // atributos
        @Id
        @GeneratedValue(strategy = GenerationType.IDENTITY)
        private Long id;
        private String title;
        private String autor;
        private Integer pages;
        private Double price;
        private LocalDate realeaseDate;
        private Boolean online;

        // constructores

        public Book() {
        }

        public Book(Long id, String title, String autor, Integer pages, Double price, LocalDate realeaseDate, Boolean online) {
            this.id = id;
            this.title = title;
            this.autor = autor;
            this.pages = pages;
            this.price = price;
            this.realeaseDate = realeaseDate;
            this.online = online;
        }

        // getter y setter
        public Long getId() {
            return id;
        }

        public void setId(Long id) {
            this.id = id;
        }

        public String getTitle() {
            return title;
        }

        public void setTitle(String title) {
            this.title = title;
        }

        public String getAutor() {
            return autor;
        }

        public void setAutor(String autor) {
            this.autor = autor;
        }

        public Integer getPages() {
            return pages;
        }

        public void setPages(Integer pages) {
            this.pages = pages;
        }

        public Double getPrice() {
            return price;
        }

        public void setPrice(Double price) {
            this.price = price;
        }

        public LocalDate getRealeaseDate() {
            return realeaseDate;
        }

        public void setRealeaseDate(LocalDate realeaseDate) {
            this.realeaseDate = realeaseDate;
        }

        public Boolean getOnline() {
            return online;
        }

        public void setOnline(Boolean online) {
            this.online = online;
        }
    }
    ```
6. Crear repositorio **BookRepository** (proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\BookRepository.java):
    ```java
    package com.example.obrestdatajpa;

    import org.springframework.data.jpa.repository.JpaRepository;
    import org.springframework.stereotype.Repository;

    @Repository
    public interface BookRepository extends JpaRepository<Book, Long> {
    }
    ```
7. Modificar **proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\ObRestDatajpaApplication.java**:
    ```java
    package com.example.obrestdatajpa;

    import org.springframework.boot.SpringApplication;
    import org.springframework.boot.autoconfigure.SpringBootApplication;
    import org.springframework.context.ApplicationContext;

    import java.time.LocalDate;

    @SpringBootApplication
    public class ObRestDatajpaApplication {

        public static void main(String[] args) {
            // SpringApplication.run(ObRestDatajpaApplication.class, args);
            ApplicationContext context = SpringApplication.run(ObRestDatajpaApplication.class, args);
            BookRepository repository = context.getBean(BookRepository.class);

            // CRUD
            // crear libro
            Book book1 = new Book(null, "Homo Deus", "Yval Noah", 450, 29.99, LocalDate.of(2018, 12, 1), true);
            Book book2 = new Book(null, "Homo Deus 2", "Yval Noah", 550, 19.99, LocalDate.of(2020, 12, 1), true);

            // almacenar un libro
            System.out.println("Libros en bd: " + repository.findAll().size());
            repository.save(book1);
            repository.save(book2);

            // recuperar todos los libros
            System.out.println("Libros en bd: " + repository.findAll().size());

            // borrar un libro
            repository.deleteById(1L);
            System.out.println("Libros en bd: " + repository.findAll().size());
        }
    }
    ```

## 5.Aplicaciones REST con Spring Boot
### Video del tema 5: Aplicaciones REST con Spring Boot
1. Crear paquetes:
    + **entities** (com.example.obrestdatajpa.entities).
    + **repository** (com.example.obrestdatajpa.repository).
    + **controller** (com.example.obrestdatajpa.controller).
2. Mover la entidad **Book** al paquete **entities** con IntelliJ para que se haga el refactoring.
3. Mover el repositorio **BookRepository** al paquete **repository** con IntelliJ para que se haga el refactoring.
4. Crear controlador **PruebaController** (proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\controller\PruebaController.java):
    ```java
    package com.example.obrestdatajpa.controller;

    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RestController;

    @RestController
    public class PruebaController {
        @GetMapping("/hola")
        public String holaMundo() {
            return "Hola Mundo";
        }

        @GetMapping("/prueba-bootstrap)")
        public String boostrap() {
            return  """
                    <!doctype html>
                    <html lang="en">
                        <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1">
                                <title>Bootstrap demo</title>
                                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">
                        </head>
                        <body>
                                <h1>Soluciones++ con Spring Boot</h1>
                                <a class="btn btn-primary" href="https://www.google.com">Google</a>
                                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>
                        </body>
                    </html>
                    """;
        }
    }
    ```
5. Crear controlador **BookController** (proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\controller\BookController.java):
    ```java
    package com.example.obrestdatajpa.controller;

    import com.example.obrestdatajpa.entities.Book;
    import com.example.obrestdatajpa.repository.BookRepository;
    import org.springframework.web.bind.annotation.GetMapping;
    import org.springframework.web.bind.annotation.RestController;

    import java.util.List;

    @RestController
    public class BookController {
        // ** ATRIBUTOS **
        private BookRepository bookRepository;

        // ** CONSTRUCTORES **
        public BookController(BookRepository bookRepository) {
            this.bookRepository = bookRepository;
        }

        // ** CRUD **
        // Read all
        /**
        * http://localhost:8080/api/books
        * @return
        */
        @GetMapping("/api/books")
        public List<Book> findAll(){
            // recuperar y devolver los libros de base de datos
            return bookRepository.findAll();
        }

        // Read id
        // Create
        // Update
        // Delete
    }
    ```
6. Para que la aplicación detecte los cambios automaticamente:
    + Ir a **File** -> **Settings**.
    + Ir a **Advanced Settings** -> **Compiler**:
        + Marcar: Allow auto-make ...
    + Ir a **Build, Execution, Deployment** -> **Compiler**:
        + Marcar: Build project automatically
7. En Postman o alguna aplicación similar:
    + Crear colección: **OB Spring REST Book**.
    + Crear request: **hola**.
        + Método: GET
        + URL: http://localhost:8080/hola
    + Crear request: **prueba-bootstrap**.
        + Método: GET
        + URL: http://localhost:8080/prueba-bootstrap
    + Crear request: **api/books**.
        + Método: GET
        + URL: http://localhost:8080/api/books
8. Acutualizar **proyectos\008spring\sesion04\ob-rest-datajpa\README.md**:
    ```md
    ≡
    3. BookController
        1. Buscar todos los libros
        2. Buscar un solo libro
        3. Crear un libro
        4. Actualizar un libro
        5. Borrar un libro
        6. Borrar todos los libros
    ```

## 6.Obteniendo valores de peticiones
### Video del tema 6: Obteniendo valores de peticiones
1. Modificar controlador **BookController** (proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\controller\BookController.java):
    ```java
    package com.example.obrestdatajpa.controller;

    import com.example.obrestdatajpa.entities.Book;
    import com.example.obrestdatajpa.repository.BookRepository;
    import org.springframework.http.HttpHeaders;
    import org.springframework.http.ResponseEntity;
    import org.springframework.web.bind.annotation.*;

    import java.util.List;
    import java.util.Optional;

    @RestController
    public class BookController {
        // ** ATRIBUTOS **
        private BookRepository bookRepository;

        // ** CONSTRUCTORES **
        public BookController(BookRepository bookRepository) {
            this.bookRepository = bookRepository;
        }

        // ** CRUD **

        // Read all
        /**
        * http://localhost:8080/api/books
        * @return
        */
        @GetMapping("/api/books")
        public List<Book> findAll(){
            // recuperar y devolver los libros de base de datos
            return bookRepository.findAll();
        }

        // Read id
        /*
        * Request
        * Response
        * @param id
        * @return
        */
        @GetMapping("/api/books/{id}")
        public ResponseEntity<Book> findOneById(@PathVariable Long id) {
            Optional<Book> bookOpt = bookRepository.findById(id);

            // opción 1
            if(bookOpt.isPresent())
                return ResponseEntity.ok(bookOpt.get());
            else
                return ResponseEntity.notFound().build();
            // opción 2
            /* return bookOpt.orElse(null); */
            // return bookOpt.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
        }

        // Create
        @PostMapping("/api/books")
        public Book create(@RequestBody Book book, @RequestHeader HttpHeaders headers){
            System.out.println(headers.get("User-Agent"));
            return bookRepository.save(book);
        }
        
        // Update
        // Delete
    }
    ```
2. En Postman o alguna aplicación similar:
    + Crear request: **api/books/id**.
        + Método: GET
        + URL: http://localhost:8080/api/books/1
    + Crear request: **post-api/books**.
        + Método: POST
        + URL: http://localhost:8080/api/books
        + Body:
            ```json
            {
                "title": "Libro nuevo",
                "autor": "María Bazó",
                "pages": 777,
                "price": 120.99,
                "realeaseDate": "2022-12-01",
                "online": false
            }
            ```

### Sesión de dudas
### Ejercicios sesiones 4, 5 y 6
+ Ejercicio 1:
    + Crear un proyecto Spring Boot con las dependencias:
        + H2
        + Spring Data JPA
        + Spring Web
        + Spring Boot dev tools
    + Crear una clase HelloController que sea un controlador REST. Dentro de la clase crear un método que retorne un saludo. Probar que retorna el saludo desde el navegador y desde Postman.
+ Ejercicio 2
    + Dentro de la misma app crear las clases necesarias para trabajar con "ordenadores":
        + Laptop (entidad)
        + LaptopRepository (repositorio)
        + LaptopController (controlador)
    + Desde LaptopController crear un método que devuelva una lista de objetos Laptop.
    + Probar que funciona desde Postman.
    + Los objetos Laptop se pueden insertar desde el método main de la clase principal.
+ Ejercicio 3
    + Crear un método en LaptopController que reciba un objeto Laptop enviado en formato JSON desde Postman y persistirlo en la base de datos.
    + Comprobar que al obtener de nuevo los laptops aparece el nuevo ordenador creado.

### Entrega ejercicios 4, 5 y 6
+ Ejercicio 1:
    1. Iniciar proyecto Spring Boot en **https://start.spring.io**:
        + Artifact: sesion07
    + Dependencias:
        + Spring Data JPA (SQL)
        + H2 Database (SQL)
        + Spring Web (WEB)
        + Spring Boot DevTools (DEVELOPER TOOLS)
    2. Abrir proyecto con IntelliJ y ejecutar aplicación:
    + **Nota**: En caso de conflicto con el puerto, configurar nuevo puerto en **...\src\main\resources\application.properties**:
        ```java
        server.port=8081
        ```
    3. Crear paquete **controller** (com.example.sesion07.controller).
    4. Crear controlador **HelloController** (...\src\main\java\com\example\sesion07\controller\HelloController.java):
        ```java
        package com.example.sesion07.controller;

        import org.springframework.web.bind.annotation.GetMapping;
        import org.springframework.web.bind.annotation.RestController;

        @RestController
        public class HelloController {
            @GetMapping("/hola")
            public String holaMundo() {
                return "Hola Mundo";
            }
        }
        ```
    5. En Postman o alguna aplicación similar:
        + Crear request:
            + Método: GET
            + URL: http://localhost:8080/hola
+ Ejercicio 2:
    1. Crear paquete **entities** (com.example.sesion07.entities).
    2. Crear entidad **Laptop** (proyectos\008spring\sesion04\ob-rest-datajpa\src\main\java\com\example\obrestdatajpa\Book.java):
        ```java
        package com.example.sesion07.entities;

        import javax.persistence.*;

        @Entity
        @Table(name = "laptops")
        public class Laptop {
            // atributos
            @Id
            @GeneratedValue(strategy = GenerationType.IDENTITY)
            private Long id;
            private String marca;
            private String modelo;
            private Integer ram;
            private Double price;

            // constructores
            public Laptop() {
            }

            public Laptop(Long id, String marca, String modelo, Integer ram, Double price) {
                this.id = id;
                this.marca = marca;
                this.modelo = modelo;
                this.ram = ram;
                this.price = price;
            }

            // getter y setter
            public Long getId() {
                return id;
            }

            public void setId(Long id) {
                this.id = id;
            }

            public String getMarca() {
                return marca;
            }

            public void setMarca(String marca) {
                this.marca = marca;
            }

            public String getModelo() {
                return modelo;
            }

            public void setModelo(String modelo) {
                this.modelo = modelo;
            }

            public Integer getRam() {
                return ram;
            }

            public void setRam(Integer ram) {
                this.ram = ram;
            }

            public Double getPrice() {
                return price;
            }

            public void setPrice(Double price) {
                this.price = price;
            }
        }
        ```
    3. Crear paquete **repository** (com.example.sesion07.repository).
    4. Crear repositorio **LaptopRepository** (...\src\main\java\com\example\sesion07\repository\LaptopRepository.java):
        ```java
        package com.example.sesion07.repository;

        import com.example.sesion07.entities.Laptop;
        import org.springframework.data.jpa.repository.JpaRepository;
        import org.springframework.stereotype.Repository;

        @Repository
        public interface LaptopRepository extends JpaRepository<Laptop, Long> {
        }
        ```
    5. Crear controlador **LaptopController** (...\src\main\java\com\example\sesion07\controller\LaptopController.java):
        ```java
        package com.example.sesion07.controller;

        import com.example.sesion07.entities.Laptop;
        import com.example.sesion07.repository.LaptopRepository;
        import org.springframework.web.bind.annotation.*;

        import java.net.http.HttpHeaders;
        import java.util.List;

        @RestController
        public class LaptopController {
            // ** ATRIBUTOS **
            private LaptopRepository laptopRepository;

            // ** CONSTRUCTORES **
            public LaptopController(LaptopRepository laptopRepository) {
                this.laptopRepository = laptopRepository;
            }

            // ** CRUD **
            // Read all
            /**
            * http://localhost:8080/api/laptops
            * @return
            */
            @GetMapping("/api/laptops")
            public List<Laptop> findAll(){
                // recuperar y devolver los libros de base de datos
                return laptopRepository.findAll();
            }
        }
        ```
    6. Modificar la clase principal del proyecto (...\src\main\java\com\example\sesion07\Sesion07Application.java):
        ```java
        package com.example.sesion07;

        import com.example.sesion07.entities.Laptop;
        import com.example.sesion07.repository.LaptopRepository;
        import org.springframework.boot.SpringApplication;
        import org.springframework.boot.autoconfigure.SpringBootApplication;
        import org.springframework.context.ApplicationContext;

        @SpringBootApplication
        public class Sesion07Application {

            public static void main(String[] args) {
                // SpringApplication.run(Sesion07Application.class, args);
                ApplicationContext context = SpringApplication.run(Sesion07Application.class, args);
                LaptopRepository repository = context.getBean(LaptopRepository.class);

                // CRUD
                // crear laptop
                Laptop laptop1 = new Laptop(null, "Lenovo", "XYZ", 12, 750.99);
                Laptop laptop2 = new Laptop(null, "Samsung", "ABC", 16, 950.99);

                // almacenar laptop
                repository.save(laptop1);
                repository.save(laptop2);
            }
        }
        ```
    7. En Postman o alguna aplicación similar:
        + Crear request:
            + Método: GET
            + URL: http://localhost:8080/api/laptops
+ Ejercicio 3:
    1. Modificar controlador **LaptopController** (...\src\main\java\com\example\sesion07\controller\LaptopController.java):
        ```java
        package com.example.sesion07.controller;

        import com.example.sesion07.entities.Laptop;
        import com.example.sesion07.repository.LaptopRepository;
        import org.springframework.web.bind.annotation.*;

        import java.net.http.HttpHeaders;
        import java.util.List;

        @RestController
        public class LaptopController {
            // ** ATRIBUTOS **
            private LaptopRepository laptopRepository;

            // ** CONSTRUCTORES **
            public LaptopController(LaptopRepository laptopRepository) {
                this.laptopRepository = laptopRepository;
            }

            // ** CRUD **
            // Read all
            /**
            * http://localhost:8080/api/laptops
            * @return
            */
            @GetMapping("/api/laptops")
            public List<Laptop> findAll(){
                // recuperar y devolver los libros de base de datos
                return laptopRepository.findAll();
            }

            // Create
            @PostMapping("/api/laptops")
            public Laptop create(@RequestBody Laptop laptop){
                return laptopRepository.save(laptop);
            }
        }
        ```
    2. Crear request:
        + Método: POST
        + URL: http://localhost:8080/api/laptops
        + Body:
            ```json
            {
                "marca": "HP",
                "modelo": "QPJ",
                "ram": 24,
                "price": 1120.99
            }
            ```

## 7.Devolviendo respuestas
### Video del tema 7: Devolviendo respuestas


    ```java
    ≡
    ```


## 8.Documentando con Swagger
### Video del tema 8: Documentando con Swagger



    ```java
    ≡
    ```




## 9.Aplicación REST con Spring Boot
### Video del tema 9: Aplicación REST con Spring Boot


    ```java
    ≡
    ```
### Ejercicios sesiones 7, 8 y 9
### Entrega ejercicios 7, 8 y 9


## 10.Builds en Aplicación REST con Spring Boot
### Video del tema 10: Builds en Aplicación REST con Spring Boot


## 11.Desplegando una Aplicación REST con Spring Boot
### Video del tema 11: Desplegando una Aplicación REST con Spring Boot


## 12.Añadiendo seguridad
### Video del tema 12: Añadiendo seguridad
### Ejercicios sesiones 10, 11 y 12
### Entrega ejercicios 10, 11 y 12


## 13.Sistemas de cifrado
### Video del tema 13: Sistemas de cifrado


## 14.Autenticación de usuarios con JWT
### Video del tema 14: Autenticación de usuarios con JWT


## 15.Aplicando JWT como método de autenticación
### Video del tema 15: Aplicando JWT como método de autenticación


## 16.Autenticación de usuarios con OAuth 2
### Vídeo del tema 16: Autenticación de usuarios con OAuth 2


## 17.Aplicando OAuth 2 como método de autenticación
### Vídeo del tema 17: Aplicando OAuth 2 como método de autenticación


## 18.Autorización de usuarios
### Vídeo del tema 18: Autorización de usuarios


## 19.Manejo de excepciones
### Vídeo del tema 19: Manejo de excepciones
### Sesión de dudas


## 20.Protección ante ataques con programación segura
### Vídeo del tema 20: Protección ante ataques con programación segura


## 21.Patrones de diseño existentes en Spring Security
### Vídeo del tema 21: Patrones de diseño existentes en Spring Security


## 22.Patrón Plantilla
### Vídeo del tema 22: Patrón Plantilla


## 23.Patrón Cadena de Responsabilidad
### Vídeo del tema 23: Patrón de Responsibilidad


## 24.Patrón de Estrategia
### Vídeo del tema 24: Patrón de Estrategia


## 25.Patrón de Proxy
### Vídeo del tema 25: Patrón de Proxy


## 26.Patrón de Constructor
### Vídeo del tema 26: Patrón de Contructor


## 27.Patrón Observador
### Vídeo del tema 27: Patrón de Observador


## 28.Patrón Decorador
### Vídeo del tema 28: Patrón Decorador


## 29.Despliegue de la aplicación
### Vídeo del tema 29: Despliegue de la aplicación


## 30.Mantenimiento en aplicaciones Spring
### Vídeo del tema 20: Mantenimiento en aplicaciones Spring


## 31.Tareas en el manejo de excepciones en Spring
### Vídeo del tema 31: Tareas en el manejo de excepciones en Spring


02-01-2023 - 23-01-2023