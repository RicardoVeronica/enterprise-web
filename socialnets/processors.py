from .models import Link


def context_processor(request):
    links = Link.objects.all()
    context = {}

    for link in links:
        context[link.key] = link.url

    return context
