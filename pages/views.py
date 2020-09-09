from django.shortcuts import render, get_object_or_404
from .models import Page


def page(request, page_id):
    template = 'pages/page.html'
    page = get_object_or_404(Page, id=page_id)
    context = {
        'page': page
    }
    return render(request, template, context)
