from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *


@admin.register(bangluong)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'Nhom_luong', 'Bac', 'Heso', 'Muc_luong']
   search_fields = ('Nhom_luong',)

@admin.register(bangluong_chinh)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'Nhom_luong', 'diem', 'Bac_1']



@admin.register(hd_laodong)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ['id', 'Ho_ten', 'Loai_hd', 'Day_nangluong', 'Tu_ngay', 'Den_ngay', 'Ht_traluong', 'Heso', 'Bac', 'Muc_luong']
   search_fields = ('Ho_ten', 'Loai_hd',  'Muc_luong',)


@admin.register(luongthang)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ['id', 'Thang_tra_luong', 'Nam','hoten_nhanvien', 'Muc_luong']
    search_fields = ('hoten_nhanvien', 'Thang_tra_luong',)

@admin.register(DmChamcong)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ['id', 'ten_danhmuc', 'kyhieu_cc',]
    search_fields = ('ten_danhmuc',)

@admin.register(Chamcongchitiet)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ['id', 'Nhan_vien','bo_phan', 'don_vi', 'thang', 'nam']
    search_fields = ('Nhan_vien','Ngaycham')

@admin.register(Chamcong)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ['id', 'user','kyhieu_cc', 'Ngay_1', ]
    search_fields = ('user',)


@admin.register(Phuongan_luongbhxh)
class PersonAdmin(ImportExportModelAdmin):
       list_display = ['id', 'Nhom_luong','Nhanvien', 'Luong_cu', 'Bac_2',
                       'CL_Luong_BHXH_PA_1','CL_Luong_moi_PA_1', 'luong_toi_thieu']


