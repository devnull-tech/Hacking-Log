from django.contrib import admin
from .models import Layout, Visitor

class LayoutAdmin(admin.ModelAdmin):
    list_display = ['layout_name', 'in_use']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'user', 'url', 'country', 'city', 'method']
    readonly_fields = ['user', 'ip_address', 'country', 'city', 'url', 'method', 'payload', 'timestamp']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False

admin.site.register(Layout, LayoutAdmin)
admin.site.register(Visitor, VisitorAdmin)
