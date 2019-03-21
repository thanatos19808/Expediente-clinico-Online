# Generated by Django 2.1.7 on 2019-03-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dem', '0002_doctor_facturacion_datos_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alergia', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Antecedentes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cita_externa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('tipo', models.CharField(max_length=45)),
                ('hora_inicio', models.CharField(max_length=5)),
                ('hora_final', models.CharField(max_length=5)),
                ('estatus', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta_conf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('tipo', models.CharField(max_length=45)),
                ('sub_tipo', models.CharField(max_length=45)),
                ('tipo_campo', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Consultorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_consultorio', models.CharField(max_length=90)),
                ('alias_consultorio', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Datos_personales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('apellido_paterno', models.CharField(max_length=45)),
                ('apellido_materno', models.CharField(max_length=45)),
                ('sexo', models.CharField(max_length=1)),
                ('correo', models.CharField(max_length=45)),
                ('rfc', models.CharField(max_length=45)),
                ('fecha_nacimiento', models.DateField()),
                ('url_foto', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=90)),
                ('num_interior', models.CharField(max_length=10)),
                ('num_exterior', models.CharField(max_length=10)),
                ('colonia', models.CharField(max_length=45)),
                ('cp', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_especialidad', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('tipo', models.CharField(max_length=45)),
                ('sub_tipo', models.CharField(max_length=45)),
                ('tipo_campo', models.CharField(max_length=4)),
                ('nota', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente_conf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=45)),
                ('tipo', models.CharField(max_length=45)),
                ('sub_tipo', models.CharField(max_length=45)),
                ('tipo_campo', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Facturacion_datos_paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=45)),
                ('rfc_registrado', models.CharField(max_length=45)),
                ('razon_social', models.CharField(max_length=90)),
                ('residencia_fiscal', models.CharField(max_length=200)),
                ('num_req_id_fiscal', models.CharField(max_length=45)),
                ('cfdi', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=3)),
                ('hora_inicio', models.CharField(max_length=5)),
                ('hora_final', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocupacion', models.CharField(max_length=45)),
                ('notas', models.CharField(max_length=200)),
                ('url_arch_priv', models.CharField(max_length=90)),
                ('antecedentes_principales', models.CharField(max_length=200)),
                ('tipo_sangre', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Pasword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio_externo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_servicio', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=3)),
                ('lada', models.CharField(max_length=3)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='Facturacion_datos_doctor',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]
