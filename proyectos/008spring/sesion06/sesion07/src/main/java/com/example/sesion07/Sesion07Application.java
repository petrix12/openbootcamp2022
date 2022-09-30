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
