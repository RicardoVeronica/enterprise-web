from django.db import models


class Service(models.Model):
    """
    Service model
    """
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Give a name for service in admin
        """
        return self.title

    class Meta:
        """
        Meta data for Service model
        """
        ordering = ['-created']
