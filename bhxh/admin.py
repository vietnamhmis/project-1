from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.





#admin.site.register(BHXHTN)

from django.contrib import admin
from .models import BHXHTN
# Register your models here.

@admin.register(BHXHTN)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'SOBHXH','HOTEN','NGAYSINH', 'GIOITINH', 'MA_BV', 'SOBL',)
    search_fields = ('HOTEN',)