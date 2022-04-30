# Instructivo para la construcción del proyecto
+ **Enunciado**:
    + En este ejercicio tendrás que crear una aplicación en Django que almacene datos de directores de cine y luego se puedan ver sus películas, así como una descripción de las mismas.
    + Tienes que personalizar el admin de la aplicación y a su vez crear las vistas de cada una de las partes de la aplicación.
1. Instalar Django en caso de no estar instalado:
    + $ pip install django
2. Crear proyecto Django **directores**:
    + $ django-admin startproject directores .
3. Lenvatar servidor web del proyecto:
    + $ python manage.py runserver
4. Crear aplicación **cine**:
    + $ python manage.py startapp cine
5. Conectar proyecto **directores** con la apliación **cine**:
    1. Modificar **proyectos\002\ejercicios12\proyecto\directores\settings.py**:
        ```py
        ≡
        # Application definition

        INSTALLED_APPS = [
            ≡
            'cine.apps.CineConfig'
        ]
        ≡
        ```
    2. Modificar **django\miproyecto\urls.py**:
        ```py
        ≡
        from django.contrib import admin
        from django.urls import path
        from django.urls import include
        from django.conf.urls.static import static, settings

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('cine/', include('cine.urls'))
        ] + static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)
        ```
    3. Crear **proyectos\002\ejercicios12\proyecto\cine\urls.py**:
        ```py
        from django.urls import include, path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
            path('/peliculas', views.peliculas, name='peliculas')
        ]
        ```
6. Preparar base de datos (migraciones):
    + $ python manage.py makemigrations
    + $ python manage.py migrate
7. Crear superusuario:
    + $ python manage.py createsuperuser
    + Username (leave blank to use 'bazop'): admin
    + Email address: bazo.pedro@gmail.com (Se puede dejar en blanco)
    + Password: admin
    + Password (again): admin
    + Bypass password validation and create user anyway? [y/N]: y
8. Crear modelos asociados a **cine** en **proyectos\002\ejercicios12\proyecto\cine\models.py**:
    ```py
    from django.db import models
    from django.urls import reverse
    import uuid

    # Create your models here.

    class Pelicula(models.Model):
        title = models.CharField(max_length=64, help_text="Indica el título de la película")
        description = models.TextField(max_length=100, help_text="Indica la descripción del película")
        director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)

        def __str__(self):
            return self.title

    class Director(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharField(max_length=100)
        date_of_birth = models.DateField(null=True, blank=True)
        date_of_death = models.DateField('Died', null=True, blank=True)

        def get_absolute_url(self):
            return reverse('author-detail', args=[str(self.id)])

        def __str__(self):
            return '%s %s' % (self.last_name, self.first_name)
    ```
9. Ejecutar cambios en la base de datos:
    + $ python manage.py makemigrations     (etablece la migraciones)
    + $ python manage.py migrate            (ejecuta las migraciones)
10. Registrar modelos en **proyectos\002\ejercicios12\proyecto\cine\admin.py**:
    ```py
    from django.contrib import admin
    from . models import Pelicula, Director

    # Registrar modelos en el panel de administración
    admin.site.register(Pelicula)
    admin.site.register(Director)
    ```
11. Diseñar vista **proyectos\002\ejercicios12\proyecto\cine\views.py**:
    ```py
    from django.shortcuts import render
    from . models import Pelicula, Director

    def index(request):
        directores = Director.objects.all()
        
        # num_authors = Author.objects.all().count()
        # disponibles = BookInstance.objects.filter(status__exact='a').count()

        return render(request, 'index.html', context={
            'directores': directores,
            'demo': 'Soluciones++'
        })

    def peliculas(request):
        director = request.GET.get('director', None)
        peliculas = Pelicula.objects.all()
        peliculasFiltradas = []
        for pelicula in peliculas:
            if director in str(pelicula.director):
                peliculasFiltradas.append(pelicula)

        return render(request, 'peliculas.html', context={
            'director': director,
            'peliculasFiltradas': peliculasFiltradas
        })
    ```
12. Crear plantilla **proyectos\002\ejercicios12\proyecto\cine\templates\plantilla.html**:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        {% block title %}<title>Directores de cine</title>{% endblock %}
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <!-- CSS only -->
        <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous"> -->

        {% load static %}
        <link rel="stylesheet" href="{% static 'css/style.css' %}">
    </head>
    <body>
        <div class="container">
            {% block content %}{% endblock %}
        </div>
    </body>
    </html>
    ```
13. Crear vista **proyectos\002\ejercicios12\proyecto\cine\templates\index.html**:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        {% extends "plantilla.html" %}

        {% block content %}

        <h1>Directores de cine</h1>
        {% for director in directores %}
            <p>{{ director }} - <a href="peliculas?director={{director}}">Ver películas</a></p>
        {% endfor %}

        <hr>

        {% endblock %}
    </body>
    </html>
    ```
14. Crear vista **proyectos\002\ejercicios12\proyecto\cine\templates\peliculas.html**:
    ```html
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        {% extends "plantilla.html" %}

        {% block content %}

        <h1>Peliculas dirigida por {{ director }}</h1>
        {% for pelicula in peliculasFiltradas %}
            <p>Título: {{ pelicula.title }}</p>
            <p>Descripción: {{ pelicula.description }}</p>
            <hr>
        {% endfor %}
        <a href="javascript: history.go(-1)">Volver</a>
        {% endblock %}
    </body>
    </html>
    ```
15. Crear archivo de estilos **proyectos\002\ejercicios12\proyecto\cine\static\css\styles.css**:
    ```css
    /* Aquí van los estilos */
    ```