from django.db import models

# Create your models here.
from django.db import models 

class producto (models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    disponible = models.BooleanField(default=True)


from mi_app.models import producto 
#crear un producto 
producto.objects.create(nombre='Laptop', precio=1500.99)
#consultar productos 
productos = producto.objects.all() 

