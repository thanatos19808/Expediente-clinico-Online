# Generated by Django 2.1.7 on 2019-03-27 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0048_telefono_acompañante_telefono_asistente_telefono_doctor_telefono_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefono',
            name='Acompañante',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='Asistente',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='Doctor',
        ),
        migrations.RemoveField(
            model_name='telefono',
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='Telefono',
        ),
    ]
