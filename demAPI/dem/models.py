from django.db import models


class Doctor(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=False)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=False)
    apellido_materno = models.CharField(max_length=45,null=True, blank=False)
    estatus = models.CharField(max_length=4,null=True, blank=True)
    sexo = models.CharField(max_length=1,null=True, blank=True)
    correo = models.EmailField(max_length=45,null=True, blank=True)
    rfc = models.CharField(max_length=45,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    url_foto = models.CharField(max_length=90,null=True, blank=True)
    cedula = models.CharField(max_length=8,null=True, blank=True)
    calle = models.CharField(max_length=90,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    estado = models.CharField(max_length=45,null=True, blank=True)
    municipio = models.CharField(max_length=45,null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        verbose_name_plural = "Doctores"


class Paciente(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=False)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=False)
    apellido_materno = models.CharField(max_length=45,null=True, blank=False)
    estatus = models.CharField(max_length=4,null=True, blank=True)
    sexo = models.CharField(max_length=1,null=True, blank=True)
    correo = models.EmailField(max_length=45,null=True, blank=True)
    rfc = models.CharField(max_length=45,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    url_foto = models.CharField(max_length=90,null=True, blank=True)
    ocupacion = models.CharField(max_length=45,null=True, blank=True)
    notas = models.CharField(max_length=200,null=True, blank=True)
    url_arch_priv = models.CharField(max_length=90,null=True, blank=True)
    antecedentes_principales = models.CharField(max_length=200,null=True, blank=True)
    tipo_sangre = models.CharField(max_length=3,null=True, blank=True)
    calle = models.CharField(max_length=90,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    estado = models.CharField(max_length=45,null=True, blank=True)
    municipio = models.CharField(max_length=45,null=True, blank=True)
    estado_nacimiento = models.CharField(max_length=45,null=True, blank=True)
    municipio_nacimiento = models.CharField(max_length=45,null=True, blank=True)
    monoclave = models.CharField(max_length=45,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes"


class Consulta(models.Model):
    fecha_consulta = models.DateField(null=True, blank=False)
    hora = models.CharField(max_length=5,null=True, blank=False)
    estatus = models.CharField(max_length=20,null=True, blank=False)
    consultorio = models.CharField(max_length=45,null=True, blank=False)
    motivo_consulta = models.CharField(max_length=200,null=True, blank=False)
    proxima_consulta = models.DateField(null=True, blank=False)
    nombre_doctor  =  models.CharField(max_length=90,null=True, blank=False)
    rfc_doctor =  models.CharField(max_length=45,null=True, blank=False)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.fecha_consulta, self.hora, self.consultorio, self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Consultas"


class Asistente(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=False)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=False)
    apellido_materno = models.CharField(max_length=45,null=True, blank=False)
    estatus = models.CharField(max_length=4,null=True, blank=True)
    sexo = models.CharField(max_length=1,null=True, blank=True)
    correo = models.EmailField(max_length=45,null=True, blank=True)
    rfc = models.CharField(max_length=45,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    url_foto = models.CharField(max_length=90,null=True, blank=True)
    permisos = models.BooleanField(default=False,null=True, blank=True)
    calle = models.CharField(max_length=90,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    estado = models.CharField(max_length=45,null=True, blank=True)
    municipio = models.CharField(max_length=45,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)

    class Meta:
        verbose_name_plural = "Asistentes"


class Acompañante(models.Model):
    nombre = models.CharField(max_length=90,null=True, blank=False)
    apellido_paterno = models.CharField(max_length=45,null=True, blank=False)
    apellido_materno = models.CharField(max_length=45,null=True, blank=False)
    sexo = models.CharField(max_length=1,null=True, blank=False)
    correo = models.EmailField(max_length=45,null=True, blank=True)
    rfc = models.CharField(max_length=45,null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    url_foto = models.CharField(max_length=90,null=True, blank=True)
    relacion = models.CharField(max_length=45,null=True, blank=True)
    calle = models.CharField(max_length=90,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.relacion, self.nombre, self.apellido_paterno)

    class Meta:
        verbose_name_plural = "Acompañantes"


class Facturacion_datos_doctor(models.Model):

    rfc = models.CharField(max_length=45,null=True, blank=False)
    razon_social = models.CharField(max_length=90,null=True, blank=False)
    regimen_fiscal = models.CharField(max_length=90,null=True, blank=False)
    tipo_comprobante = models.CharField(max_length=90,null=True, blank=False)
    Doctor = models.OneToOneField(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.rfc, self.Doctor.nombre, self.Doctor.apellido_paterno, self.Doctor.apellido_materno)

    class Meta:
        verbose_name_plural = "Doctores - Datos de facturación"


class Consultorio(models.Model):
    nombre_consultorio = models.CharField(max_length=90,null=True, blank=False)
    alias_consultorio = models.CharField(max_length=45,null=True, blank=True)
    calle = models.CharField(max_length=90,null=True, blank=True)
    num_interior = models.CharField(max_length=10,null=True, blank=True)
    num_exterior = models.CharField(max_length=10,null=True, blank=True)
    colonia = models.CharField(max_length=45,null=True, blank=True)
    cp = models.CharField(max_length=5,null=True, blank=True)
    estado = models.CharField(max_length=45,null=True, blank=True)
    municipio = models.CharField(max_length=45,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.nombre_consultorio, self.alias_consultorio)

    class Meta:
        verbose_name_plural = "Doctores - Consultorios"


class Especialidad(models.Model):
    nombre_especialidad = models.CharField(max_length=45,null=True, blank=False)
    nombre_sub_especialidad = models.CharField(max_length=45,null=True, blank=False)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.nombre_especialidad, self.Doctor.nombre, self.Doctor.apellido_paterno, self.Doctor.apellido_materno)

    class Meta:
        verbose_name_plural = "Doctores - Especialidades"


class Consulta_campos_conf(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=False)
    tipo = models.CharField(max_length=45,null=True, blank=False)
    sub_tipo = models.CharField(max_length=45,null=True, blank=False)
    tipo_campo = models.CharField(max_length=4,null=True, blank=False)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.titulo, self.Doctor.nombre, self.Doctor.apellido_paterno, self.Doctor.apellido_materno)


class Expediente_conf(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=False)
    tipo = models.CharField(max_length=45,null=True, blank=False)
    sub_tipo = models.CharField(max_length=45,null=True, blank=False)
    tipo_campo = models.CharField(max_length=4,null=True, blank=False)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.titulo, self.Doctor.nombre, self.Doctor.apellido_paterno, self.Doctor.apellido_materno)


class Cita_externa(models.Model):
    fecha_cita = models.DateField(null=True, blank=False)
    tipo = models.CharField(max_length=45,null=True, blank=False)
    hora_inicio = models.CharField(max_length=5,null=True, blank=False)
    hora_final = models.CharField(max_length=5,null=True, blank=False)
    estatus = models.CharField(max_length=10,null=True, blank=False)
    color = models.CharField(max_length=2,null=True, blank=False)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.fecha_cita, self.hora_inicio, self.hora_final, self.Doctor.nombre, self.Doctor.apellido_paterno, self.Doctor.apellido_materno)

    class Meta:
        verbose_name_plural = "Doctores - Citas Externas"


class Horario(models.Model):
    dia = models.CharField(max_length=3,null=True, blank=False)
    hora_inicio = models.CharField(max_length=5,null=True, blank=False)
    hora_final = models.CharField(max_length=5,null=True, blank=False)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.dia)

    class Meta:
        verbose_name_plural = "Doctores - Horarios"

class Telefono_doctor(models.Model):
    tipo = models.CharField(max_length=3,null=True, blank=False)
    lada = models.CharField(max_length=3,null=True, blank=False)
    telefono = models.CharField(max_length=10,null=True, blank=False)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.tipo, self.lada, self.telefono)

    class Meta:
        verbose_name_plural = "Doctores - Telefonos"

class Telefono_paciente(models.Model):
    tipo = models.CharField(max_length=3,null=True, blank=False)
    lada = models.CharField(max_length=3,null=True, blank=False)
    telefono = models.CharField(max_length=10,null=True, blank=False)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.tipo, self.lada, self.telefono)

    class Meta:
        verbose_name_plural = "Pacientes - Telefonos"


