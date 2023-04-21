from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from .views import *
urlpatterns = [
#-----------------------------------Chức danh:
    path('dmcd/', views.dm_chucdanh,name="dm_chucdanh"),
    path('dmcd/insert_student', views.Insertchucdanh,name="Insertchucdanh"),
    path('ddmcd/update_chucdanh', views.update_chucdanh,name="update_chucdanh"),
    path('dmcd/delete_chucdanh', views.delete_chucdanh,name="delete_chucdanh"),

#-----------------------------------Vị trí 7 yêu tố:
    path('dmvt/', views.dm_vitricv,name="dm_vitricv"),
    path('dinhgia7/', dinhgia_list_7yto, name='dinhgia_list_7yto'),  # dinhgia_list_7yto.html.html
    path('dinhgia7/<int:id>/', update_dinhgia7, name='update_dinhgia7'),  # dinhgia_up-2.html
    path('motacv7/<int:id>/', view_motacv_chitiet7, name='view_motacv_chitiet77'),
    path('motacv/', add_motacv, name='add_motacv'),#mota_cv/dinhgia_add_mota.html# dang chay chuong trinh smart
    path('update_mota_7/<int:id>/', update_mota_7, name='update_mota_7'),
    path('motacv7ctiet/<int:id>/', view_motacv_chitiet77, name='view_motacv_chitiet7'),

#-----------------------------------Vị trí 7 yêu tố:
    path('dinhgia/', dinhgia_list, name='dinhgia_list'), #dinhgia_list1.html
    path('dinhgia/<int:id>/', update_dinhgia, name='update_dinhgia'),#dinhgia_up-2.html
    path('dinhgia/delete/<int:id>/', del_dinhgia, name='del_dinhgia'),

    path('motacv/<int:id>/', view_motacv_chitiet, name='view_motacv_chitiet'),#mota_cv/test.html# dang chay chuong trinh smart
    path('dinhgiamcv/<int:id>/', update_mota, name='update_mota'),
    path('load-bophan/', load_bophans, name='load_bophans'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)