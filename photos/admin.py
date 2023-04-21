from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin

from .models import Photo, Category

admin.site.register(Category)

@admin.register(Photo)
class PersonAdmin(ImportExportModelAdmin):
     list_display = ('id', 'category', 'image', 'description')
