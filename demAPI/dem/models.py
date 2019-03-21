from django.db import models


class Direccion(models.Model):
    calle = models.CharField(max_length=90)
    num_interior = models.CharField(max_length=10)
    num_exterior = models.CharField(max_length=10)
    colonia = models.CharField(max_length=45)
    cp = models.CharField(max_length=5)


class Facturacion_datos_doctor(models.Model):
    rfc = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=90)
    regimen_fiscal = models.CharField(max_length=90)
    tipo_comprobante = models.CharField(max_length=90)


class Consultorio(models.Model):
    nombre_consultorio = models.CharField(max_length=90)
    alias_consultorio = models.CharField(max_length=45)
    Direccion = models.OneToOneField(Direccion, null=True, blank=True, on_delete=models.CASCADE)


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=45)


class Consulta_campos_conf(models.Model):
    titulo = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    sub_tipo = models.CharField(max_length=45)
    tipo_campo = models.CharField(max_length=4)


class Expediente_conf(models.Model):
    titulo = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    sub_tipo = models.CharField(max_length=45)
    tipo_campo = models.CharField(max_length=4)


class Cita_externa(models.Model):
    fecha_cita = models.DateField()
    tipo = models.CharField(max_length=45)
    hora_inicio = models.CharField(max_length=5)
    hora_final = models.CharField(max_length=5)
    estatus = models.CharField(max_length=10)
    color = models.CharField(max_length=2)


class Horario(models.Model):
    dia = models.CharField(max_length=3)
    hora_inicio = models.CharField(max_length=5)
    hora_final = models.CharField(max_length=5)


class Servicio_externo(models.Model):
    descripcion_servicio = models.CharField(max_length=200)


class Telefono(models.Model):
    tipo = models.CharField(max_length=3)
    lada = models.CharField(max_length=3)
    telefono = models.CharField(max_length=10)


class Contraseña(models.Model):
    Contraseña = models.CharField(max_length=45)


class Datos_personales(models.Model):
    nombre = models.CharField(max_length=90)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1)
    correo = models.CharField(max_length=45)
    rfc = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField()
    url_foto = models.CharField(max_length=90)


class Alergia(models.Model):
    alergia = models.CharField(max_length=200)


class Antecedentes(models.Model):
    descripcion = models.CharField(max_length=200)


class Expediente(models.Model):
    titulo = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    sub_tipo = models.CharField(max_length=45)
    tipo_campo = models.CharField(max_length=4)
    nota = models.CharField(max_length=200)


class Facturacion_datos_paciente(models.Model):
    rfc = models.CharField(max_length=45)
    rfc_registrado = models.CharField(max_length=45)
    razon_social = models.CharField(max_length=90)
    residencia_fiscal = models.CharField(max_length=200)
    num_req_id_fiscal = models.CharField(max_length=45)
    cfdi = models.CharField(max_length=90)


class Diagnostico(models.Model):
    clave = models.CharField(max_length=4)
    nombre_diagnostico = models.CharField(max_length=200)
    vigente = models.BooleanField(default=False)


class Estudio(models.Model):
    nombre_carpeta = models.CharField(max_length=90)
    fecha_estudios = models.DateField()
    url_archivo = models.CharField(max_length=90)


class Receta(models.Model):
    fecha_receta = models.DateField()
    folio_receta = models.CharField(max_length=20)


class Medicamento(models.Model):
    clave = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    indicaciones = models.CharField(max_length=200)
    Receta = models.ForeignKey(Receta, null=True, blank=True, on_delete=models.CASCADE)


class Pago(models.Model):
    fecha_pago = models.DateField()
    descripcion_pago = models.CharField(max_length=200)
    monto = models.IntegerField()
    forma_pago = models.CharField(max_length=4)
    factura_pago = models.CharField(max_length=200)


class Consulta_campos(models.Model):
    titulo = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    sub_tipo = models.CharField(max_length=45)
    tipo_campo = models.CharField(max_length=4)
    nota = models.CharField(max_length=200)


