from django.urls import path

from . import views

from .views import (
    ItemDetailView,
    OrderSummaryView,
    CheckoutView,
    HomeView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    home_select,
)



#https://www.youtube.com/watch?v=7fG4eHe7ZRM
urlpatterns = [
    path('hhh/', HomeView.as_view(), name='HomeView'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),#product.html"
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),


    path('', views.home_select, name='home_select'), ###Thự nghiệm smart



]

