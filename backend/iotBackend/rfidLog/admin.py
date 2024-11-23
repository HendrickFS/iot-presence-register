from django.contrib import admin
from .models import employee, rfidLog, sensor

class employeeAdmin(admin.ModelAdmin):
    list_display = ('rfid', 'name', 'email')
    search_fields = ('rfid', 'name', 'email')
    ordering = ('rfid',)

class rfidLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'timestamp', 'type')
    search_fields = ('employee', 'timestamp', 'type')
    ordering = ('employee', 'timestamp')

class sensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'location')
    search_fields = ('id', 'location')
    ordering = ('id',)



admin.site.register(rfidLog, rfidLogAdmin)
admin.site.register(employee, employeeAdmin)
admin.site.register(sensor, sensorAdmin)