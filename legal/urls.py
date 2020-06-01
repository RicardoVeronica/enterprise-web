from django.urls import path
from . import views as legal_views

urlpatterns = [
    path('legal/<int:legal_id>/<slug:legal_slug>', legal_views.legal,
         name='legal_url'),
]
