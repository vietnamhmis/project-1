from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *



@admin.register(Mota_Cv)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id','ma_tenvitri','Ten_Nhom_CV', 'Ten_vitri_full', 'Ten_theoluong','don_vi', 'bo_phan','to_nhom', 'mota_Cong_viec']
   search_fields = ('don_vi', 'bo_phan','to_nhom', 'mota_Cong_viec')

@admin.register(Mota_Cv7)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id','Ten_Nhom_CV', 'chuc_danh','tong_diem7', 'Nhom_luong', 'Ten_vitri_full', 'bo_phan','to_nhom', 'mota_Cong_viec']
    #list_display = ['id','ten_nghe_NNDH','Ten_Nhom_CV', 'Ten_vitri_full', 'tong_diem7','Nhom_luong', 'bo_phan','to_nhom', 'mota_Cong_viec']
   search_fields = ('don_vi', 'bo_phan','to_nhom', 'mota_Cong_viec')


@admin.register(Chuc_danh)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id','Ten', 'Chuc_trach']
