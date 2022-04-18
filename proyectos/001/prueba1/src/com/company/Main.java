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