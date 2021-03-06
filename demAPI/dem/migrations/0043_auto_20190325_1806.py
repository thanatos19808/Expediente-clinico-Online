# Generated by Django 2.1.7 on 2019-03-25 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0042_auto_20190325_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acompañante',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
        migrations.AlterField(
            model_name='acompañante',
            name='apellido_materno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='acompañante',
            name='apellido_paterno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='acompañante',
            name='nombre',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='acompañante',
            name='sexo',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='alergia',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
        migrations.AlterField(
            model_name='alergia',
            name='alergia',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
        migrations.AlterField(
            model_name='antecedentes',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='Contraseña',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='apellido_materno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='apellido_paterno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='nombre',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='permisos',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='asistente',
            name='sexo',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='color',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='estatus',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='fecha_cita',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='hora_final',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='hora_inicio',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cita_externa',
            name='tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='Paciente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='consultorio',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='estatus',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='fecha_consulta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='hora',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='motivo_consulta',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='proxima_consulta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos',
            name='Consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consulta'),
        ),
        migrations.AlterField(
            model_name='consulta_campos',
            name='nota',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos',
            name='sub_tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos',
            name='tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos',
            name='tipo_campo',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos',
            name='titulo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos_conf',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='consulta_campos_conf',
            name='sub_tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos_conf',
            name='tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos_conf',
            name='tipo_campo',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='consulta_campos_conf',
            name='titulo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='consultorio',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='consultorio',
            name='nombre_consultorio',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='Consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consulta'),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='nombre_diagnostico',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='vigente',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Contraseña',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='apellido_materno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='apellido_paterno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='cedula',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='sexo',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='nombre_especialidad',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='Consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consulta'),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='fecha_estudios',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='nombre_carpeta',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='estudio',
            name='url_archivo',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='Paciente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='nota',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='sub_tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='tipo_campo',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='expediente',
            name='titulo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='expediente_conf',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='expediente_conf',
            name='sub_tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='expediente_conf',
            name='tipo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='expediente_conf',
            name='tipo_campo',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='expediente_conf',
            name='titulo',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_doctor',
            name='Doctor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_doctor',
            name='razon_social',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_doctor',
            name='regimen_fiscal',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_doctor',
            name='rfc',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_doctor',
            name='tipo_comprobante',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='Paciente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Paciente'),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='cfdi',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='num_req_id_fiscal',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='razon_social',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='residencia_fiscal',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='rfc',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='facturacion_datos_paciente',
            name='rfc_registrado',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='Doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Doctor'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='dia',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_final',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_inicio',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='Receta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Receta'),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='descripcion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='indicaciones',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_materno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='apellido_paterno',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tipo_sangre',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='descripcion_pago',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='factura_pago',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='fecha_pago',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='forma_pago',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='monto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pago',
            name='tipo_pago',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='Consulta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dem.Consulta'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='fecha_receta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='folio_receta',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='lada',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='telefono',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='tipo',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
