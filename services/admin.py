from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    """
    Show read only fields in admin for services
    """
    readonly_fields = ('created', 'updated')


admin.site.register(Service, ServiceAdmin)
