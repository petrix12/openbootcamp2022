from django.shortcuts import render
from . models import Author, Genre, Book, BookInstance

def index(request):
    # num_books = Book.objects.all.count()
    num_books = Book.objects.count()
    # num_instances = BookInstance.objects.all.count()
    num_instances = BookInstance.objects.count()
    num_authors = Author.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact='a').count()

    return render(request, 'index.html', context={
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'disponibles': disponibles,
        'demo': 'Soluciones++'
    })
