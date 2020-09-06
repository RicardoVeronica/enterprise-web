from django.shortcuts import render


def blog(request):
    template = 'blog/blog.html'
    return render(request, template)
