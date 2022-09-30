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
