from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Dinhbien_HC, Dinhbien_base, Dinhbien_ca, tonghopdinhbien

@admin.register(Dinhbien_HC)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Noi_dung_cviec', 'dinhbienhc', 'Tong_phut_1nam', 'to_nhom', 'chuc_vu')
   # search_fields = ('chuc_vu')
    list_filter = ['don_vi', 'bo_phan', 'to_nhom', 'chuc_vu', ]

@admin.register(Dinhbien_ca)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','chuc_vu', 'Tong_phut_1namc', 'dinhbienca')
    list_filter = [ 'don_vi', 'bo_phan', 'to_nhom', 'chuc_vu','Tong_phut_1namc', 'dinhbienca']

@admin.register(tonghopdinhbien)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'don_vi', 'bo_phan', 'to_nhom', 'chuc_vu', 'chucdanh_dinhbien', 'Tong_phut_1nam','tong_dinhbien')
    list_filter = [ 'chucdanh_dinhbien', 'bo_phan', 'to_nhom', 'chuc_vu',]

