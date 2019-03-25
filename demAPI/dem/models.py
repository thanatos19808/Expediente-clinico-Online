from django.db import models


class Doctor(models.Model):
    cedula = models.CharField(max_length=8,null=True, blank=True)
    dgp = models.CharField(max_length=90,null=True, blank=True)


class Paciente(models.Model):
    ocupacion = models.CharField(max_length=45,null=True, blank=True)
    notas = models.CharField(max_length=200,null=True, blank=True)
    url_arch_priv = models.CharField(max_length=90,null=True, blank=True)
    antecedentes_principales = models.CharField(max_length=200,null=True, blank=True)
    tipo_sangre = models.CharField(max_length=3,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Consulta(models.Model):
    fecha_consulta = models.DateField(null=True, blank=True)
    hora = models.CharField(max_length=5,null=True, blank=True)
    estatus = models.CharField(max_length=20,null=True, blank=True)
    consultorio = models.CharField(max_length=45,null=True, blank=True)
    motivo_consulta = models.CharField(max_length=200,null=True, blank=True)
    proxima_consulta = models.DateField(null=True, blank=True)
    Paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Asistente(models.Model):
    permisos = models.BooleanField(default=False,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Acompañante(models.Model):
    relacion = models.CharField(max_length=45,null=True, blank=True)
    Paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Direccion(models.Model):
    calle = models.CharField(max_length=90,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    Doctor = models.OneToOneField(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    Asistente = models.OneToOneField(Asistente, null=True, blank=True, on_delete=models.CASCADE)
    Acompañante = models.OneToOneField(Acompañante, null=True, blank=True, on_delete=models.CASCADE)
    Paciente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Facturacion_datos_doctor(models.Model):
    rfc = models.CharField(max_length=45,null=True, blank=True)
    razon_social = models.CharField(max_length=90,null=True, blank=True)
    regimen_fiscal = models.CharField(max_length=90,null=True, blank=True)
    tipo_comprobante = models.CharField(max_length=90,null=True, blank=True)
    Doctor = models.OneToOneField(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Consultorio(models.Model):
    nombre_consultorio = models.CharField(max_length=90,null=True, blank=True)
    alias_consultorio = models.CharField(max_length=45,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=45,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Consulta_campos_conf(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=True)
    tipo = models.CharField(max_length=45,null=True, blank=True)
    sub_tipo = models.CharField(max_length=45,null=True, blank=True)
    tipo_campo = models.CharField(max_length=4,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Expediente_conf(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=True)
    tipo = models.CharField(max_length=45,null=True, blank=True)
    sub_tipo = models.CharField(max_length=45,null=True, blank=True)
    tipo_campo = models.CharField(max_length=4,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Cita_externa(models.Model):
    fecha_cita = models.DateField(null=True, blank=True)
    tipo = models.CharField(max_length=45,null=True, blank=True)
    hora_inicio = models.CharField(max_length=5,null=True, blank=True)
    hora_final = models.CharField(max_length=5,null=True, blank=True)
    estatus = models.CharField(max_length=10,null=True, blank=True)
    color = models.CharField(max_length=2,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Horario(models.Model):
    dia = models.CharField(max_length=3,null=True, blank=True)
    hora_inicio = models.CharField(max_length=5,null=True, blank=True)
    hora_final = models.CharField(max_length=5,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Servicio_externo(models.Model):
    descripcion_servicio = models.CharField(max_length=200,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)


class Telefono(models.Model):
    tipo = models.CharField(max_length=3,null=True, blank=True)
    lada = models.CharField(max_length=3,null=True, blank=True)
    telefono = models.CharField(max_length=10,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    Asistente = models.ForeignKey(Asistente, null=True, blank=True, on_delete=models.CASCADE)
    Acompañante = models.ForeignKey(Acompañante, null=True, blank=True, on_delete=models.CASCADE)
    Paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Contraseña(models.Model):
    Contraseña = models.CharField(max_length=45,null=True, blank=True)
    Doctor = models.OneToOneField(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    Asistente = models.ForeignKey(Asistente, null=True, blank=True, on_delete=models.CASCADE)

class Datos_personales(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=True)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=True)
    apellido_materno = models.CharField(max_length=45,null=True, blank=True)
    sexo = models.CharField(max_length=1,null=True, blank=True)
    correo = models.CharField(max_length=45,null=True, blank=True)
    rfc = models.CharField(max_length=45,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    url_foto = models.CharField(max_length=90,null=True, blank=True)
    Doctor = models.OneToOneField(Doctor, null=True, blank=True, on_delete=models.CASCADE)
    Asistente = models.OneToOneField(Asistente, null=True, blank=True, on_delete=models.CASCADE)
    Acompañante = models.OneToOneField(Acompañante, null=True, blank=True, on_delete=models.CASCADE)
    Paciente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Alergia(models.Model):
    alergia = models.CharField(max_length=200,null=True, blank=True)
    Paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Antecedentes(models.Model):
    descripcion = models.CharField(max_length=200,null=True, blank=True)
    Paciente = models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Expediente(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=True)
    tipo = models.CharField(max_length=45,null=True, blank=True)
    sub_tipo = models.CharField(max_length=45,null=True, blank=True)
    tipo_campo = models.CharField(max_length=4,null=True, blank=True)
    nota = models.CharField(max_length=200,null=True, blank=True)
    Paciente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Facturacion_datos_paciente(models.Model):
    rfc = models.CharField(max_length=45,null=True, blank=True)
    rfc_registrado = models.CharField(max_length=45,null=True, blank=True)
    razon_social = models.CharField(max_length=90,null=True, blank=True)
    residencia_fiscal = models.CharField(max_length=200,null=True, blank=True)
    num_req_id_fiscal = models.CharField(max_length=45,null=True, blank=True)
    cfdi = models.CharField(max_length=90,null=True, blank=True)
    Paciente = models.OneToOneField(Paciente, null=True, blank=True, on_delete=models.CASCADE)


class Diagnostico(models.Model):
    clave = models.CharField(max_length=4,null=True, blank=True)
    nombre_diagnostico = models.CharField(max_length=200,null=True, blank=True)
    vigente = models.BooleanField(default=False,null=True, blank=True)
    Consulta = models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)


class Estudio(models.Model):
    nombre_carpeta = models.CharField(max_length=90,null=True, blank=True)
    fecha_estudios = models.DateField(null=True, blank=True)
    url_archivo = models.CharField(max_length=90,null=True, blank=True)
    Consulta = models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)


class Receta(models.Model):
    fecha_receta = models.DateField(null=True, blank=True)
    folio_receta = models.CharField(max_length=20,null=True, blank=True)
    Consulta = models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)


class Medicamento(models.Model):
    clave = models.CharField(max_length=30,null=True, blank=True)
    descripcion = models.CharField(max_length=200,null=True, blank=True)
    indicaciones = models.CharField(max_length=200,null=True, blank=True)
    Receta = models.ForeignKey(Receta, null=True, blank=True, on_delete=models.CASCADE)


class Pago(models.Model):
    fecha_pago = models.DateField(null=True, blank=True)
    descripcion_pago = models.CharField(max_length=200,null=True, blank=True)
    monto = models.IntegerField(null=True, blank=True)
    forma_pago = models.CharField(max_length=4,null=True, blank=True)
    factura_pago = models.CharField(max_length=200,null=True, blank=True)
    Consulta = models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)
    Servicio_externo = models.ForeignKey(Servicio_externo, null=True, blank=True, on_delete=models.CASCADE)


class Consulta_campos(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=True)
    tipo = models.CharField(max_length=45,null=True, blank=True)
    sub_tipo = models.CharField(max_length=45,null=True, blank=True)
    tipo_campo = models.CharField(max_length=4,null=True, blank=True)
    nota = models.CharField(max_length=200,null=True, blank=True)
    Consulta = models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)




