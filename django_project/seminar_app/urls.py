from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('heads/', views.heads_tails, name='heads_tails'),
    path('dice/', views.dice, name='dice'),
    path('number/', views.random_number, name='random_number'),
    path('authors/', views.authors_view, name='authors'),
    path('posts/', views.post_view, name='posts'),
    
]