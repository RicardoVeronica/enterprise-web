from django.shortcuts import render, get_object_or_404
# get_object_or_404: instead of showing debug error, show 404 error not found
from .models import Post, Category


def blog(request):
    """
    Blog view
    """
    template = 'blog/blog.html'
    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, template, context)


def category(request, category_id):
    """
    Shows category views
    """
    template = 'blog/category.html'
    category = get_object_or_404(Category, id=category_id)
    context = {'category': category}

    return render(request, template, context)
