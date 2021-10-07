from typing import ClassVar
from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField


SexoCliente = [
    [0, 'Hombre'],
    [1, 'Mujer'],
    [2, 'Otros']
]

RecibirOfertasEmail = [
    [0, 'No recibir ofertas al correo'],
    [1, 'Recibir ofertas al correo']
]

RolUsuario = [
    [1, 'Administrador'],
    [2, 'Vendedor'],
    [3, 'Gerente Asociación']
]

RubroProducto = [
    [1, 'Alimento'],
    [2, 'Electrodomésticos'],
    [3, 'Línea Blanca'],
    [4, 'Ropa']
]


# VER SOBRE LAS CODIGO VERIFICADOR DEL RUT.
class Cliente(models.Model):
    IdCliente = models.AutoField(primary_key=True)
    RutCliente = models.IntegerField()
    Nom_cliente = models.CharField(max_length=20)
    Ap_paterno = models.CharField(max_length=20)
    Sexo = models.IntegerField(choices=SexoCliente)
    Fecha_nac = models.DateField()
    Correo = models.EmailField(max_length=50)
    Recibir_Ofertas = models.IntegerField(choices=RecibirOfertasEmail)
    Nom_Usuario = models.CharField(max_length=30)
    Passwd = models.CharField(max_length=30)
    Puntos = models.IntegerField()
    FotoCliente = models.ImageField(null=True, upload_to="FotoClientes", default='/prueba.jpg')

    def __str__(self):
        return self.Nom_cliente

class Historial(models.Model):
    IdCliente = models.AutoField(primary_key=True)
    IdOferta = models.IntegerField(null=True, blank=True)
    IdCupon = models.IntegerField()
    FotoBoleta = models.ImageField(upload_to="FotoBoletas")
    Valoraciones = models.IntegerField(null=True)
    pag_visitadas = models.IntegerField(null=True)

class Cupon(models.Model):
     IdCupon = models.IntegerField(primary_key=True)
     RutConsu = models.IntegerField()


class Oferta(models.Model):
    IdOferta = models.IntegerField(primary_key=True)
    Oferta2x1 = models.TextField(max_length=100)
    TemporadaOferta = models.CharField(max_length=30)
    TopeProd = models.IntegerField()
    Descuento = models.IntegerField()
    EmailEnviados = models.IntegerField()
    FotoOferta = models.ImageField(upload_to="FotoBoleta")
    RutUsuario = models.IntegerField()

    def __str__(self):
        return self.Oferta2x1

class Usuario(models.Model):
    RutUsuario = models.IntegerField( primary_key=True)
    IdUsuario = models.IntegerField()
    IdOferta = models.IntegerField()
    IdConsulta = models.IntegerField()
    NomEncargado = models.CharField(max_length=50)

    def __str__(self):
        return self.NomEncargado

class Autenticar(models.Model):
    IdUsuario = models.IntegerField()
    RolUser = models.IntegerField(choices=RolUsuario)
    NomUser = models.CharField(max_length=20)
    PasswdUser = models.CharField(max_length=20)

    def __str__(self):
        return self.NomUser

class Producto(models.Model):
    IdProducto = models.IntegerField(primary_key=True)
    NomProducto = models.CharField(max_length=50)
    FotoProducto = models.ImageField(default='/prueba.jpg', upload_to="FotoProductos")
    PrecioNormal = models.IntegerField()
    PrecioOferta = models.IntegerField()
    StockProducto = models.IntegerField()
    LinkProducto = models.CharField(max_length=150)
    IdRubro = models.IntegerField()
    IdOferta = models.IntegerField()

    def __str__(self):
        return self.NomProducto

class ConsultaProducto(models.Model):
    IdProducto = models.IntegerField(primary_key=True)
    IdConsulta = models.IntegerField()
    IdTienda = models.IntegerField()
    RutUsuario = models.IntegerField()

class Tienda(models.Model):
    IdTienda = models.IntegerField(primary_key=True)
    NomTienda = models.CharField(max_length=50)
    DireccionTienda = models.CharField(max_length=100)

    def __str__(self):
        return self.NomTienda

class Rubro(models.Model):
    IdProducto = models.IntegerField()
    IdRubro = models.IntegerField(choices=RubroProducto)
    Rubro = models.CharField(max_length=30)

    def __str__(self):
        return self.Rubro










    





