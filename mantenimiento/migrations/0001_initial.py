# Generated by Django 4.2.12 on 2024-05-14 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('IdCase', models.AutoField(primary_key=True, serialize=False)),
                ('CaseSerial', models.CharField(max_length=200)),
                ('Observacion', models.TextField()),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('IdEstado', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('IdImpresora', models.AutoField(primary_key=True, serialize=False)),
                ('ImpresoraSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('IdMonitor', models.AutoField(primary_key=True, serialize=False)),
                ('MonitorSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Resolucion', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Parlante',
            fields=[
                ('IdParlante', models.AutoField(primary_key=True, serialize=False)),
                ('ParlanteSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyector',
            fields=[
                ('IdProyector', models.AutoField(primary_key=True, serialize=False)),
                ('ProyectorSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Raton',
            fields=[
                ('IdRaton', models.AutoField(primary_key=True, serialize=False)),
                ('RatonSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('IdTeclado', models.AutoField(primary_key=True, serialize=False)),
                ('TecladoSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Distribucion', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoMantenimiento',
            fields=[
                ('IdTipoMantenimiento', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=100)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ups',
            fields=[
                ('IdUps', models.AutoField(primary_key=True, serialize=False)),
                ('UpsSerial', models.CharField(max_length=200)),
                ('Marca', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=200)),
                ('FechaIngreso', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('IdMantenimiento', models.AutoField(primary_key=True, serialize=False)),
                ('FechaIngreso', models.DateField()),
                ('FechaSalida', models.DateField()),
                ('DescripcionMantenimiento', models.CharField(max_length=500)),
                ('IdTipoMantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.tipomantenimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('IdLaboratorio', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=100)),
                ('Codigo', models.CharField(max_length=100)),
                ('Responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('IdEquipo', models.AutoField(primary_key=True, serialize=False)),
                ('SistemaOperativo', models.CharField(max_length=100)),
                ('Descripcion', models.CharField(max_length=500)),
                ('Case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.case')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.estado')),
                ('Monitor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.monitor')),
                ('Parlante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.parlante')),
                ('Raton', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.raton')),
                ('Teclado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mantenimiento.teclado')),
            ],
        ),
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('IdEncargado', models.AutoField(primary_key=True, serialize=False)),
                ('Cedula', models.CharField(max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
