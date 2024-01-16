from django.contrib import admin
from django.urls import path
from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns ('',
    url(r'^$', views.callback),
    )