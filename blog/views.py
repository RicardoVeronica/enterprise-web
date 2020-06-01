from django.shortcuts import render
from .models import Post


def blog(request):
    """
    Blog view
    """
    template = 'blog/blog.html'
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, template, context)
