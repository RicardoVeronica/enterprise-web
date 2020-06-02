from django.urls import path
from . import views as contact_views

urlpatterns = [
    path('', contact_views.contact, name='contact_url'),
]
