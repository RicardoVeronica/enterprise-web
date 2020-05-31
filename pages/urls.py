from django.urls import path
from . import views as pages_views

urlpatterns = [
    path('', pages_views.home, name='home_url'),
    path('about/', pages_views.about, name='about_url'),
    path('timetable/', pages_views.timetable, name='timetable_url'),
]
