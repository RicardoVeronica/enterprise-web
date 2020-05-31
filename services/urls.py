from django.urls import path
from . import views as services_views

urlpatterns = [
    path('services/', services_views.services, name='services_url'),
]
