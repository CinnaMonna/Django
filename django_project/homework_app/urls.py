from django.urls import path
from . import views

urlpatterns = [
    path('index1/', views.index1, name='index1'),
    path('about1/', views.about1, name='about1'),
    path('clients/', views.clients_view, name='clients'),
    path('orders/<int:client_id>/', views.orders_by_client_id, name='orders'),
    path('products/<int:order_id>/', views.products_by_order_id, name='products'),
    path('allproducts/<int:client_id>/', views.products_by_client_id, name='allproducts'),
]