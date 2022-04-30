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
