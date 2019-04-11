# Generated by Django 2.1.7 on 2019-03-27 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0050_auto_20190327_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudio',
            name='Consulta',
        ),
        migrations.AddField(
            model_name='estudio',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
    ]