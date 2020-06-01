from django.urls import path
from . import views as blog_views

urlpatterns = [
    path('', blog_views.blog, name='blog_url'),
    path('category/<int:category_id>/', blog_views.category,
         name='category_url'),
]
