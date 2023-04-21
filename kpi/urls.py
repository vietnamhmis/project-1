from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *


#app_name = 'enroll' #Khai báo thi file html mới chay cổng post
from django.contrib import admin
from django.urls import path

from django.conf.urls import url
app_name = 'kpi'
urlpatterns = [
    #Lọc dữ liệu:


#----------------------------------end

#
    path('timloc/', BootstrapFilterView, name="BootstrapFilterView"),
    # Js Create-del, updat data
    path('rq/',views.index),

    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^create/$', views.product_create, name='product_create'),
    url(r'^products/(?P<pk>\d+)/update/$', views.product_update, name='product_update'),
    url(r'^products/(?P<pk>\d+)/delete/$', views.product_delete, name='product_delete'),


























    path('jjj', TaskView.as_view(), name="task"),
    path('view', ViewTaskView.as_view(), name="view"),
    path('view/<int:pk>', TaskDeleteView.as_view(), name="delete"),

#***>>> --- Chương trình THÊM/SỬA/XÓA Danh mục KPI CÁ NHÂN-----------------------------------------
    path('kpi/', add_kpi, name="add_kpi"),
    path('kpi/delete/<int:id>/', delete_data, name="del_dmkpi"),
    path('kpi/<int:id>/', update_data,name="update_dmkpi"),
    path('kpix', views.ex_excel, name= "ex_excel"),

  #>>>>> ..KẾT THÚC chương trình THÊM/SỬA/XÓA Danh mục KPI CÁ NHÂN-----------------------------------------
#***>>> --- Chương trình  KPI CÁ NHÂN-----------------------------------------
    path('kpicn/', add_kpicn, name="add_kpicn"),
    path('kpicn/delete/<int:id>/', delete_kpicn, name="delete_kpicn"),
    path('kpicn/<int:id>/', update_kpicn,name="update_kpicn"),

  #>>>>> ..KẾT THÚC chương trình  KPI CÁ NHÂN-----------------------------------------

#***>>>---Đây là chương trình THÊM/SỬA/XÓA Danh mục KPI ĐƠN VỊ-----------------------------------------
    path('kpidv/', views.kpi_donvi, name="kpi_dv_v"),
    path('delete/<int:id>/', views.delete_datadv, name="delete_dv"),
    path('kpidv/<int:id>/', views.update_kpidv,name="updatedv"),
    path('kpidvx', views.ex_exceldv, name= "ex_exceldv"),
  #>>>>>.. KẾT THÚC chương trình THÊM/SỬA/XÓA Danh mục KPI CÁ NHÂN-----------------------------------------

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)