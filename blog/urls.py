# -*- coding: utf-8 -*-
from django.urls import path
from . import views

__author__ = "suvorovao"


urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
