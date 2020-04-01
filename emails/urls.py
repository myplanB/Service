from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from emails import views

urlpatterns = [
    path('send/', views.index,name='index'),
    path('upload_file/',views.upload_file,name='upload_file')
]
