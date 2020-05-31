from django.shortcuts import render
from .models import Service


def services(request):
    """
    Services app view
    """
    services = Service.objects.all()
    context = {
        'services': services
    }
    template = 'services/services.html'
    return render(request, template, context)
