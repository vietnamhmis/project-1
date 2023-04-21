from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import registerUser, loginUser, logout_User, privatePage

app_name = 'login'

urlpatterns = [
    path('taonv/', registerUser.as_view(),name= 'register'),

    path('dangnhap/', loginUser.as_view(), name='loginUser'),
    path('thoat/', views.logout_User, name='lgout_user'),
    path('pri/', privatePage.as_view(), name='private'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

