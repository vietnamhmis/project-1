from django.test import TestCase

# Create your tests here.
import django_filters
from django_filters import DateFilter, CharFilter
from .models import *

#********>>>>>>> Đây là chương trình LỌC Danh mục KPI CÁ NHÂN-----------------------------------------
class UserFilter(django_filters.FilterSet):
    class Meta:
         model = dmkpi
         fields = ['Ten_KPI', 'LoaiCV']
         filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': django_filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }
    #Ten_KPI = CharFilter(field_name='Ten_KPI', lookup_expr='icontains')
    #LoaiCV__name = django_filters.CharFilter(lookup_expr='icontains')
    #LoaiCV = CharFilter(field_name='LoaiCV', lookup_expr='icontains')
    #class Meta:
     #   model = CViec
       # fields = {
        #    'Ten_KPI': ['contains'],
       #     'LoaiCV': ['exact'],
      #  }
        #exclude = ['Don_vi_tinh', 'Tan_xuat_d_gia', 'Ti_trong',]

#<<<<<<... Kết thúc chương trình LỌC Danh mục KPI cá nhân............................................



#********>>>>>>> Đây là chương trình LỌC KPI CÁ NHÂN-----------------------------------------
class KPI_Filter(django_filters.FilterSet):
    Ten_KPI = CharFilter(field_name='Ten_KPI', lookup_expr='icontains')
    class Meta:
        model = giao_KPI
        fields = ['Ten_KPI','Nguoigiao','DVi_giao','Cviec_phan_KPI']
#<<<<<<... Kết thúc chương trình LỌC KPI cá nhân............................................

#********>>>>>>> Đây là chương trình LỌC Danh mục KPI ĐƠN VỊ-----------------------------------------
class D_muc_KPI_Dvi_Filter(django_filters.FilterSet):
    #Ma_KPo = CharFilter(field_name='Ma_KPo', lookup_expr='icontains')
    Ten_KPI = CharFilter(field_name='Ten_KPI', lookup_expr='icontains')
    class Meta:
        model = Dmkpi_dv
        fields = ['Vien_canh_cluoc', 'Dv_quanly_KPI', 'Ten_KPI',]

class Dmkpi_dv_Filter(django_filters.FilterSet):
    #Ma_KPo = CharFilter(field_name='Ma_KPo', lookup_expr='icontains')
    Ten_KPI = CharFilter(field_name='Ten_KPI', lookup_expr='icontains')
    class Meta:
        model = Dmkpi_dv
        fields = ['Vien_canh_cluoc', 'Dv_quanly_KPI', 'Ten_KPI',]


#<<<<<<... Kết thúc chương trình LỌC Danh mục KPI ĐƠN VỊ............................................
