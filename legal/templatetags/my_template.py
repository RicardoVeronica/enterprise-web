from django import template
from legal.models import Legal

register = template.Library()


@register.simple_tag
def get_legal_list():
    legals = Legal.objects.all()

    return legals
