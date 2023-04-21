from django.contrib import admin


from import_export.admin import ImportExportModelAdmin

from .models import *



#--------
# Register your models here.
@admin.register(Congviec_nangluc)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id',  'name', 'chucdanh_CV', 'nangluc_cv','Muc_thanhthao_nluc', 'stt')
#------

@admin.register(Danhgia_nluc)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id','Diem_tu_danhgia', 'Diem_dat','Nhanvien_dg_nangluc','TenNangluc_congviec', 'tu_danhgia_dapung'  )
#------

@admin.register(tong_nl)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id','user','Ketqua_danhgia',  'user')






