from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import *

app_name: "nangluc"
urlpatterns = [

    path('knl2/', Congviec_nangluc_list_2, name='Congviec_nangluc_list_2'),
    path('knl3/', Khung_nangluc_intatca, name='Khung_nangluc_intatca'),
    path('knl/', Khung_nangluc_list, name=''),

    path('knl/<int:id>/', update_Congviec_nangluc, name='update_Congviec_nangluc'),#dinhgia_up-2.html
    path('knl/delete/<int:id>/', del_Congviec_nangluc, name='del_Congviec_nangluc'),
    path('knlt/', add_khung_nangluc, name='add_khung_nangluc'),
    path('nlcm/', add_khung_nanglucchuyenmon, name='add_khung_nanglucchuyenmon'),#Khung_nanglucCM_add.html

    path('danhgia/', Danhgia_nangluc_list, name='Danhgia_nangluc_list'),#Danhgia_nangluc_chitiet.html
    path('danhgia2/', Danhgia_nangluc_list2, name='Danhgia_nangluc_list2'),#Danhgia_nangluc2.html

#    path('danhgia/<int:id>/', Danhgia_nangluc_upQL, name='Danhgia_nangluc_upQL'),#Danhgia_up.html
    path('danhgiacn/<int:id>/', Danhgia_nangluc_update_cannhan, name='Danhgia_nangluc_update_cannhan'),#Danhgia_up_CN.html

    path('themdg/', add_danhgia_nangluc, name='add_danhgia_nangluc'),#Danhgia_nangluc_add

    path('kqad/', add_ketqua_nangluc, name='add_ketqua_nangluc'),
    path('kqdg/', Danhgia_nangluc_list, name='kequa_nangluc_list'), # In ca nhan
    path('danhgia3/', Danhgia_nangluc_list_intatca, name='Danhgia_nangluc_list_intatca'), # In ca nhan


    path('nld/', OrderSummaryView1.as_view(), name='order-summary1'),
    path('in_nl/', views.index_nl, name='dashboard-index'),



       #-----------------------------------KHUNG Năng lực



    #-----------------------------------Quan lý Đanh giá năng lực
    path('dgnl/', views.danhgianangluc_view,name="danhgianangluc_view"),
    path('dgnl/insert_student', views.InsertStudent,name="insert_nangluc"),
    path('dgnl/update_all', views.update_all,name="update_all_nangluc"),
    path('dgnl/delete_data', views.delete_data,name="delete_data_nangluc"),
    #---------------------------------
    path('khgnl/', views.khungnangluc_view,name="Khung_nangluc_list"),
    path('khgnl/insert_student', views.Insertkhung_nangluc,name="insert_khungnangluc"),
    path('khgnl/update_all', views.update_all_k,name="update_khung_nangluc"),
    path('khgnl/delete_data', views.delete_data_k,name="delete_data_nangluc"),

    #----------------------------------Nhanvien...dgnlnv
    path('dgnlnv/', views.danhgianangluc_view_nhanvien,name="danhgianangluc_view_nv"),#Danhgia_nangluc_nv.html
    path('dgnlnv/insert_student', views.Insert_nangluc_nv,name="insert_nangluc_nv"),
    path('dgnlnv/update_all', views.update_all_nhanvien,name="update_all_nangluc_nv"),
    path('dgnlnv/delete_data', views.delete_nv_nhanvien,name="delete_data_nangluc_nv"),





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)