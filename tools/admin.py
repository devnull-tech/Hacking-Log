from django.contrib import admin
from .models import Tool

class ToolAdmin(admin.ModelAdmin):
    list_display = ['tool_name', 'releases_url', 'updated_at']

admin.site.register(Tool, ToolAdmin)
