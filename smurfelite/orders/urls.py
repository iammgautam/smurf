from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/cart/', views.cart, name='cart'),
    path('orders/checkout/', views.checkout, name='checkout'),
]
