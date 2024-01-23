from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heads/', views.heads_tails, name='heads_tails'),
    path('dice/', views.dice, name='dice'),
    path('number/', views.random_number, name='random_number'),
    
]