class Acompañante(models.Model):
    relacion = models.CharField(max_length=45)
    Datos_personales = models.OneToOneField(Datos_personales, null=True, blank=True, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    Telefono = models.ForeignKey(Telefono, null=True, blank=True, on_delete=models.CASCADE)


class Asistente(models.Model):
    permisos = models.BooleanField(default=False)
    Datos_personales = models.OneToOneField(Datos_personales, null=True, blank=True, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    Telefono = models.ForeignKey(Telefono, null=True, blank=True, on_delete=models.CASCADE)
    Contraseña = models.ForeignKey(Contraseña, null=True, blank=True, on_delete=models.CASCADE)


class Consulta(models.Model):
    fecha_consulta = models.DateField()
    hora = models.CharField(max_length=5)
    estatus = models.CharField(max_length=20)
    consultorio = models.CharField(max_length=45)
    motivo_consulta = models.CharField(max_length=200)
    proxima_consulta = models.DateField()
    Receta = models.ForeignKey(Receta, null=True, blank=True, on_delete=models.CASCADE)
    Pago = models.ForeignKey(Pago, null=True, blank=True, on_delete=models.CASCADE)
    Consulta_campos = models.ForeignKey(Consulta_campos, null=True, blank=True, on_delete=models.CASCADE)
    Estudio = models.ForeignKey(Estudio, null=True, blank=True, on_delete=models.CASCADE)
    Diagnostico = models.ForeignKey(Diagnostico, null=True, blank=True, on_delete=models.CASCADE)


class Paciente(models.Model):
    ocupacion = models.CharField(max_length=45)
    notas = models.CharField(max_length=200)
    url_arch_priv = models.CharField(max_length=90)
    antecedentes_principales = models.CharField(max_length=200)
    tipo_sangre = models.CharField(max_length=3)
    Facturacion_datos_paciente = models.OneToOneField(Facturacion_datos_paciente, null=True, blank=True, on_delete=models.CASCADE)
    Expediente = models.OneToOneField(Expediente, null=True, blank=True, on_delete=models.CASCADE)
    Antecedentes = models.ForeignKey(Antecedentes, null=True, blank=True, on_delete=models.CASCADE)
    Alergia = models.ForeignKey(Alergia, null=True, blank=True, on_delete=models.CASCADE)
    Telefono = models.ForeignKey(Telefono, null=True, blank=True, on_delete=models.CASCADE)
    Direccion = models.ForeignKey(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    Datos_personales = models.OneToOneField(Datos_personales, null=True, blank=True, on_delete=models.CASCADE)
    Acompañante = models.ForeignKey(Acompañante, null=True, blank=True, on_delete=models.CASCADE)
    Consulta = models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)

class Doctor(models.Model):
    cedula = models.CharField(max_length=8)
    dgp = models.CharField(max_length=90)
    Facturacion_datos_doctor = models.OneToOneField(Facturacion_datos_doctor, null=True, blank=True, on_delete=models.CASCADE)
    Consultorio = models.ForeignKey(Consultorio, null=True, blank=True, on_delete=models.CASCADE)
    Especialidad = models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)
    Consulta_campos_conf = models.ForeignKey(Consulta_campos_conf, null=True, blank=True, on_delete=models.CASCADE)
    Expediente_conf = models.ForeignKey(Expediente_conf, null=True, blank=True, on_delete=models.CASCADE)
    Cita_externa = models.ForeignKey(Cita_externa, null=True, blank=True, on_delete=models.CASCADE)
    Horario = models.ForeignKey(Horario, null=True, blank=True, on_delete=models.CASCADE)
    Servicio_externo = models.ForeignKey(Servicio_externo, null=True, blank=True, on_delete=models.CASCADE)
    Telefono = models.ForeignKey(Telefono, null=True, blank=True, on_delete=models.CASCADE)
    Contraseña = models.ForeignKey(Contraseña, null=True, blank=True, on_delete=models.CASCADE)
    Direccion = models.OneToOneField(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    Datos_personales = models.OneToOneField(Datos_personales, null=True, blank=True, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
    Asistente = models.ForeignKey(Asistente, null=True, blank=True, on_delete=models.CASCADE)


