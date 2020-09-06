from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(default='../static/img/default.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
