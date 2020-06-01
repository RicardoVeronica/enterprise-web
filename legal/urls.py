from django.urls import path
from . import views as legal_views

urlpatterns = [
    path('legal/<int:legal_id>/', legal_views.legal, name='legal_url'),
]
