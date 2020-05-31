from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    """
    Read only filds in Admin for categories
    """
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    """
    Read only fields in admin for Posts
    """
    readonly_fields = ('created', 'updated')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
