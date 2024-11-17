
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'enquetes'


urlpatterns = [
 path("test-login/", views.test_template, name="test_login"),
]