class Telefono_asistente(models.Model):
    tipo = models.CharField(max_length=3,null=True, blank=False)
    lada = models.CharField(max_length=3,null=True, blank=False)
    telefono = models.CharField(max_length=10,null=True, blank=False)
    Asistente = models.ForeignKey(Asistente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.tipo, self.lada, self.telefono)

    class Meta:
        verbose_name_plural = "Asistentes - Telefonos"


class Telefono_acompañante(models.Model):
    tipo = models.CharField(max_length=3,null=True, blank=False)
    lada = models.CharField(max_length=3,null=True, blank=False)
    telefono = models.CharField(max_length=10,null=True, blank=False)
    Acompañante = models.ForeignKey(Acompañante, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s' % (self.tipo, self.lada, self.telefono)

    class Meta:
        verbose_name_plural = "Acompañantes - Telefonos"


class Alergia(models.Model):
    alergia = models.CharField(max_length=200,null=True, blank=False)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.alergia, self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Alergias"


class Antecedentes(models.Model):
    descripcion = models.CharField(max_length=200,null=True, blank=False)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.descripcion, self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Antecedentes"


class Expediente(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=False)
    tipo = models.CharField(max_length=45,null=True, blank=False)
    sub_tipo = models.CharField(max_length=45,null=True, blank=False)
    tipo_campo = models.CharField(max_length=4,null=True, blank=False)
    nota = models.CharField(max_length=200,null=True, blank=False)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.titulo, self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)


