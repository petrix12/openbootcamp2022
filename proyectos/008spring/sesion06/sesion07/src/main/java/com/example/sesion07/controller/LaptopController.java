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
