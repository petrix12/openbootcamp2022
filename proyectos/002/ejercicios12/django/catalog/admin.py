from django.contrib import admin

from . models import Author, Genre, Book, BookInstance

# Registrar modelos en el panle de administración
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(BookInstance)

