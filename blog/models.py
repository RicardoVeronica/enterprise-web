from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category model for blog
    """
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta data in category model
        """
        ordering = ['-created']
        verbose_name_plural = 'categories'

    def __str__(self):
        """
        Show category name in admin
        """
        return self.name


class Post(models.Model):
    """
    Post for blog
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.DateTimeField(default=now)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta data in post model
        """
        ordering = ['-created']

    def __str__(self):
        """
        Show post title in admin
        """
        return self.title
