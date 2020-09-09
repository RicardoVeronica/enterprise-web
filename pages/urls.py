from django.urls import path
from .views import page

urlpatterns = [
    path('page/<int:page_id>/', page, name='page')
]
