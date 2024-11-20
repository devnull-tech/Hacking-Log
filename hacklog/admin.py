from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ['vm_name', 'platform', 'operating_system', 'created_at']

admin.site.register(Log, LogAdmin)