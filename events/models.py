from django.db import models

class EventModel(models.Model):
    id = models.AutoField(primary_key=True)
    denominacion = models.CharField(max_length=300, unique=True)
    MODALIDAD_CHOICES = [
        (1, 'Presencial'),
        (2, 'Virtual'),
        (3, 'Hibrida'),
    ]
    modalidad = models.IntegerField(choices=MODALIDAD_CHOICES)
    ubicacion = models.CharField(max_length=200)
    web = models.CharField(max_length=100, unique=True)
    mail = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    fecha_incio = models.TimeField()
    fecha_fin = models.TimeField()

    class Meta:
        db_table = 'eventos'

    
class PonentesModel(models.models):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(max_length=200)
    procedencia = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=20)
    resumen_cv = models.TextField()
    eje_tematico_id = models.IntegerField()

