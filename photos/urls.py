from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('pho',views.gallery,name= 'gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
