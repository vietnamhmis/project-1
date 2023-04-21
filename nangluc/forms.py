from django import forms
from .models import Congviec_nangluc, Danhgia_nluc
from mota_cv.models import Mota_Cv7



class nang_luc_cv_form(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Congviec_nangluc
        fields = ['id', 'chucdanh_CV']
        widgets = {

            'chucdanh_CV': forms.Select(attrs={'class':'form-select'}),
        }

class mota_cv_form(forms.ModelForm):

    class Meta:
        model = Mota_Cv7
        fields = ['id', 'Ten_Nhom_CV']
        widgets = {

            'Ten_vitri_full': forms.Select(attrs={'class':'form-select'}),
        }


class Congviec_nangluc_form(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Congviec_nangluc
        fields = ['name','chucdanh_CV','nangluc_cv','Muc_quantrong_nluc','Muc_thanhthao_nluc']

        labels = {

            'chucdanh_CV':('Chức danh công việc'),
            'nangluc_cv':('Năng lực công việc'),
            'Muc_quantrong_nluc':('Mức độ quan trọng tiêu chuẩn năng lực'),
            'Muc_thanhthao_nluc':('Mức độ thành thạo năng lực'),
        }

        widgets = {
           'chucdanh_CV': forms.Select(attrs={'class':'form-select'}),
           'nangluc_cv': forms.Select(attrs={'class':'form-select'}),
           'Muc_quantrong_nluc': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
           'Muc_thanhthao_nluc': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
        }



class Danhgia_nlform(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    Xuất_Word = forms.BooleanField(required=False)
    Báo_cáo_TH = forms.BooleanField(required=False)
    class Meta:
        model = Congviec_nangluc
        fields = ['name',]

#---------------------------------------
class Khung_nangluc(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Congviec_nangluc
        fields = ['name','chucdanh_CV', 'nangluc_cv',]

#---------------------------------------



class Danhgia_nangluc_form(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    Xuất_Word = forms.BooleanField(required=False)
    Báo_cáo_TH = forms.BooleanField(required=False)
    class Meta:
        model = Danhgia_nluc
        fields = [
           'Landanhgia_nagluc','TenNangluc_congviec','Nhanvien_dg_nangluc', 'tu_danhgia_dapung', 'Quanly_dg_nangluc',  'Quanly_danhgia',
        ]
        labels = {
            'name':('Đợt đánh giá năng lực công việc'),
            'Nhanvien_dg_nangluc':('Nhân viên đánh giá Năng lực'),

            'tu_danhgia_dapung':('Tự đánh giá năng lực'),
            'Quanly_dg_nangluc':('Quản lý trực tiếp đánh giá Năng lực'),
            'Quanly_danhgia':('Quản lý đánh giá năng lực'),
        }

        widgets = {
           'tu_danhgia_dapung': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
           'Quanly_danhgia': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
           'Tile_hoanthanh': forms.NumberInput(attrs={'class':'form-control','ROWS':'1'}),
        }

class Danhgia_nangluc_up_form(forms.ModelForm):
    class Meta:
        model = Danhgia_nluc
        fields = ['tu_danhgia_dapung']
        labels = {
          #  'Nhanvien_dg_nangluc':('Nhân viên đánh giá Năng lực'),
            'tu_danhgia_dapung':('Tự đánh giá năng lực'),}

class Danhgia_nangluc_up_formQL(forms.ModelForm):
    class Meta:
        model = Danhgia_nluc
        fields = ['Quanly_danhgia']
        labels = {
          #  'Nhanvien_dg_nangluc':('Nhân viên đánh giá Năng lực'),
            'Quanly_danhgia':('Điểm do Quản lý trực tiếp đánh giá'),}


#-----------------------------------------
