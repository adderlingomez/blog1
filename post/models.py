from django.db import models

# Create your models here.
from datetime import date





class post(models.model):
    titulo = models.CharField(max_length=40)
    cuerpo = models.TextField()
    fecha = models.DateField(default= date.today)