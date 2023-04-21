from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .views import *

app_name: "crud_ajax"
urlpatterns = [

    path('crud/',  views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/',  views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/',  views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
    path('ajax/crud/delete/',  views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)