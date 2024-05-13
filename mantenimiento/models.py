from django.db import models

# Create your models here.

from django.db import models

class Encargado(models.Model):
    IdEncargados = models.AutoField(primary_key=True)
    Cedula = models.CharField(max_length=10)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Nombres} {self.Apellidos}"

class Laboratorio(models.Model):
    IdLaboratorio = models.AutoField(primary_key=True)
    Numero = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=100)
    Responsable = models.ForeignKey(Encargado, on_delete=models.PROTECT)
    def __str__(self):
        return self.Codigo

class Estado(models.Model):
    IdEstado = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.Descripcion

class TipoMantenimiento(models.Model):
    IdTipoMantenimiento = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=100)
    def __str__(self):
        return self.Descripcion

class Equipo(models.Model):
    IdEquipo = models.AutoField(primary_key=True)
    Marca = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    SistemaOperativo = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=500)
    Estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    def __str__(self):
        return f"{self.IdEquipo} - {self.Marca}"


class Mantenimiento(models.Model):
    IdMantenimiento = models.AutoField(primary_key=True)
    IdTipoMantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.PROTECT)
    IdEquipo = models.ForeignKey(Equipo, on_delete=models.PROTECT)
    FechaIngreso = models.DateField()
    FechaSalida = models.DateField()
    DescripcionMantenimiento = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.IdTipoMantenimiento} - {self.IdEquipo} -  {self.FechaIngreso} - {self.FechaSalida} - {self.DescripcionMantenimiento}"
