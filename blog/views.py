from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def blog(request):
    template = 'blog/blog.html'
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, template, context)


def category(request, category_pk):
    template = 'blog/category.html'
    category = get_object_or_404(Category, pk=category_pk)
    context = {
        'category': category
    }
    return render(request, template, context)
