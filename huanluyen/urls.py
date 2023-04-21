from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
from .views import web_index, web_about, web_course, web_blog, web_Contac, bangluong_list

app_name = 'huanluyen'
urlpatterns = [
    #-------------
    path('vkhqlnnl/', bangluong_list, name='web_index'),
    path('ha/', web_about, name='web_about'),
    path('hc/', web_course, name='web_course'),
    path('hb/', web_blog, name='web_blog'),
    path('hc/', web_Contac, name='web_Contac'),
    #------------

    path('tuvan/', views.lop_tu_van, name='tu_van'),
    path('tuvan/<str:pk>/', views.viewChuongtrinh_tu_van, name='viewChuongtrinh_tu_van'),
    path('addhl/', views.add_lop_tu_van, name='tu_van_add'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

