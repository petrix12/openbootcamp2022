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
