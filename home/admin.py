from django.contrib import admin
from .models import Layout, Visitor

class LayoutAdmin(admin.ModelAdmin):
    list_display = ['layout_name', 'in_use']

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'url', 'timestamp']
    readonly_fields = ['ip_address', 'url', 'timestamp']
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj = ...):
        return False
    
    def has_change_permission(self, request, obj = ...):
        return False

admin.site.register(Layout, LayoutAdmin)
admin.site.register(Visitor, VisitorAdmin)