class Facturacion_datos_paciente(models.Model):
    rfc = models.CharField(max_length=45,null=True, blank=False)
    rfc_registrado = models.CharField(max_length=45,null=True, blank=False)
    razon_social = models.CharField(max_length=90,null=True, blank=False)
    residencia_fiscal = models.CharField(max_length=200,null=True, blank=False)
    num_req_id_fiscal = models.CharField(max_length=45,null=True, blank=False)
    cfdi = models.CharField(max_length=90,null=True, blank=False)
    Paciente = models.OneToOneField(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.rfc, self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Datos de Facturación"


class Diagnostico(models.Model):
    clave = models.CharField(max_length=4,null=True, blank=True)
    nombre_diagnostico = models.CharField(max_length=200,null=True, blank=False)
    vigente = models.BooleanField(default=False,null=True, blank=False)
    Consulta = models.ForeignKey(Consulta, null=True, blank=False, on_delete=models.CASCADE)



class Estudio(models.Model):
    nombre_estudio = models.CharField(max_length=90,null=True, blank=False)
    fecha_estudio = models.DateField(null=True, blank=False)
    url_archivo = models.CharField(max_length=90,null=True, blank=False)
    Paciente = models.ForeignKey(Paciente, null=True, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s %s' % (self.nombre_estudio, self.fecha_estudio,  self.Paciente.nombre, self.Paciente.apellido_paterno, self.Paciente.apellido_materno)

    class Meta:
        verbose_name_plural = "Pacientes - Estudios"


class Receta(models.Model):
    fecha_receta = models.DateField(null=True, blank=False)
    folio_receta = models.CharField(max_length=20,null=True, blank=False)
    Consulta = models.ForeignKey(Consulta, null=True, blank=False, on_delete=models.CASCADE)


class Medicamento(models.Model):
    clave = models.CharField(max_length=30,null=True, blank=True)
    descripcion = models.CharField(max_length=200,null=True, blank=False)
    indicaciones = models.CharField(max_length=200,null=True, blank=False)
    Receta = models.ForeignKey(Receta, null=True, blank=False, on_delete=models.CASCADE)


class Pago(models.Model):
    fecha_pago = models.DateField(null=True, blank=False)
    descripcion_pago = models.CharField(max_length=200,null=True, blank=False)
    tipo_pago = models.CharField(max_length=4,null=True, blank=False)
    monto = models.IntegerField(null=True, blank=False)
    forma_pago = models.CharField(max_length=4,null=True, blank=False)
    factura_pago = models.CharField(max_length=200,null=True, blank=False)
    pago_consulta = models.BooleanField(default=False,null=True, blank=True)
    id_consulta = models.CharField(max_length=200,null=True, blank=True)
    Doctor = models.ForeignKey(Doctor, null=True, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Doctores - Pagos"


class Consulta_campos(models.Model):
    titulo = models.CharField(max_length=45,null=True, blank=False)
    tipo = models.CharField(max_length=45,null=True, blank=False)
    sub_tipo = models.CharField(max_length=45,null=True, blank=False)
    tipo_campo = models.CharField(max_length=4,null=True, blank=False)
    nota = models.CharField(max_length=200,null=True, blank=False)
    Consulta = models.ForeignKey(Consulta, null=True, blank=False, on_delete=models.CASCADE)




