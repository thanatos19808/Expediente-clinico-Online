# Generated by Django 2.1.7 on 2019-03-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0034_auto_20190322_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Cita_externa',
            field=models.ManyToManyField(blank=True, to='dem.Cita_externa'),
        ),
    ]