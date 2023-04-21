from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

#-----------
from django.urls import path

from django.contrib import admin

from django.urls import include, path

from . import views
from .views import *
#------
urlpatterns = [
    path('aap/', views.HomePage,name="homeh"),
    path('aap/insert_student', views.InsertStudent,name="insert"),
    path('aap/update_all', views.update_all,name="update_all"),
    path('aap/delete_data', views.delete_data,name="delete_data"),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)









