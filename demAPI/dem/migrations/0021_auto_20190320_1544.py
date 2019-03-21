# Generated by Django 2.1.7 on 2019-03-20 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0020_medicamento_pago_receta'),
    ]

    operations = [
        migrations.AddField(
            model_name='consulta',
            name='Consulta_campos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consulta_campos'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Diagnostico',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Diagnostico'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Estudio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Estudio'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Pago',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Pago'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='Receta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Receta'),
        ),
        migrations.AddField(
            model_name='medicamento',
            name='Receta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Receta'),
        ),
    ]