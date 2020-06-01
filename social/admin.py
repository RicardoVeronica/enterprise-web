from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    """
    Show read only fields in admin
    """
    readonly_fields = ('created', 'updated')


admin.site.register(Link, LinkAdmin)
