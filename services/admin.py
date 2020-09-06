from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_field = ('updated', 'created',)


admin.site.register(Service, ServiceAdmin)
