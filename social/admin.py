from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    """
    Show read only fields in admin
    """
    readonly_fields = ('created', 'updated')

    # TODO: Does not work
    def get_readonly_fileds(self, request, obj=None):
        """
        Check if an user is Employee group
        """
        if request.user.groups.filter(name="Employee").exist():
            return ('key', 'name')
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)
