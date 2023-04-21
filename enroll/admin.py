from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Nhan_vien)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'ho_lot_thuong_dung', 'ten_thuong_dung', 'vitri_CV', )
    search_fields = ('ten_thuong_dung',)


@admin.register(Quanly)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id',  'ten_thuong_dung')
    search_fields = ('ten_thuong_dung',)



