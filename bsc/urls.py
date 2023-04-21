from django.urls import path

from . import views

from .views import (
    ItemDetailView,
    OrderSummaryView1,
    CheckoutView,
    HomeView,
    add_to_kpi,
    remove_from_kpi,
    remove_single_item_from_kpi,
    danhmuc_KPI,
update_kpi,
update_single_item_from_cart,
PaymentView,
)

app_name = 'bsc'
urlpatterns = [
    path('bsc2/', HomeView.as_view(), name='home'),
    path('bsc/', danhmuc_KPI, name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product1'),
    
    path('checkout/', CheckoutView.as_view(), name='checkout'),

    path('order-summary1/', OrderSummaryView1.as_view(), name='order-summary1'),

    path('add_to_kpi/<slug>/', add_to_kpi, name='add_to_kpi'),

    path('remove-from-kpi/<slug>/', remove_from_kpi, name='remove-from-kpi'),

    path('remove-item-from-kpi/<slug>/', remove_single_item_from_kpi,
         name='remove_single_item_from_kpi'),

    path('update_item_from_cart/<slug>/', update_single_item_from_cart,
         name='update_single_item_from_cart'),

    path('kup/<int:id>/', update_kpi,name="update_kpi"),

    path('payment/<payment_option>/', PaymentView.as_view(),name="payment"),

]
















