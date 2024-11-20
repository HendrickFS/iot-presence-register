from django.contrib import admin
from .models import employee, rfidLog

class employeeAdmin(admin.ModelAdmin):
    list_display = ('rfid', 'name', 'email')
    search_fields = ('rfid', 'name', 'email')
    ordering = ('rfid',)

class rfidLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'timestamp', 'type')
    search_fields = ('employee', 'timestamp', 'type')
    ordering = ('employee', 'timestamp')

admin.site.register(rfidLog, rfidLogAdmin)
admin.site.register(employee, employeeAdmin)