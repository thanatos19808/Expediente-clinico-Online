# Generated by Django 2.1.7 on 2019-03-19 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=8)),
                ('dgp', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion_datos_doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=45)),
                ('razon_social', models.CharField(max_length=90)),
                ('regimen_fiscal', models.CharField(max_length=90)),
                ('tipo_comprobante', models.CharField(max_length=90)),
            ],
        ),
    ]
