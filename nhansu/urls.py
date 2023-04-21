from django.urls import path, include

from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    #----aajax--------------------------------
    path('yt/',  views.YtoView.as_view(), name='crud_ajax'),
    path('ajax/yt/create/',  views.CreateYeu_to_1_trinh_do.as_view(), name='crud_ajax_create'),
    path('ajax/yt/update/',  views.UpdateYeu_to_1_trinh_do.as_view(), name='crud_ajax_update'),
    path('ajax/yt/delete/',  views.DeleteYeu_to_1_trinh_do.as_view(), name='crud_ajax_delete'),
    #-----------------
    path('dva/',  views.Donvi_View.as_view(), name='Donvi_View'),
    path('dvx/crud/create/',  views.Create_donvi.as_view(), name='Create_donvi'),
    path('dvu/crud/update/',  views.Update_ax_Donvi.as_view(), name='Update_ax_Donvi'),

    path('dvd/crud/delete/',  views.Delete_ax_donvi.as_view(), name='Delete_ax_donvi'),

#***>>> --- Chương trình ----------------------------------------
    path('in/', views.index, name='dashboard-index'),
    path('bdnl/', views.index, name='dashboard-index'),
#***>>>---Đây là chương trình THÊM/SỬA/XÓA Danh mục KPI ĐƠN VỊ-----------------------------------------
    path('themto/',add_to, name="add_to"),
    path('thembp/',add_bophan, name="add_bophan"),
    path('themdv/',add_donvi, name="add_donvi"),

#--------------------------------------
    path('dmdv/', listDon_vi, name='listDon_vi'),

    #--------------------------------------

    path('udmdv/<int:id>/', update_donvi, name="update_donvi"),
    path('dmdv/delete/<int:id>/', del_donvi, name="del_donvi"),
#--------------------------------------
    path('dmbp/', list_Bophan, name='list_Bophan'),

    path('dmbp2/', show_products, name='list_Bophan'),


    path('sdmbp/<int:id>/', s_bophan, name='s_bophan'),

    path('udmbp/<int:id>/', update_bophan, name="update_bophan"),
    path('dmbp/delete/<int:id>/', del_bophan, name="del_bophan"),
#--------------------------------------
   # -------------------------------------------
    path('dmto/', list_to, name='list_to'),
    path('dmtos/<int:id>/', update_tonhom, name="update_tonhom"),
    path('sdmto/<int:id>/', s_to_nhom, name='s_to_nhom'),
    path('dmto/delete/<int:id>/', del_to, name="del_to"),

#======
    path('dmvb/', Vanban_q, name="Vanban"),

    path('vbad/', add_vanban, name="add_vanban"),
    path('dmvb/<int:id>/', update_Vanban, name="update_Vanban"),
    path('dmvb/delete/<int:id>/', del_Vanban, name="del_Vanban"),

 #------------------Năng lực-------------
    path('dmnl/', Nangluc_list, name="list_nangluc"),#Nangluc_list.html
    path('dmnlq/', Nangluc_list_q, name="Nangluc_list_q"),#Nangluc_list.html



    path('nl/<int:id>/', nangluc_chitiet, name="nangluc_chitiet"),#nangluc_chitiet.html
    path('dmnl2/', list_nangluc_2, name="list_nangluc_2"),
    path('nl2/<int:id>/', nangluc_chitiet2, name="nangluc_chitiet2"),
    path('adnl/', add_nangluc, name="add_nangluc"),
    path('dmnl/<int:id>/', update_nangluc, name="update_nangluc"),
    path('dmnll/delete/<int:id>/', del_nangluc, name="del_nangluc"),
    path('adnluc/', add_nangluc_thu, name="add_nangluc"),

    #------------------KPI---------------
    path('dmkpi/', kpi_list, name="kpi_list"),#kpi_list.html
    path('add_kpi/',add_kpi, name="add_kpi"),

    path('dmkpi/<int:id>/', kpi_chitiet, name="kpi_chitiet"),#KPI_chitiet.html
    path('dmkpiup/<int:id>/', update_kpi, name="update_kpi"),
    path('dmkpi/delete/<int:id>/', del_kpi, name="del_kpi"),




#>>>>>.. KẾT THÚC chương trình THÊM/SỬA/XÓA Danh mục KPI CÁ NHÂN-----------------------------------------
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
