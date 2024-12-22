from django.contrib import admin
from .models import Log, Term, Bot

class BotAdmin(admin.ModelAdmin):
    list_display = ['provider', 'model', 'in_use']

class TermAdmin(admin.ModelAdmin):
    list_display = ['term']

class LogAdmin(admin.ModelAdmin):
    def enable_or_disable_selected_logs(self, request, queryset):
        for log in queryset:
            log.is_public = not log.is_public
            log.save()

    actions = [enable_or_disable_selected_logs]
    list_display = ['vm_name', 'platform', 'operating_system', 'is_public', 'created_at']

admin.site.register(Log, LogAdmin)
admin.site.register(Term, TermAdmin)
admin.site.register(Bot, BotAdmin)
