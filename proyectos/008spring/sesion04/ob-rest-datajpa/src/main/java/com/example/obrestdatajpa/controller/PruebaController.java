package com.example.obrestdatajpa.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PruebaController {
    @GetMapping("/hola")
    public String holaMundo() {
        return "Hola Mundo";
    }

    @GetMapping("prueba-bootstrap")
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
