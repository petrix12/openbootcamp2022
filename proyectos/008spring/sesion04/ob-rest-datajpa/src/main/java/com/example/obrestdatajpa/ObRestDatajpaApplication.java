package com.example.obrestdatajpa;

import com.example.obrestdatajpa.entities.Book;
import com.example.obrestdatajpa.repository.BookRepository;
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
