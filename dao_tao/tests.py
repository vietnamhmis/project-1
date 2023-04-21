from django.test import TestCase

# Create your tests here.
@admin.register(Noidunghuanluyen)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('id', 'description','tenlop', 'ngay_huanluyen','educator','excerpt','number_lessons','image' )
    search_fields = ('tenlop',)



    #---------
#DATABASES = {
 #   'default': {
 #       'ENGINE': 'django.db.backends.mysql',
  #      'NAME': 'nhansu_hatien',
   #     'USER': 'huyhoang',
    #    'PASSWORD': '2009huyhoang',
 #   }
#}