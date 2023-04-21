from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin


# Register your models here.


@admin.register(Product)
class PersonAdmin(ImportExportModelAdmin):
       list_display = ('id', 'name',)



@admin.register(Task)
class PersonAdmin(ImportExportModelAdmin):
       list_display = ('id', 'name',)









@admin.register(Author)
class PersonAdmin(ImportExportModelAdmin):
       list_display = ('id', 'name',)


@admin.register(Category)
class PersonAdmin(ImportExportModelAdmin):
       list_display = ('id', 'name',)

@admin.register(Journal)
class PersonAdmin(ImportExportModelAdmin):
       list_display = ('id', 'title',)



@admin.register(Don_vi_tinh)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ('id', 'Don_vi_tinh',)
   search_fields = ('Don_vi_tinh',)

# Register your models here.

@admin.register(Phan_KPI)
class PersonAdmin(ImportExportModelAdmin):
   list_display = ('id', 'Ten_KPI','Cviec_phan_KPI', 'Tan_xuat_d_gia','Don_vi_tinh','Dv_quanly_KPI')
   search_fields = ('Ten_KPI',)


@admin.register(Dmkpi_dv)
class PersonAdmin(ImportExportModelAdmin):
  list_display = ('id','Ten_KPo', 'Ma_KPo','Ten_KPI','Don_vi_tinh','Chitieu_KPI','Ti_trong',  'Tan_xuat_d_gia',)
  search_fields = ('Ten_KPI',)

@admin.register(dmkpi)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'LoaiCV','Ten_KPI',  'Don_vi_tinh', 'Tan_xuat_d_gia', 'Ngaytao', 'Ngay_update')
    list_filter = ['LoaiCV']
    search_fields = ['Ten_KPI',]

