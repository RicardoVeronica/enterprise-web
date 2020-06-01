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
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published',)
    search_fields = ('title', 'content', 'author__username',
                     'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        """
        Show categories in list_display
        """
        return ", ".join(c.name for c in obj.categories.all().order_by('name'))
    post_categories.short_description = 'categories'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
