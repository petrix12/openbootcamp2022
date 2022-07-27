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
