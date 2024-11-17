# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include

from apps.registro import views  # add this

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts', include('allauth.urls')),

]
