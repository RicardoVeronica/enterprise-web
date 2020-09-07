from django.urls import path
from .views import blog, category

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/category/<int:category_pk>/', category, name='category')
]
