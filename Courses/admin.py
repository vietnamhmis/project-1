from django.contrib import admin
from . models import Courses
# ImportExportModelAdmin----------------
from import_export.admin import ImportExportModelAdmin
# ImportExportModelAdmin----------------

# Register your models here.
#class CourseAdmin(admin.ModelAdmin):
   # list_display = ('name', 'educator','excerpt', 'picture', 'video',)
   # search_fields = ('name',)
    #admin.site.register(Courses,CourseAdmin)


# ImportExportModelAdmin----------------
@admin.register(Courses)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'educator', 'description', 'excerpt', 'number_lessons', 'picture', 'video')
    search_fields = ('name',)


