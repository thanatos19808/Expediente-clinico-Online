from django.contrib import admin
from .models import Doctor, Paciente, Facturacion_datos_doctor ,Consultorio ,Especialidad ,Consulta_campos_conf ,Expediente_conf ,Cita_externa ,Horario ,Telefono_doctor, Telefono_paciente, Telefono_asistente, Telefono_acompañante ,Alergia ,Antecedentes ,Expediente ,Facturacion_datos_paciente ,Diagnostico ,Estudio ,Receta ,Medicamento ,Pago ,Consulta_campos ,Acompañante ,Asistente ,Consulta
#it work

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["cedula", "nombre","apellido_paterno","apellido_materno"]
    search_fields = ["cedula","nombre","apellido_paterno","apellido_materno"]
    class Meta:
        model = Doctor


class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ["nombre_especialidad", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["nombre_especialidad", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Especialidad


class Facturacion_datos_doctorAdmin(admin.ModelAdmin):
    list_display = ["rfc", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["rfc", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Facturacion_datos_doctor


class ConsultorioAdmin(admin.ModelAdmin):
    list_display = ["nombre_consultorio", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["nombre_consultorio", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Consultorio



class Cita_externaAdmin(admin.ModelAdmin):
    list_display = ["fecha_cita", "hora_inicio", "hora_final", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["fecha_cita", "hora_inicio", "hora_final", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Cita_externa


class HorarioAdmin(admin.ModelAdmin):
    list_display = ["dia", "hora_inicio", "hora_final", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["dia", "hora_inicio", "hora_final", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Horario


class PacienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido_paterno", "apellido_materno"]
    search_fields = ["nombre", "apellido_paterno", "apellido_materno"]

    class Meta:
        model = Paciente


class AlergiaAdmin(admin.ModelAdmin):
    list_display = ["alergia", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["alergia", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Alergia


class AntecedentesAdmin(admin.ModelAdmin):
    list_display = ["descripcion", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["descripcion", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Antecedentes


class Facturacion_datos_pacienteAdmin(admin.ModelAdmin):
    list_display = ["rfc", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["rfc", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Facturacion_datos_paciente


class Facturacion_datos_pacienteAdmin(admin.ModelAdmin):
    list_display = ["rfc", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["rfc", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Facturacion_datos_paciente


class ConsultaAdmin(admin.ModelAdmin):
    list_display = ["fecha_consulta", "hora", "consultorio", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["fecha_consulta", "hora", "consultorio", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Consulta


class AsistenteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido_paterno", "apellido_materno", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["nombre", "apellido_paterno", "apellido_materno", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Asistente


class AcompañanteAdmin(admin.ModelAdmin):
    list_display = ["relacion", "nombre", "apellido_paterno", "apellido_materno", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["relacion", "nombre", "apellido_paterno", "apellido_materno", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Acompañante


class Telefono_pacienteAdmin(admin.ModelAdmin):
    list_display = ["tipo", "lada", "telefono", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno"]
    search_fields = ["tipo", "lada", "telefono", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Telefono_paciente


class Telefono_doctorAdmin(admin.ModelAdmin):
    list_display = ["tipo", "lada", "telefono", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["tipo", "lada", "telefono", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Telefono_doctor


class Telefono_asistenteAdmin(admin.ModelAdmin):
    list_display = ["tipo", "lada", "telefono", "asistente__nombre", "asistente__apellido_paterno", "asistente__apellido_materno"]
    search_fields = ["tipo", "lada", "telefono", "Asistente__nombre", "Asistente__apellido_paterno", "Asistente__apellido_materno"]

    def asistente__nombre(self, instance):
        return instance.Asistente.nombre

    def asistente__apellido_paterno(self, instance):
        return instance.Asistente.apellido_paterno

    def asistente__apellido_materno(self, instance):
        return instance.Asistente.apellido_materno

    class Meta:
        model = Telefono_asistente


class Telefono_acompañanteAdmin(admin.ModelAdmin):
    list_display = ["tipo", "lada", "telefono", "acompañante__nombre", "acompañante__apellido_paterno", "acompañante__apellido_materno"]
    search_fields = ["tipo", "lada", "telefono", "Acompañante__nombre", "Acompañante__apellido_paterno", "Acompañante__apellido_materno"]

    def acompañante__nombre(self, instance):
        return instance.Acompañante.nombre

    def acompañante__apellido_paterno(self, instance):
        return instance.Acompañante.apellido_paterno

    def acompañante__apellido_materno(self, instance):
        return instance.Acompañante.apellido_materno

    class Meta:
        model = Telefono_acompañante


class EstudioAdmin(admin.ModelAdmin):
    list_display = ["nombre_estudio", "fecha_estudio", "paciente__nombre", "paciente__apellido_paterno", "paciente__apellido_materno", "url_archivo"]
    search_fields = ["nombre_estudio", "fecha_estudio", "Paciente__nombre", "Paciente__apellido_paterno", "Paciente__apellido_materno", "url_archivo"]

    def paciente__nombre(self, instance):
        return instance.Paciente.nombre

    def paciente__apellido_paterno(self, instance):
        return instance.Paciente.apellido_paterno

    def paciente__apellido_materno(self, instance):
        return instance.Paciente.apellido_materno

    class Meta:
        model = Estudio


class PagoAdmin(admin.ModelAdmin):
    list_display = ["monto","fecha_pago", "doctor__nombre", "doctor__apellido_paterno", "doctor__apellido_materno"]
    search_fields = ["monto","fecha_pago", "Doctor__nombre", "Doctor__apellido_paterno", "Doctor__apellido_materno"]

    def doctor__nombre(self, instance):
        return instance.Doctor.nombre

    def doctor__apellido_paterno(self, instance):
        return instance.Doctor.apellido_paterno

    def doctor__apellido_materno(self, instance):
        return instance.Doctor.apellido_materno

    class Meta:
        model = Telefono_doctor

admin.site.site_header = 'TOP MEDICAL'
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Facturacion_datos_doctor, Facturacion_datos_doctorAdmin)
admin.site.register(Consultorio, ConsultorioAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
#admin.site.register(Consulta_campos_conf)
#admin.site.register(Expediente_conf)
admin.site.register(Cita_externa,Cita_externaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Telefono_doctor,Telefono_doctorAdmin)
admin.site.register(Telefono_paciente, Telefono_pacienteAdmin)
admin.site.register(Telefono_asistente, Telefono_asistenteAdmin)
admin.site.register(Telefono_acompañante, Telefono_acompañanteAdmin)
admin.site.register(Alergia, AlergiaAdmin)
admin.site.register(Antecedentes,AntecedentesAdmin)
#admin.site.register(Expediente)
admin.site.register(Facturacion_datos_paciente,Facturacion_datos_pacienteAdmin)
#admin.site.register(Diagnostico)
admin.site.register(Estudio, EstudioAdmin)
#admin.site.register(Receta)
#admin.site.register(Medicamento)
admin.site.register(Pago, PagoAdmin)
#admin.site.register(Consulta_campos)
admin.site.register(Acompañante, AcompañanteAdmin)
admin.site.register(Asistente, AsistenteAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Paciente,PacienteAdmin)
