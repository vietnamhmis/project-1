from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


app_name: "kpi_bsc"
urlpatterns = [
    path('dg_kpinv/', views.danhgiakpi_vnv,name="danhgia_kpi_view_nv"),
    path('dg_kpinv/insert_student', views.Insert_kpi_nv,name="Insert_kpi_nv"),
    path('dg_kpinv/update_all', views.update_kpi_nhanvien,name="update_kpi_nhanvien"),
    path('dg_kpinv/delete_data', views.delete_kpi_nhanvien,name="delete_kpi_nhanvien"),

    path('kh_kpi/', views.Khungkpi_View,name="Khungkpi_View"),
    path('kh_kpi/insert_student', views.Insertkhung_kpi,name="Insertkhung_kpi"),
    path('kh_kpi/update_all', views.updatekhung_kpi,name="updatekhung_kpi"),
    path('kh_kpi/delete_data', views.delete_khungkpi,name="delete_khungkpi"),

    path('dg_kpi/', views.danhgia_kpi_view,name="danhgia_kpi_view"),
    path('dg_kpi/insert_student', views.Insert_kpi,name="insert_kpi"),
    path('dg_kpi/update_kpi', views.update_kpi,name="update_kpi"),
    path('dg_kpi/delete_kpi', views.delete_kpi,name="delete_kpi"),

#-------------
    path('kkpi2/', Khung_kpi_list_2, name='Khung_kpi_list_2'),
    path('kkpit/', add_khung_kpi, name='add_khung_kpi'),
    path('kkpil/', Khung_kpi_list, name='Khung_kpi_list'),#Khung_kpi_list.html
#-------------

    path('kkpi/<int:id>/', update_Khung_KPI, name='update_Khung_KPI'),#Khung_KPI_up.html
    path('kkpi/delete/<int:id>/', del_Khung_KPI, name='del_Khung_KPI'),#Khung_KPI_delete.html
    #path('knlt/', add_khung_nangluc, name='add_khung_nangluc'),
    #path('nlcm/', add_khung_nanglucchuyenmon, name='add_khung_nanglucchuyenmon'),#Khung_nanglucCM_add.html

    path('danhgiakpi/', danhgia_KPI_list, name='danhgia_KPI_list'),#Danhgia_nangluc_chitiet.html
    path('danhgiakpi_2/', Danhgia_kpi_list2, name='Danhgia_kpi_list2'),#Danhgia_nangluc2.html
    path('danhgiakpi/<int:id>/', Danhgia_KPI_update, name='Danhgia_KPI_update'),#Danhgia_KPI_up.html
    #path('danhgiacn/<int:id>/', Danhgia_nangluc_update_canhan, name='Danhgia_nangluc_update_canhan'),#Danhgia_up.html
    path('tkpi/', add_danhgia_kpi, name='add_danhgia_kpi'),#Danhgia_nangluc_add
    #path('kqad/', add_ketqua_nangluc, name='add_ketqua_nangluc'),
    #path('kqdg/', Danhgia_nangluc_list, name='kequa_nangluc_list'), # In ca nhan
    #path('danhgia3/', Danhgia_nangluc_list_intatca, name='Danhgia_nangluc_list_intatca'), # In ca nhan


    #-----------------------------------



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)