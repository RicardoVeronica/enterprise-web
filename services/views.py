from django.shortcuts import render
from .models import Service


def services(request):
    template = 'services/services.html'
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, template, context)
