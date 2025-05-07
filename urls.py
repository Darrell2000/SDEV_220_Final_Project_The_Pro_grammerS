from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_view, name='menu'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
]

