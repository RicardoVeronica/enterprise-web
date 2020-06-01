from django.db import models


class Legal(models.Model):
    """
    Model for app Legal
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta data for Legal model
        """
        ordering = ['-title']

    def __str__(self):
        """
        Show title in admin
        """
        return self.title
