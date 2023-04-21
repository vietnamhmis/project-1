from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'dao_tao'
urlpatterns = [
    path('daotao/', views.lop_daotao, name='gallery'),
    path('daotao/<str:pk>/', views.viewChuongtrinh_daotao, name='viewChuongtrinh_daotao'),
    path('adddt/', views.add_lop_daotao, name='add_lop_daotao'),
    path('daotao/delete/<int:id>/', views.del_daotao, name='del_daotao'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

