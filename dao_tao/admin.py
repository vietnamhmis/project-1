from django.contrib import admin

from .models import Noidungdaotao, Lopdaotao, giangvien
from import_export.admin import ImportExportModelAdmin


admin.site.register(Noidungdaotao)
admin.site.register(Lopdaotao)
admin.site.register(giangvien)

