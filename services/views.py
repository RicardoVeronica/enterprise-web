from django.shortcuts import render


def services(request):
    template = 'services/services.html'
    return render(request, template)
