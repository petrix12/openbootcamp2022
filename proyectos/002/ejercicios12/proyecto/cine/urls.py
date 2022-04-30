from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas', views.peliculas, name='peliculas')
]