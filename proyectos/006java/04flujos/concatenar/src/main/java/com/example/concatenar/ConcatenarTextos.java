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
