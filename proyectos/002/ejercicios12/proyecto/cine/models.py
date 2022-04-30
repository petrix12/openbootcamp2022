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
        return '%s %s' % (self.first_name, self.last_name)