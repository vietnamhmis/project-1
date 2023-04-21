from django import forms
from .models import Khung_kpi, Danhgia_KPI
from mota_cv.models import Mota_Cv7

class Mota_cv_form(forms.ModelForm):
    class Meta:
        model = Mota_Cv7
        fields = ['id', 'Ten_Nhom_CV']
        widgets = {

            'Ten_vitri_full': forms.Select(attrs={'class':'form-select'}),
        }

#---------------------------------------
class Khung_KPI_form(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    Tất_cả  = forms.BooleanField(required=False)
    class Meta:
        model = Khung_kpi
        fields = ['name','chucdanh_CV', 'kpi_cv', 'ti_trong', 'chi_tieu']
        labels = {
            'chucdanh_CV':('Chức danh công việc'),
            'kpi_cv':('KPI công việc'),
            'ti_trong':('Tỉ trọng'),
            'chi_tieu':('Chỉ tiêu'),

        }

        widgets = {
           'chucdanh_CV': forms.Select(attrs={'class':'form-select'}),
           'kpi_cv': forms.Select(attrs={'class':'form-select'}),
           'ti_trong': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
           'chi_tieu': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
        }


class Khung_KPI_form_update(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Khung_kpi
        fields = "__all__"
        labels = {
            'chucdanh_CV':('Chức danh công việc'),
            'kpi_cv':('KPI công việc'),
            'ti_trong':('Tỉ trọng'),

        }

        widgets = {
           'chucdanh_CV': forms.Select(attrs={'class':'form-select'}),
           'kpi_cv': forms.Select(attrs={'class':'form-select'}),
           'ti_trong': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
        }
#---------------------------------------


class Danhgia_KPI_form(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    Xuất_Word = forms.BooleanField(required=False)
    Báo_cáo_TH = forms.BooleanField(required=False)
    Tất_cả  = forms.BooleanField(required=False)

    class Meta:
        model = Danhgia_KPI
        fields = [
           'Landanhgia_KPI','Ten_kpi','Nhanvien_dg_KPI','tu_danhgia_dapung', 'Quanly_danhgia',
        ]
        labels = {
            'name':('Đợt đánh giá năng lực công việc'),
            'Nhanvien_dg_KPI':('Nhân viên ĐƯỢC đánh giá kpi'),
            'tu_danhgia_dapung':('Tự đánh giá năng lực'),
            'Quanly_danhgia':('Quản lý trực tiếp đánh giá '),
            'Ketqua_danhgia':('Đánh giá chung, cuối'),
        }

        widgets = {

           'tu_danhgia_dapung': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
           'Quanly_danhgia': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
           'Ketqua_danhgia': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
        }

