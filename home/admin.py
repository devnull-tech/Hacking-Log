from django.contrib import admin
from .models import Layout, Visitor

class LayoutAdmin(admin.ModelAdmin):
    list_display = ['layout_name', 'in_use']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'url', 'timestamp']
    readonly_fields = ['ip_address', 'url', 'timestamp']

admin.site.register(Layout, LayoutAdmin)
admin.site.register(Visitor, VisitorAdmin)