from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include

from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path as url

#-----------
from django.urls import path

from django.contrib import admin
from django.urls import path


#------
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Courses.urls')),
    path('', include('enroll.urls')),
    path('', include('nhansu.urls')),
   # path('', include('login.urls')),
    path('', include('luong.urls')),
    path('', include('dao_tao.urls')),
    path('', include('huanluyen.urls')),
    path('', include('mota_cv.urls')),
    path('', include('dinhbien.urls')),
    path('', include('kpi.urls')),
    path('', include('nangluc.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls')),
  #  path('', include('bsc.urls')),

    path('', include('kpi_bsc.urls')),
    path('', include('crud_ajax.urls')),

    #path('', include('CRUDAPP.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)









