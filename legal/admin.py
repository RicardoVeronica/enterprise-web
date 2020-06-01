from django.contrib import admin
from .models import Legal


class LegalAdmin(admin.ModelAdmin):
    """
    Show read only file in admin for legal files
    """
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'order')


admin.site.register(Legal, LegalAdmin)
