import datetime
from django.core import validators
from django import forms

from django.conf import settings
from .models import *


#********>>>>>>> Đây là chương trình THÊM/SỬA/XÓA KPI DANH MỤC NHÂN VIÊN......................................



class Form_FNhanvien(forms.ModelForm):
    Xuất_word = forms.BooleanField(required=False)
    class Meta:
        model = Nhan_vien
        fields = '__all__'

class Form_Nhanvien(forms.ModelForm):
    Tất_cả  = forms.BooleanField(required=True)
    thang = forms.CharField()

    class Meta:
        model = Nhan_vien
        fields = '__all__'
        widgets = {
            'NGAYSINH': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'ngay_vao_dv': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'ngay_sinh': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'ngay_cap_CCCD': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'ngay_cap_hochieu': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'ngay_cap_sld': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'Ngay_vao_dang': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'Ngay_ct': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'Ngay_vao_doan': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'Tu_ngay_chuc_vu_da_qua': forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),
            'Den_ngay_huc_vu_da_qua': forms.DateInput(format=('%d-%m-%Y'), attrs={'class': 'form-control','placeholder': 'Chọn ngày','type': 'date'}),

        }


#class Form_Nhanvien(forms.ModelForm):

  #  class Meta:
        #model = Nhan_vien
       # fields = '__all__'

        #fields =['ma_nhan_vien', 'ho_lot_thuong_dung', 'ten_thuong_dung', 'vitri_CV', 'avatar','tel_dd', 'email', 'C_danh_kiem_nhiem', 'Gioi_tinh', 'Nguoi_qly']
        #
       # fields = ['ho_lot_thuong_dung','ten_thuong_dung', 'Chieu_cao',  'Can_nang', 'dd_nhan_dang', 'Danh_hieu_ph_tang']
      #Nhóm 4:  fields = [ 'trinhdovh',  'trinhdo', 'trinh_do_ctri', 'trinh_do_ql']

       #Nhóm 3 fields = [  'Masothue_cn', 'so_so_ld', 'so_so_bhxh', 'ngay_cap_sld', 'ma_phieu_kcb', 'Taikhoan_nh', 'Ten_nganhang','dc_hiennay','px_cu_tru','qh_cu_tru','tinh_cu_tru','dc_thuong_tru','px_thuong_tru','qh_thuong_tru','ma_tinh_thuong_tru']

      #Nhóm 2  fields = [ 'vitri_CV', 'avatar','tel_dd', 'email', 'C_danh_kiem_nhiem', 'Gioi_tinh', 'Nguoi_qly', 'ho_lot_thuong_dung', 'ngay_sinh','ma_tinh_noi_sinh', 'so_CCCD', 'ngay_cap_CCCD', 'ton_giao', 'dan_toc','Tinhtrang_gd', 'So_nguoi_phuthuoc', 'thanhphan_gd','Nguyen_quan']


 #fields = ['ho_lot_thuong_dung','ten_thuong_dung', 'Ngay_vao_dang',  'Ngay_ct', 'Tai_chi_bo', 'Chuc_vu_dang', 'Ngay_vao_doan','Noi_vao_doan', 'Chuc_vu_doan']

# fields =['ngay_sinh', 'ma_tinh_noi_sinh', 'so_CCCD', 'ngay_cap_CCCD', 'avatar','tel_dd', 'email', 'C_danh_kiem_nhiem', 'Gioi_tinh', 'Nguoi_qly', ]


class Form_Nhanvien_TTCN(forms.ModelForm):
    class Meta:
        model = Nhan_vien
        fields =['ma_nhan_vien', 'ho_lot_thuong_dung', 'ten_thuong_dung', 'vitri_CV', 'avatar','tel_dd', 'email']


class NhanvienSearchForm(forms.ModelForm):
    Xuất_Excel = forms.BooleanField(required=False)
    class Meta:
        model = Nhan_vien
        fields = ['ho_lot_thuong_dung', 'ten_thuong_dung', 'vitri_CV']
        widgets = {
            'ho_lot_thuong_dung': forms.TextInput(attrs={'class':'form-control'}),
            'ten_thuong_dung': forms.TextInput(attrs={'class':'form-control'}),
           # 'tel_dd': forms.NumberInput(attrs={'class':'form-control'}),
           # 'email': forms.EmailField(attrs={'class':'form-control'}),
            'vitri_CV': forms.Select(attrs={'class':'form-select'}),
        }



 #_--------------Chương trinh load tỉnh, huyện, xã...

from nhansu.models import Tinh, Quan_huyen, Phuong_xa

from nhansu.models import Bo_phan,To_nhom

#---------------
class DiaphuongForm(forms.ModelForm):
    class Meta:
        model = Nhan_vien
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['quan_huyen'].queryset = Quan_huyen.objects.none()
        self.fields['phuong_xa'].queryset = Phuong_xa.objects.none()

        self.fields['bo_phan'].queryset = Bo_phan.objects.none()
        self.fields['to_nhom'].queryset = To_nhom.objects.none()

        if 'tinh_thanh' in self.data:
            try:
                tinh_thanh_id = int(self.data.get('tinh_thanh'))
                self.fields['quan_huyen'].queryset = Quan_huyen.objects.filter(Tinh_thanh_id=tinh_thanh_id).order_by('Ten_quan')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['quan_huyen'].queryset = self.instance.quan_huyen.quan_huyen_set.order_by('Ten_quan')

        if 'quan_huyen' in self.data:
            try:
                quan_huyen_id = int(self.data.get('quan_huyen'))
                self.fields['phuong_xa'].queryset = Phuong_xa.objects.filter(quan_huyen_id=quan_huyen_id).order_by('Ten_xa')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['phuong_xa'].queryset = self.instance.phuong_xa.phuong_xa_set.order_by('Ten_xa')


#-------------------------
        if 'don_vi' in self.data:
            try:
                don_vi_id = int(self.data.get('don_vi'))
                self.fields['bo_phan'].queryset = Bo_phan.objects.filter(don_vi_id=don_vi_id).order_by('ten_bp')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['bo_phan'].queryset = self.instance.don_vi.bo_phan_set.order_by('ten_bp')

        if 'bo_phan' in self.data:
            try:
                bo_phan_id = int(self.data.get('bo_phan'))
                self.fields['to_nhom'].queryset = To_nhom.objects.filter(bo_phan_id=bo_phan_id).order_by('ten_to')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['to_nhom'].queryset = self.instance.bo_phan.to_nhom_set.order_by('ten_to')





