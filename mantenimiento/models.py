from django.contrib.auth.models import User
from django.db import models

class Laboratorio(models.Model):
    IdLaboratorio = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=100)
    Responsable = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self. IdLaboratorio} - {self.Codigo} - {self.Nombre} - {self.Responsable.first_name} {self.Responsable.last_name}'

class Estado(models.Model):
    IdEstado = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.IdEstado} - {self.Descripcion}'

class TipoMantenimiento(models.Model):
    IdTipoMantenimiento = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.IdTipoMantenimiento} -  {self.Descripcion}'

class Case(models.Model):
    IdCase = models.AutoField(primary_key=True)
    CaseSerial = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    Observacion = models.TextField()

    def __str__(self):
        return f'{self.IdCase} - {self.CaseSerial} - {self.FechaIngreso} - {self.Observacion}'

class Monitor(models.Model):
    IdMonitor = models.AutoField(primary_key=True)
    MonitorSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Resolucion = models.CharField(max_length=50)
    FechaIngreso = models.DateField()
    Observacion = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.IdMonitor} - {self.MarcaModelo} - {self.MonitorSerial} - {self.Resolucion}'

class Teclado(models.Model):
    IdTeclado = models.AutoField(primary_key=True)
    TecladoSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Distribucion = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()

    def __str__(self):
        return f'{self.IdTeclado} -  {self.MarcaModelo} - {self.TecladoSerial}'

class Raton(models.Model):
    IdRaton = models.AutoField(primary_key=True)
    RatonSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return f'{self.IdRaton} -  {self.MarcaModelo} - {self.RatonSerial}'

class Parlante(models.Model):
    IdParlante = models.AutoField(primary_key=True)
    ParlanteSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return f'{self.IdParlante} - {self.MarcaModelo} - {self.ParlanteSerial}'

class Impresora(models.Model):
    IdImpresora = models.AutoField(primary_key=True)
    ImpresoraSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return f'{self.IdImpresora} -  {self.MarcaModelo} - {self.ImpresoraSerial}'

class Proyector(models.Model):
    IdProyector = models.AutoField(primary_key=True)
    ProyectorSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return f'{self.IdProyector} -  {self.MarcaModelo} - {self.ProyectorSerial}'

class Ups(models.Model):
    IdUps = models.AutoField(primary_key=True)
    UpsSerial = models.CharField(max_length=200)
    MarcaModelo = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=200)
    FechaIngreso = models.DateField()
    def __str__(self):
        return str(self.IdUps)

class Equipo(models.Model):
    IdEquipo = models.AutoField(primary_key=True)
    SistemaOperativo = models.CharField(max_length=100, blank=True)
    IP = models.CharField(max_length=16, null=True, blank=True)
    Descripcion = models.CharField(max_length=500, null=False, blank=True)
    Estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    Case = models.ForeignKey(Case, on_delete=models.PROTECT, null=True, blank=True)
    Monitor = models.ForeignKey(Monitor, on_delete=models.PROTECT, null=True, blank=True)
    Teclado = models.ForeignKey(Teclado, on_delete=models.PROTECT, null=True, blank=True)
    Raton = models.ForeignKey(Raton, on_delete=models.PROTECT, null=True, blank=True)
    Parlante = models.ForeignKey(Parlante, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return f'{self.IdEquipo} - {self.SistemaOperativo} - {self.Estado}'

class Mantenimiento(models.Model):
    IdMantenimiento = models.AutoField(primary_key=True)
    IdTipoMantenimiento = models.ForeignKey(TipoMantenimiento, on_delete=models.PROTECT)
    IdEquipo = models.ForeignKey(Equipo, on_delete=models.PROTECT,  null=True)
    FechaIngreso = models.DateField()
    FechaSalida = models.DateField()
    DescripcionMantenimiento = models.CharField(max_length=500)

    def __str__(self): 
        return f'{self.IdMantenimiento} - {self.IdTipoMantenimiento.Descripcion} - {self.FechaIngreso} - {self.FechaSalida} - {self.DescripcionMantenimiento}'


