from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import  add_nhanvien, delete_nhanvien, update_nhanvien,  \
    list_nhanvien, employee, nhanvien_profile_3, nhanvien_profile_up, nhanvien_profile_up_tt1, \
     donvi_nhanvien, tonhom_nhanvien, bophan_nhanvien, nhanvien_profile_view
from .views import  load_diaphuong,  BaocaoFilter, BaocaoFilter_DSVN

#app_name = 'enroll' #Khai báo thi file html mới chay cổng post

urlpatterns = [
#***>>> --- Chương trình THÊM/SỬA/XÓA Danh mục NHÂN VIỆN----------------------------------------
    path('BaocaoFilter_DSVN/', BaocaoFilter_DSVN, name="BaocaoFilter_DSVN"),
    path('', BaocaoFilter, name="BaocaoFilter"),

    path('employees/', employee, name='employees'),# hiển thi nhân vien dang hình: employes.html
    path('dmnv/', list_nhanvien, name="list_nhanvien"),# enroll/employee_list.html

    path('dmdv/<int:id>/', donvi_nhanvien, name="donvi_nhanvien"),# donvi_nhanvien.  employee_list_nvien_dvi.html

    path('dmbp/<int:id>/', bophan_nhanvien, name="bophan_nhanvien"),# donvi_nhanvien.  employee_list_nvien_bp.html
    path('dmto/<int:id>/', tonhom_nhanvien, name="tonhom_nhanvien"),# donvi_nhanvien.  employee_list_nvien_to.html

    path('nhanvien/', add_nhanvien, name="add_nhanvien"),#enroll/employees_addsua.html------.
    path('ad_nhanvien/', add_nhanvien, name='add_nhanvien_dt'),# thêm nhân viên employee_add_photo.html

    path('nhanvien/delete/<int:id>/', delete_nhanvien, name="delete_nhanvien"),#enroll/employees_delete.html
    path('nhanvien/<int:id>/', update_nhanvien,name="up_nhanvien"),#enroll/employee_update_1.html.html

    path('load-dp/', load_diaphuong, name='load_diaphuong'),


    path('profile/<int:id>/', nhanvien_profile_view, name='nhanvien_profile_view'), #new enroll/employes_profile_3.html
   path('pro/<int:id>/', nhanvien_profile_up, name='nhanvien_profile_up'), #new enroll/employes_profile_3.html
    path('profile/<int:id>/', nhanvien_profile_3, name='nhanvien_profile_3'), #Xem Profie: new enroll/employes_profile_3.html
   # path('pro_up/<int:id>/', nhanvien_profile_up_tt1, name='nhanvien_profile_up_tt1'), #Xem Profie: new enroll/employes_profile_3

  #>>>>> ..KẾT THÚC chương trình THÊM/SỬA/XÓA Danh mục KPI CÁ NHÂN-----------------------------------------

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)