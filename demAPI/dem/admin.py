from django.contrib import admin
from .models import Doctor, Datos_personales ,Facturacion_datos_doctor ,Consultorio ,Especialidad ,Consulta_campos_conf ,Expediente_conf ,Cita_externa ,Horario ,Servicio_externo ,Telefono ,Contraseña ,Direccion ,Paciente ,Asistente

class DoctorAdmin(admin.ModelAdmin):
    list_display = ["cedula"]
    search_fields = ["cedula"]
    class Meta:
        model = Doctor


class Datos_personalesAdmin(admin.ModelAdmin):
    list_display = ["nombre"]
    search_fields = ["nombre"]
    class Meta:
        model = Datos_personales



admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Datos_personales, Datos_personalesAdmin)
admin.site.register(Facturacion_datos_doctor)
admin.site.register(Consultorio)
admin.site.register(Especialidad)
admin.site.register(Consulta_campos_conf)
admin.site.register(Expediente_conf)
admin.site.register(Cita_externa)
admin.site.register(Horario)
admin.site.register(Servicio_externo)
admin.site.register(Telefono)
admin.site.register(Contraseña)
admin.site.register(Direccion)
admin.site.register(Paciente)
admin.site.register(Asistente)
