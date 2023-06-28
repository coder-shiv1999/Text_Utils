from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('modify',views.modify,name='modify'),
]
