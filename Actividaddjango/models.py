from django.db import models

# Create your models here.
# Define un modelo llamado Libro
class Libro(models.Model):
    titulo = models.CharField(max_length=100)  # Campo de texto para el título
    autor = models.CharField(max_length=100)   # Campo de texto para el autor
    genero = models.CharField(max_length=50)   # Campo agregado: género del libro

    def __str__(self):
        return self.titulo  # Representación del objeto como cadena
