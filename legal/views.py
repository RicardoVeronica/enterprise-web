from django.shortcuts import render, get_object_or_404
from .models import Legal


def legal(request, legal_id):
    """
    Views for legal files
    """
    template = 'legal/legal.html'
    legal = get_object_or_404(Legal, id=legal_id)
    context = {'legal': legal}

    return render(request, template, context)
