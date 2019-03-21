# Generated by Django 2.1.7 on 2019-03-19 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0003_auto_20190319_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=8)),
                ('dgp', models.CharField(max_length=90)),
                ('Cita_externa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Cita_externa')),
                ('Consulta_conf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consulta_conf')),
                ('Consultorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consultorio')),
                ('Datos_personales', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Datos_personales')),
                ('Direccion', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Direccion')),
                ('Especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Especialidad')),
                ('Expediente_conf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Expediente_conf')),
                ('Facturacion_datos_doctor', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Facturacion_datos_doctor')),
                ('Horario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Horario')),
            ],
        ),
        migrations.RenameModel(
            old_name='Pasword',
            new_name='Password',
        ),
        migrations.AddField(
            model_name='doctor',
            name='Password',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Password'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Servicio_externo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Servicio_externo'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='Telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Telefono'),
        ),
    ]