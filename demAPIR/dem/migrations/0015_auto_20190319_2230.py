# Generated by Django 2.1.7 on 2019-03-19 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0014_auto_20190319_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='acompañante',
            name='Datos_personales',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Datos_personales'),
        ),
        migrations.AddField(
            model_name='acompañante',
            name='Direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Direccion'),
        ),
        migrations.AddField(
            model_name='acompañante',
            name='Telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Telefono'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Datos_personales',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Datos_personales'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='Datos_personales',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Datos_personales'),
        ),
    ]