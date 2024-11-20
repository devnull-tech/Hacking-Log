from django.contrib import admin
from .models import Layout

class LayoutAdmin(admin.ModelAdmin):
    list_display = ['layout_name', 'in_use']

admin.site.register(Layout, LayoutAdmin)