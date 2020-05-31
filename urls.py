# -*- coding: utf-8 -*-
import aldryn_addons.urls

from django.urls import include, path
from aldryn_django.utils import i18n_patterns

urlpatterns = [
    # add your own patterns here
    path('', include('pages.urls')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
