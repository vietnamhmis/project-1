from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import list_bhxhtn, bhxh_profile, update_bhxh, delete_BHXH, load_diaphuong



urlpatterns = [
    path('bhyt/', list_bhxhtn, name='bhxhtn_list'),# bhxh/bhxhtn_list.html

    path('bhtn/<int:id>/', bhxh_profile, name='bhxh_tokhai'),#bhxh/bhxhtn_tokhai.html'
    path('delete_BHXH/delete/<int:id>/', delete_BHXH, name="delete_BHXH"),#bhxh/bhxh_delete.html
    path('bhxhtn/<int:id>/', update_bhxh,name="update_bhxh"),#bhxh/bhxhtn_update.htm
    path('load-dp/', load_diaphuong, name='load_diaphuong'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)