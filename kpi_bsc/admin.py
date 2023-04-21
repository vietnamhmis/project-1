from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import *



#--------
# Register your models here.
@admin.register(Khung_kpi)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id',  'ti_trong', 'name', 'chucdanh_CV', 'kpi_cv', 'stt')

@admin.register(Danhgia_KPI)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id',  'Landanhgia_KPI', 'Nhanvien_dg_KPI', 'Ten_kpi', )