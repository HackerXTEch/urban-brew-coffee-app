from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name='home'),
    path('instantcoffee/', views.instantcoffee, name='instantcoffee'),
    path('gifts/', views.gifts, name='gifts'),
    path('accessories/', views.accessories, name='accessories'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='cont'),

]