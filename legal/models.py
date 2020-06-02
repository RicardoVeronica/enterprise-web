from django.db import models
from ckeditor.fields import RichTextField


class Legal(models.Model):
    """
    Model for app Legal
    """
    title = models.CharField(max_length=100)
    content = RichTextField()
    order = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta data for Legal model
        """
        ordering = ['order', 'title']

    def __str__(self):
        """
        Show title in admin
        """
        return self.title
