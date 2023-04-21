import datetime
from django.core import validators
from django import forms

from django.conf import settings
from .models import giao_KPI,  dmkpi, Dmkpi_dv

##********>>>>>>> ......................................

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'dateadded', 'productcode', 'price', 'quantity', 'category_type', )





##********>>>>>>> Form Query......................................

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["owner", "name", "task_date", "start_time", "end_time"]
























##********>>>>>>> Đây là chương trình THÊM/SỬA/XÓA KPI DANH MỤC KPI CÁ NHÂN......................................
class dmkpi_form(forms.ModelForm):
    class Meta:
        model = dmkpi
        fields = '__all__'


#<<<<<<... Kết thúc chương trình THÊM/SỬA/XÓA Danh mục KPI CÁ NHÂN............................................
class dmkpi_SearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = dmkpi
        fields = ['Ten_KPI', 'LoaiCV']


##********>>>>>>> Đây là chương trình THÊM/SỬA/XÓA KPI DANH MỤC KPI ĐƠN VỊ......................................
class kpi_dv_f(forms.ModelForm):
    #export_to_CSV = forms.BooleanField()
    class Meta:
        model = Dmkpi_dv
        fields = '__all__'
        widgets = {
            'Ma_KPo': forms.TextInput(attrs={'class':'form-control'}),

            'Ten_KPo': forms.TextInput(attrs={'class':'form-control'}),
            'Ten_KPI': forms.TextInput(attrs={'rows':3, 'cols':5,'class':'form-control'}),
            'Don_vi_tinh': forms.Select(attrs={'class':'form-select'}),
           # 'Chitieu_KPI': forms.TextInput(attrs={'class':'form-control'}),
          #  'Ti_trong': forms.TextInput(attrs={'class':'form-control'}),
            'Vien_canh_cluoc': forms.Select(attrs={'class':'form-select', 'size':'1'}),
            'Tan_xuat_d_gia': forms.Select(attrs={'class':'form-select'}),
            'Dv_quanly_KPI': forms.Select(attrs={'class':'form-select'}),
                  }
#<<<<<<... Kết thúc chương trình THÊM/SỬA/XÓA Danh mục KPI ĐƠN VỊ............................................



##********>>>>>>> Đây là form: KPI ......................................
class giao_KPI_f(forms.ModelForm):
    class Meta:
        model = giao_KPI
        fields = '__all__'
        widgets = {
            'Ten_KPI': forms.TextInput(attrs={'class':'form-control'}),
            'Ky_giao_KPI': forms.Select(attrs={'class':'form-control'}),
            'Nguoigiao': forms.Select(attrs={'class':'form-control'}),
            'Nguoi_nhan': forms.TextInput(attrs={'class':'form-control'}),
            'Ti_trong': forms.TextInput(attrs={'class':'form-control'}),
                  }
 #<<<<<<... Kết thúc chương trình THÊM/SỬA/XÓA Danh mục KPI ĐƠN VỊ............................................

