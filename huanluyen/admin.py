from django.contrib import admin

from .models import Noidungtu_van, Loptu_van, giangvien,  Duan_c_giao, khach_hang

from import_export.admin import ImportExportModelAdmin



#admin.site.register(Loptu_van)
@admin.register(Loptu_van)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','name', 'content', 'image')



@admin.register(khach_hang)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','image_kh', 'name_kh', 'content_Kh')

@admin.register(giangvien)
class PersonAdmin(ImportExportModelAdmin):
      list_display = ('id', 'CTV','image','name')

@admin.register(Noidungtu_van)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'tenlop')

@admin.register(Duan_c_giao)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id','name')