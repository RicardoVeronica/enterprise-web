from django.shortcuts import render


def blog(request):
    """
    Blog view
    """
    template = 'blog/blog.html'
    return render(request, template)
