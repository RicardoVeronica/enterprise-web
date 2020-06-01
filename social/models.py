from django.db import models


class Link(models.Model):
    """
    Model for social app
    """
    key = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta data for social model
        """
        ordering = ['-name']

    def __str__(self):
        """
        Shows social name in the admin
        """
        return self.name
