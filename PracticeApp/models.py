from django.db import models

SIGNOS = (
    ('Aries','Aries'),
    ('Tauro','Tauro'),
    ('Géminis','Géminis'),
    ('Cáncer','Cáncer'),
    ('Leo','Leo'),
    ('Virgo','Virgo'),
    ('Libra','Libra'),
    ('Escorpio','Escorpio'),
    ('Sagitario','Sagitario'),
    ('Capricornio','Capricornio'),
    ('Acuario','Acuario'),
    ('Piscis','Piscis'))

# Create your models here.
class Signo(models.Model):
    nombre=models.CharField(max_length=20)
    signo=models.CharField(max_length=12,choices=SIGNOS)