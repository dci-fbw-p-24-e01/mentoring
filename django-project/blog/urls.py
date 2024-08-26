from django.urls import path

from . import views

urlpatterns = [
    path('posts/', views.blog_home, name='blog_home')

]