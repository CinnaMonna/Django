from django.urls import path
from . import views

urlpatterns = [
    path('index1/', views.index1, name='index1'),
    path('about1/', views.about1, name='about1'),
    path('clients/', views.clients_view, name='clients')       
]