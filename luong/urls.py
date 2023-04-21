from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from . import views

from django.urls import re_path
from django.urls import include, path

from .models import file_re

from .views import *

from .views import bangluong_list, hopdong_view, update_hopdong, del_hopdong, del_nangluong, update_nangluong, \
    nangluong_view,  luongthang_nhanvien, hopdongchitiet, luongthang_tamung

urlpatterns = [
   # path('luong/', bangluong_list, name='bangluong_list'), #dinhgia_list1.html
    path('add_bangluong/', add_bangluong, name='add_bangluong'),
    path('yto_luong/<int:id>/', yto_luong, name='7yto_luong'),


    path('luong/', bangluong_chinh_list, name='bangluong_list'), #dinhgia_list1.html
    path('luongbhxh/', bangluong_BHXH_list, name='bangluong_BHXH'), #dinhgia_list1.html
    path('luongthang/', luong_thang, name='luongthang_list'), #dinhgia_list1.html
    path('luongthang/<int:id>/', luongthang_nhanvien, name='luongthang_nhanvien'), #luongthang_nhanvien_chitiet.html
    path('luongtamung/', luongthang_tamung, name='luongthang_tamung'), #luongthang_tamung.html
    path('luong_tamung_add/', luong_tamung_add, name='luong_tamung_add'), #Tamung_add.html

    #-----

    path('add_PA_xepluong/', add_paluong, name='PA_luong'),

    path('xepluong/', xepluong, name='xepluong'),


    path('nvhd/<int:id>/', nhanvien_hopdong, name='nhanvien_hopdong'),

    #|---------
    path('add_hopdong/', add_hopdong, name='add_hopdong'),
    path('hopdong/', hopdong_view, name='hopdong_view'),
    path('hopdong/<int:id>/', update_hopdong, name="update_hopdong"),
    path('hopdong/delete/<int:id>/', del_hopdong, name="del_hopdong"),
    path('hopdongchitiet/<int:id>/', hopdongchitiet, name="hopdongchitiet"),
    path('chamdut_hopdong/<int:id>/', chamdut_hopdong, name="chamdut_hopdong"),




    path('add_nangluong/', add_nangluong, name='add_nangluong'),
    path('nangluong/', nangluong_view, name='nangluong_view'),
    path('nangluong/<int:id>/', update_nangluong, name="update_nangluong"),
    path('nangluong/delete/<int:id>/', del_nangluong, name="del_nangluong"),

    path('dieudong/', dieu_dong_view, name='dieu_dong_view'),
    path('dieudong/<int:id>/', update_dieu_dong, name="update_dieu_dong"),
    path('dieudong/delete/<int:id>/', del_dieu_dong, name="del_dieu_dong"),

    path('bonhiem/', bo_nhiem_view, name='bo_nhiem_view'),
    path('bonhiem/<int:id>/', update_bonhiem, name="update_bonhiem"),
    path('bonhiem/delete/<int:id>/', del_bonhiem, name="del_bonhiem"),

    path('chamcong/', chamcong_thang, name ='chamcong_thang'),
    path('achamcong/', add_chamcong, name ='add_chamcong'),

    path('ddd/', views.Luonglistviews.as_view(), name='Luonglistviews'),
    path('test/', render_pdf_view, name='render_pdf_view'),
    path('test/<pk>', luong_render_pdf_view, name='luong_render_pdf_view'),
  #  path('file_re/', file_re, name='file_re')



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)