# -*- coding: utf-8 -*-
from django.urls import path, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


urlpatterns = [
    path('', include('core.urls')),
    path('', include('services.urls')),
    path('', include('blog.urls')),
    path('', include('pages.urls')),
    path('', include('form.urls')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
