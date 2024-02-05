from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('heads/<int:count>/', views.heads_tails, name='heads_tails'),
    path('dice/<int:count>/', views.dice, name='dice'),
    path('number/<int:count>/', views.random_number, name='random_number'),
    path('authors/', views.authors_view, name='authors'),
    path('posts/', views.post_view, name='posts'),
    path('authors_posts/<int:author_id>', views.authors_posts_list, name='authors_posts'),
    path('post1/<int:post_id>', views.post, name='post1'),
    path('game/', views.choose_game, name='game'),
    path('author/', views.author_add, name='author'),
    path('post/', views.post_add, name='post'),
    
] 