from django.urls import path
from .views import home, about, store

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('store/', store, name='store'),
]
