from typing import ClassVar
from django.db import models
from django.db.models.base import Model


SexoCliente = [
    [0, 'Hombre'],
    [1, 'Mujer'],
    [2, 'Otros']
]

RecibirOfertasEmail = [
    [0, 'No recibir ofertas al correo'],
    [1, 'Recibir ofertas al correo']
]
class Cliente(models.Model):
    IdCliente = models.AutoField(max_length=4)
    RutCliente = models.IntegerField(max_length=9)
    Nom_cliente = models.CharField(max_length=20)
    Ap_paterno = models.CharField(max_length=20)
    Sexo = models.IntegerField(choices=SexoCliente)
    Fecha_nac = models.DateField()
    Correo = models.EmailField(max_length=50)
    Recibir_Ofertas = models.IntegerField(choices=RecibirOfertasEmail)
    Nom_Usuario = models.CharField(max_length=30)
    Passwd = models.CharField(max_length=30)
    Puntos = models.IntegerField(max_length=10)
    FotoCliente = models.ImageField(upload_to="FotoCliente")

    

class Historial(models.Model):
    IdCliente = models.AutoField(max_length=4)
    IdOferta = models.IntegerField(max_length=10)
    IdCupon = models.IntegerField(max_length=10)
    FotoBoleta = models.ImageField(upload_to="FotoBoleta")
    pag_visitadas = models.IntegerField(max_length=6)




