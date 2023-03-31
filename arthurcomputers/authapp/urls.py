from django.urls import path
from authapp import views
from .views import About

urlpatterns = [
    path('',views.Home, name="Home"),
    path('about', About, name='about'),
    ]