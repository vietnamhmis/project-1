from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import dinhbien_hc_list, update_dinhbienhc, del_dinhbienhc, add_dinhbiehc, dinhbien_ca_list, \
    update_dinhbienca, del_dinhbienca, add_dinhbienca, dinhbien_th, tonhom_dinhbien, dinhbien_hc_chi_tiet, \
    dinhbien_ca_chi_tiet, bophan_dinhbien, donvi_dinhbien

urlpatterns = [
    path('dinhbienhc/', dinhbien_hc_list, name='dinhbien_hc_list'),

    path('dinhbienhc/<int:id>/', update_dinhbienhc, name='update_dinhbienhc'),
    path('dinhgbienhc/delete/<int:id>/', del_dinhbienhc, name='del_dinhbienhc'),
    path('add_hc/', add_dinhbiehc, name='add_dinhbiehc'),

    path('dinhbienca/', dinhbien_ca_list, name='dinhbien_ca_list'),

    path('dinhbienca/<int:id>/', update_dinhbienca, name='update_dinhbienca'),

    path('dinhgbienca/delete/<int:id>/', del_dinhbienca, name='del_dinhbienca'),
    path('add_ca/', add_dinhbienca, name='add_dinhbienca'),
    #----------chittiet ca


    path('dinhbien/', dinhbien_th, name='dinhbien_th'),

    path('dinhbiend/<int:id>/', donvi_dinhbien, name='donvi_dinhbien'),
    path('dinhbienb/<int:id>/', bophan_dinhbien, name='bophan_dinhbien'),
    path('dinhbient/<int:id>/', tonhom_dinhbien, name='tonhom_dinhbien'),


    path('dinhbiench/<int:id>/', dinhbien_hc_chi_tiet, name='dinhbien_hc_chi_tiet'),#dinhbien_hc_list_cv.html
    path('dinhbientc/<int:id>/', dinhbien_ca_chi_tiet, name='dinhbien_ca_chi_tiet'), #dinhbien_ca_list_cv.html



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)