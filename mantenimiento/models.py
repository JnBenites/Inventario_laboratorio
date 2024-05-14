from django.contrib.auth.models import User
from django.db import models

class Encargado(models.Model):
    IdEncargado = models.AutoField(primary_key=True)
    Cedula = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name} - {self.user.email}'

class Laboratorio(models.Model):
    IdLaboratorio = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=100)
    Responsable = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Codigo} {self.Nombre} - {self.Responsable.first_name} {self.Responsable.last_name}'

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

class Case(models.Model):
    IdCase = models.AutoField(primary_key=True)
    CaseSerial = models.CharField(max_length=200)
    Observacion = models.TextField()
    FechaIngreso = models.DateField()

    def __str__(self):
        return str(self.CaseSerial)

class Monitor(models.Model):
    IdMonitor = models.AutoField(primary_key=True)
    MonitorSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Resolucion = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()

    def __str__(self):
        return str(self.MonitorSerial)

class Teclado(models.Model):
    IdTeclado = models.AutoField(primary_key=True)
    TecladoSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Distribucion = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()

    def __str__(self):
        return str(self.TecladoSerial)

class Raton(models.Model):
    IdRaton = models.AutoField(primary_key=True)
    RatonSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return str(self.RatonSerial)

class Parlante(models.Model):
    IdParlante = models.AutoField(primary_key=True)
    ParlanteSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return str(self.ParlanteSerial)

class Impresora(models.Model):
    IdImpresora = models.AutoField(primary_key=True)
    ImpresoraSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return str(self.IdImpresora)

class Proyector(models.Model):
    IdProyector = models.AutoField(primary_key=True)
    ProyectorSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return str(self.IdProyector)

class Ups(models.Model):
    IdUps = models.AutoField(primary_key=True)
    UpsSerial = models.CharField(max_length=200)
    Marca = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return str(self.IdUps)

class Equipo(models.Model):
    IdEquipo = models.AutoField(primary_key=True)
    SistemaOperativo = models.CharField(max_length=100)
    Descripcion = models.CharField(max_length=500)
    Estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    Case = models.ForeignKey(Case, on_delete=models.PROTECT, null=True)
    Monitor = models.ForeignKey(Monitor, on_delete=models.PROTECT, null=True)
    Teclado = models.ForeignKey(Teclado, on_delete=models.PROTECT, null=True)
    Raton = models.ForeignKey(Raton, on_delete=models.PROTECT, null=True)
    Parlante = models.ForeignKey(Parlante, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return f'{self.IdEquipo} - {self.SistemaOperativo} - {self.Descripcion}'

class Mantenimiento(models.Model):
    IdMantenimiento = models.AutoField(primary_key=True)
    IdTipoMantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.PROTECT)
    IdEquipo = models.ForeignKey(Equipo, on_delete=models.PROTECT,  null=True)
    FechaIngreso = models.DateField()
    FechaSalida = models.DateField()
    DescripcionMantenimiento = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.IdTipoMantenimiento.Descripcion} - {self.IdEquipo} - {self.FechaIngreso} - {self.FechaSalida} - {self.DescripcionMantenimiento}'


